""" turn the yaml account files into simple text files:
one line per acocunt, just the acocunt name
"""

import yaml

with open('students.yaml', 'r') as f:
    cfg = yaml.load(f)
print '\n'.join(cfg['students'])

with open('accounts.yaml', 'r') as f:
    cfg = yaml.load(f)
print '\n'.join(cfg['admin'])
print '\n'.join(cfg['grader'])

with open('groupaccounts.yaml', 'r') as f:
    cfg = yaml.load(f)
print '\n'.join([x['acc'] for x in cfg['groupaccounts']])
