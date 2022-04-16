---
layout: post
title: Verilog Cheat Sheet
slug: verilog_cheat_sheet
date: 2022-04-03 23:52
status: publish
author: Yimin
categories: 
  - IC Interview
tags: 
  - Verilog
  - GitHub
excerpt: 记录一下Verilog总忘的syntax!
---
[notice]记录一下刷题过程中Verilog总忘，总搞混的语法！[/notice]

## If Statement
When there are more than one commands, add begin ... end syntax for that branch.
```verilog
if ()
else if()
else
```

## Case
Again add begin ... end syntax when there are more than one commands.
```verilog
case (A)
3'b001:
3'b010:
3'b100:
default:
endcase
```
## Loop
Inside always block...
```verilog
integer i;
always @(posedge clk) begin
  for (i=1; i<100; i=i+1) begin
  end
end
```
Outside always block...
```verilog
genvar i;
generate
  for (i=0; i<255; i=i+1) begin loop_name
  end
endgenerate
```
## Duplication
Some examples...
```verilog
assign a = {51{1'b1}};
assign b = {width{A}};
assign {b, a[2:1], c} = {};
assign out = {{24{in[7]}}, in}; // Sign bit extension
assign out = {in[0], in[1], in[2], in[3]}; // Reverse
```
## Onehot
```verilog
module onehot(input [255:0] r1, input [7:0] addr, output out);
  assign out = r[addr];
endmodule
```
## Masking
```verilog
assign Q = r1[addr*4+3 -: 4];
```

## Define a Register File
```verilog
  module regfile(
    input clk,
    input we3,
    input [4:0] ra1, ra2, wa3,
    input [31:0] wd3,
    output [31:0] rd1, rd2
  );
  reg [31:0] rf [31:0];
  
  always @(posedge clk)
    if (we3) rf[wa3] <= wd3;
  
  assign rd1 = (ra1!=0)? rf[ra1] : 0;
  assign rd2 = (ra2!=0)? rf[ra2] : 0;

  endmodule
```

## Typical problems in HDLBits
Create a set of counters suitable for use as a 12-hour clock (with am/pm indicator). Your counters are clocked by a fast-running clk, with a pulse on ena whenever your clock should increment (i.e., once per second).

reset resets the clock to 12:00 AM. pm is 0 for AM and 1 for PM. hh, mm, and ss are two BCD (Binary-Coded Decimal) digits each for hours (01-12), minutes (00-59), and seconds (00-59). Reset has higher priority than enable, and can occur even when not enabled.

The following timing diagram shows the rollover behaviour from 11:59:59 AM to 12:00:00 PM and the synchronous reset and enable behaviour.
```verilog
module top_module(
    input clk,
    input reset,
    input ena,
    output pm,
    output [7:0] hh,
    output [7:0] mm,
    output [7:0] ss); 
    wire enable[4:1];
    
    cnt #(.START(0), .END(9)) ss0(clk, reset, ena, ss[3:0]);
    cnt #(.START(0), .END(5)) ss1(clk, reset, enable[1], ss[7:4]);
    cnt #(.START(0), .END(9)) mm0(clk, reset, enable[2], mm[3:0]);
    cnt #(.START(0), .END(5)) mm1(clk, reset, enable[3], mm[7:4]);
    cnt_hour h(clk, reset, enable[4], hh[7:0], pm);

    assign enable[1] = ena && ss[3:0] == 4'h9;
    assign enable[2] = enable[1] && ss[7:4] == 4'h5;
    assign enable[3] = enable[2] && mm[3:0] == 4'h9;
    assign enable[4] = enable[3] && mm[7:4] == 4'h5;

endmodule

module cnt (
    input clk,
    input reset,
    input ena,
    output reg [3:0] q
);
parameter START = 0, END = 9;
always @(posedge clk)
    if (reset)
        q <= START;
    else if(~ena) q <= q;
    else q <= q < END? q + 1 : START;
endmodule

module cnt_hour (
    input clk,
    input reset,
    input ena,
    output reg [7:0] q,
    output reg pm
);
always @(posedge clk)
    if (reset) q <= 8'h12;
    else if(~ena) q <= q;
    else case (q)
            8'h12: q <= 8'h01;
            8'h09: q <= 8'h10;
            default: q[3:0] <= q[3:0] + 1;
        endcase
always @(posedge clk)
    if (reset) pm <= 0;
    else if(ena && q == 8'h11) pm <= ~pm;
endmodule
```