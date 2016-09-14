"""Take an expect script, run it (executing jhsell), 
parse the output to get a compact form."""

import sys
import subprocess

javaprog = sys.argv[1] + ".java.exp"
expect = "/usr/bin/expect"

completeProc = subprocess.run([expect, javaprog],
                                  stdout=subprocess.PIPE,
                                  stderr =subprocess.PIPE,
                                  universal_newlines=True,
                                  )

result = completeProc.stdout

with open(javaprog + ".out", 'w') as out:
    out.write(result)

# get rid of undesirable lines
result = result.split('\n')[1:]
result = filter(lambda x: not x.startswith("| "), result)
result = filter(lambda x: not x.startswith("jshell> "), result)
result = filter(lambda x: not x.startswith("   ...> "), result)
result = filter(lambda x: not x.isspace(), result)
result = filter(lambda x: not x == "", result)

print("\n".join(result))
