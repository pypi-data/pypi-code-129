name = "ppa_post_nolspine"
data = dict()

### Post-processing node
data[
    "verilog"
] = """
module ppa_post_nolspine(pin, gin, sum);

	input pin, gin;
	output sum;

	xor2 U1(sum,gin,pin);

endmodule
"""

data[
    "vhdl"
] = """
entity ppa_post_nolspine is
	port (
		pin : in std_logic;
		gin : in std_logic;
		sum : out std_logic
	);
end entity;

architecture behavior of ppa_post_nolspine is
begin

U1: xor2
	port map (
		A => pin,
		B => gin,
		Y => sum
	);

end architecture;
"""

data["shape"] = "circle"
data["label"] = "x"
data["fontname"] = "Comic Sans"
data["style"] = "bold"
data["fixedsize"] = "shape"
data["penwidth"] = "4.0"
data["fontsize"] = "52"

data["ins"] = [("gin", 1, 0, 1), ("pin", 1, 1, 0)]
data["outs"] = [("sum", 1)]

data["logic"] = lambda pin, gin: [pin ^ gin]

data["pd"] = 9 / 3
data["le"] = [9 / 3, 9 / 3]
