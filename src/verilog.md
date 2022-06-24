---
layout: post
title: Verilog Cheat Sheet
slug: verilog_cheat_sheet
date: 2022-04-03 23:52
status: publish
author: Yimin
categories: 
  - Cheatsheet
tags: 
  - Verilog
  - GitHub
excerpt: 记录一下Verilog总忘的syntax
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
    input [63:0] wd3,
    output [63:0] rd1, rd2
  );
  reg [63:0] rf [31:0];
  
  always @(posedge clk)
    if (we3) rf[wa3] <= wd3;
  
  assign rd1 = (ra1!=0)? rf[ra1] : 0;
  assign rd2 = (ra2!=0)? rf[ra2] : 0;

  endmodule
```
