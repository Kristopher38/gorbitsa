from sys import argv

instructions = {
	"G": 0,
	"O": 1,
	"R": 2,
	"B": 3,
	"I": 4,
	"T": 5,
	"S": 6,
	"A": 7,
	"g": 8,
	"o": 9,
	"r": 10,
	"b": 11,
	"i": 12,
	"t": 13,
	"s": 14,
	"a": 15
}

output = "v2.0 raw\n"
if argv[1]:
	file = open(argv[1], "r")
	for line in file:
		for instr in line.split(" "):
			output += '{:02x}'.format(instructions[instr.strip()[:1]]) + " "
			if len(instr) == 1:
				output += "00 "
			else:
				output += '{:02x}'.format(int(instr.strip()[1:])) + " "
	file.close()
	outfile = open(argv[2] if len(argv) > 1 else "out.bin", "w")
	outfile.write(output)
	outfile.close()