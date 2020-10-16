import sys
import getopt
print(sys.argv[1:])
arg, _ = getopt.getopt(sys.argv[1:], "dh", ["debug","help"])
print()
