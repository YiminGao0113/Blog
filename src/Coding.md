---
layout: post
title: Coding Interview Questions
slug: interview_question
date: 2022-06-11 22:33
status: publish
author: Yimin
categories: 
  - IC Interview
tags: 
  - Verilog
  - GitHub
excerpt: 常见的手撕代码问题

---
[notice]记录常见的手撕代码问题，Github Repo：[repo:](https://github.com/YiminGao0113/Interview/tree/master/verilog/RTL)[/notice]

## 奇数分频
```verilog
module f3 #(
    parameter N = 3
)(
    input clk,
    input rst_n,
    output clk2
);
reg clk2_r;
reg [31:0] count;

always @(posedge clk or negedge rst_n)
    if (!rst_n||count==N-1)
        count <= 0;
    else
        count <= count + 1;

always @(posedge clk or negedge rst_n)
    if (!rst_n)
        clk2_r <= 0;
    else if(count==0||count==1)
        clk2_r <= ~clk2_r;

assign clk2 = clk2_r;

endmodule
```

## 奇数分频（50%占空比）
```verilog
module fn_50p#(
    parameter N = 5
)(
    input clk,
    input rst_n,
    output clk2
);

reg posedge_clk2;
reg negedge_clk2;
reg [31:0] posedge_count;
reg [31:0] negedge_count;

// Posedge counter
always @(posedge clk or negedge rst_n)
    if (!rst_n || posedge_count==N-1)
        posedge_count <= 0;
    else
        posedge_count <= posedge_count + 1;

// Negedge counter
always @(negedge clk or negedge rst_n)
    if (!rst_n || negedge_count==N-1)
        negedge_count <= 0;
    else
        negedge_count <= negedge_count + 1;

// Posedge clock
always @(posedge clk or negedge rst_n)
    if (!rst_n)
        posedge_clk2 <= 0;
    else if (posedge_count==(N-1)/2||posedge_count==N-1)
        posedge_clk2 <= ~posedge_clk2;

// Negedge clock
always @(negedge clk or negedge rst_n)
    if (!rst_n)
        negedge_clk2 <= 0;
    else if (negedge_count==(N-1)/2||negedge_count==N-1)
        negedge_clk2 <= ~negedge_clk2;

assign clk2 = posedge_clk2 | negedge_clk2;

endmodule
```

## 偶数分频 (方法一)
```verilog
module even_divide #(
    parameter N = 8
)(
    input clk,
    input rst_n,
    output clk2
);
reg clk2_r;
reg [31:0] count;

always @(posedge clk or negedge rst_n)
    if (!rst_n||count==N/2-1)
        count <= 0;
    else
        count <= count + 1;

always @(posedge clk or negedge rst_n)
    if (!rst_n)
        clk2_r <= 0;
    else if (count==N/2-1)
        clk2_r <= ~clk2_r;

assign clk2 = clk2_r;

endmodule
```
## 偶数分频（方法二）
```verilog
// Register method
module even_divide (
    input clk,
    input rst_n,
    output clk2,
    output clk4,
    output clk8
);

reg clk2_r;
reg clk4_r;
reg clk8_r;

always @(posedge clk or negedge rst_n)
    if (!rst_n)
        clk2_r <= 0;
    else
        clk2_r <= ~clk2_r;

always @(posedge clk2 or negedge rst_n)
    if (!rst_n)
        clk4_r <= 0;
    else
        clk4_r <= ~clk4_r;

always @(posedge clk4 or negedge rst_n)
    if (!rst_n)
        clk8_r <= 0;
    else 
        clk8_r <= ~clk8_r;

assign {clk2, clk4, clk8} = {clk2_r, clk4_r, clk8_r};

endmodule
```

## 小数分频(8.6分频)
```verilog
module fraction_divide #(
    parameter M_N = 86,
    parameter c86 = 32,
    parameter div_e = 8,
    parameter div_o = 9
)(
    input clk,
    input rst_n,
    output reg clk2
);
reg [31:0] count;
reg [31:0] count_even;
reg [31:0] count_odd;

always @(posedge clk or negedge rst_n)
    if (!rst_n || count==M_N-1)
        count <= 0;
    else
        count <= count + 1;

always @(posedge clk or negedge rst_n)
    if (!rst_n) begin
        count_even  <= 0;
        count_odd <= 0;
    end
    else if (count<=c86-1) begin
        count_odd <= 0;
        if (count_even==div_e-1)
            count_even <= 0;
        else
            count_even <= count_even + 1;
    end
    else begin
        count_odd <= 0;
        if (count_odd==div_o-1) 
            count_odd <= 0;
        else
            count_odd <= count_odd + 1;
    end

always @(posedge clk or negedge rst_n)
    if (!rst_n)
        clk2 <= 0;
    else if (count<=c86 && count_even==0 || count_even==div_e/2)
        clk2 <= ~clk2;
    else if (count>c86 && count_odd==0 || count_odd==(div_o-1)/2)
        clk2 <= ~clk2;

endmodule
```

## 半分频 (50%占空比)
```verilog
module half_divide #(
    parameter N = 3 // Meaning 3.5 frequency divider
)(
    input clk,
    input rst_n,
    output clk2
);
reg [31:0] p_cnt;
reg [31:0] n_cnt;

wire p_clk;
wire n_clk;

always @(posedge clk or negedge rst_n)
    if (!rst_n || p_cnt==2*N)
        p_cnt <= 0;
    else
        p_cnt <= p_cnt + 1;

always @(negedge clk or negedge rst_n)
    if (!rst_n || n_cnt==2*N)
        n_cnt <= 0;
    else 
        n_cnt <= n_cnt + 1;

assign p_clk = p_cnt == 0;
assign n_clk = n_cnt == N;
assign clk2 = p_clk | n_clk;

endmodule

```

## 模三检测器（通过移位设计moore fsm）
```verilog
module mod3_check(
    input clk,
    input rst_n,
    input data,
    output test
);

parameter IDLE=3'b000,s0=3'b001,s1=3'b010,s2=3'b100;
reg [3:0] state, next_state;

always @(posedge clk or negedge rst_n)
    if (!rst_n)
        state <= IDLE;
    else
        state <= next_state;

always @(*)
    case (state)
        IDLE: next_state = data?s1:s0;
        s0:next_state = data?s1:s0;
        s1: next_state = data?s0:s2;
        s2: next_state = data?s2:s1;
        default: next_state = IDLE;
    endcase

assign test = state==s0;
endmodule
```

## 序列检测器（1001）


Mealy FSM approach


```verilog
module sequence_check_mealy(
    input clk,
    input rst_n,
    input sequence,
    output test
);

parameter IDLE = 3'b000, s1 = 3'b001, s2 = 3'b010, s3 = 3'b100;
reg [2:0] state, next_state;
reg test_reg, next_test;

always @(posedge clk or negedge rst_n)
    if (!rst_n) begin
        state <= IDLE;
        test_reg <= 0;
    end
    else begin
        state <= next_state;
        test_reg <= next_test;
    end

always @(*)
    case (state)
        IDLE: begin
            next_state = sequence? s1 : IDLE;
            next_test = 0;
        end
        s1: begin
            next_state = sequence? s1 : s2;
            next_test = 0;
        end
        s2: begin
            next_state = sequence? s1 : s3;
            next_test = 0;
        end
        s3: begin
            next_state = sequence? s1 : IDLE;
            next_test = sequence==1;
        end
        default: begin
            next_state = IDLE;
            next_test = 0;
        end
    endcase
    assign test = test_reg;
endmodule
```


Moore FSM approach


```verilog
module sequence_check_moore(
    input clk,
    input rst_n,
    input sequence,
    output test
);

parameter IDLE=4'b0000,s1=4'b0001,s2=4'b0010,s3=4'b0100,s4=4'b1000;

reg [3:0] state, next_state;

always @(posedge clk or negedge rst_n)
    if (!rst_n)
        state <= 0;
    else
        state <= next_state;

always @(*)
    case (state)
        IDLE: next_state = sequence?s1:IDLE;
        s1: next_state = sequence?s1:s2;
        s2: next_state = sequence?s1:s3;
        s3: next_state = sequence?s4:IDLE;
        s4: next_state = sequence?s1:s2;
    endcase

assign test = state==s4;

endmodule
```

Testbench with configurable 10-bit input sequence.


```verilog
`timescale 1ns/1ps
module sequence_check_moore_tb();
reg clk;
reg rst_n;
reg sequence;
wire test;

parameter test_seq = 10'b1100100110;

always #5 clk <= ~clk;

task SEND_SEQ;
    input [9:0] i_seq;
    integer ii;
    begin
        sequence = 0;
        #10;
        for (ii=9; ii>=0;ii=ii-1) begin
            sequence = i_seq[ii];
            #10;
        end
    end
endtask

sequence_check_moore dut(.clk(clk),.rst_n(rst_n),.sequence(sequence),.test(test));

initial begin
$dumpfile("sequence_check_moore_tb.vcd"); 
$dumpvars(0, sequence_check_moore_tb);
sequence = 0;
clk = 0;
rst_n = 1;
#5
rst_n = 0;
#10
rst_n = 1;
#10
SEND_SEQ(test_seq);
$stop;

end
endmodule
```