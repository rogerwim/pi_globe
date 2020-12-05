import sys
import getopt
args,_ = getopt.getopt(sys.argv[1:], "dh", ["debug","help"])
print(args)
help = False
debug = False
for argument in args:
	parsed = argument[:1][0]
	if parsed == "-d":
		debug = True
	if parsed == "-h":
		help = True
print(debug,help)
