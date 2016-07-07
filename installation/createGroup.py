"""Create group accounts along with passwords and hashes"""

import pwgen
import crypt
import yaml

num = 10
fstr = "gp1_16_{i:02d}"

ga = []

for i in range(num):
    acc = fstr.format(i=i)
    pw = pwgen.pwgen(8,symbols=False)
    hsh = crypt.crypt(pw, "gp1")
    ga.append({'acc': acc, 'pw': pw, 'hash': hsh})

print ga

with open('accounts/groupaccounts.yaml', 'w') as f:
    f.write('---\ngroupaccounts:\n')
    f.write(yaml.dump(ga, default_flow_style = False).replace('- {acc', '  - {acc'))
    f.write('...')
    
    
