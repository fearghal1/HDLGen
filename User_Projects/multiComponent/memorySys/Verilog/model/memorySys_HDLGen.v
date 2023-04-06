/* 
   Header section
   Generated by HDLGen, Github https://github.com/abishek-bupathi/HDLGen
   Reference: https://tinyurl.com/VerilogTips 
      
   Component Name : memorySys
   Title          : 2 x 4-digit memory array write/read and bank select mux
*/

/*
   Description
   System contains 2 x synchronous write / combinational read register memory arrays (4 x 
   4-bit arrays)
   ce enable all registers
   selMemBankToBeWritten selects register array memory bank select for writes
   we assertion enables synchronous writes
   Write data is dIn(3:00)

   selMemBankToBeRead selects register array memory bank select for reads, with output 
   data dOut(3:0)

   Author(s)      : Fearghal Morgan
   Company        : University of Galway
   Email          : fearrghal.morgan@university.ie
   Date           : 31/03/2023
*/

/*
   module signal dictionary
   clk	clk signal
   rst	rst signal
   selMemBankToBeWritten	select memory array to be written to
   we	Synchronous write enable
   add	memory address
   dIn	4-bit input data bus
   dOut	4-bit data output
   ce	Chip enable
   selMemBankToBeRead	0 select reg4x4() memory output data, 1 select reg4x4() 
   memory output data
*/

/*  
   internal signal dictionary
   dOut_1	memory back 1 data array
   dOut_0	memory back 0 data array
   selCe1   = ce and selMemBankToBeWritten
   selCe0	= ce and (not 
   selMemBankToBeWritten)
*/

// module declaration
module memorySys(
		clk,
		rst,
		selMemBankToBeWritten,
		we,
		add,
		dIn,
		dOut,
		ce,
		selMemBankToBeRead
	);

	// Port definitions
	input  clk;
	input  rst;
	input  selMemBankToBeWritten;
	input  we;
	input [1:0] add;
	input [3:0] dIn;
	output [3:0] dOut;
	input  ce;
	input  selMemBankToBeRead;

    reg [3:0] dOut;

    // Internal signal declarations
    reg [3:0] dOut_1;
    reg [3:0] dOut_0;
    wire  selCe1;
    wire  selCe0;

mux21_4_i: mux21_4
	(
    .mux21_4_In1 (dOut_1),
    .mux21_4_In0 (dOut_0),
    .sel (selMemBankToBeRead),
    .mux21_4_Out (dOut)
	);

reg4x4_1_i: reg4x4 
    (
	.clk (clk), 
	.rst (rst), 
   	.ce (selCe1),
   	.we (we),
   	.add (add),
   	.dIn (dIn),
   	.dOut (dOut_1)
   	);

reg4x4_1_i: reg4x4 
    (
	.clk (clk), 
	.rst (rst), 
   	.ce (selCe0),
   	.we (we),
   	.add (add),
   	.dIn (dIn),
   	.dOut (dOut_0)
   	);
		
    assign selCe0 = ce; // Complete if required and delete this comment


    assign selCe1 = ce; // Complete if required and delete this comment

endmodule