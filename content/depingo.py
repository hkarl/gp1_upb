"""Remove the pingo startup code from an ipynb """

import sys

f = sys.argv[1]

with open(f, 'r') as fp:
    t = fp.readlines()

inpingo = False

for l in t:
    if "pingo_host" in l:
        inpingo = True

    if not inpingo:
        print(l, end="")
        
    if inpingo and "print (r.status_code)" in l:
        inpingo = False
        print(r'"\n"')

