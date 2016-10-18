import sys
import itertools


numvl = int(sys.argv[1])

lines = sys.stdin.readlines()
skiptext = sys.argv[2]
if skiptext is not "":
    lines = list(
        itertools.dropwhile(lambda x: skiptext not in x,
                                lines))[1:]

numlines = len(lines)
slidespervl = int(numlines/numvl)+1

print(slidespervl)

    

for vl in range(numvl):
    print("=======================")
    print("VL: ", vl+1)
    print("".join(lines[vl*slidespervl:(vl+1)*slidespervl]))
    

