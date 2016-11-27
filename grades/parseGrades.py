"""Parse grades manually entered in yaml format.
Example: 

---
grades:
- matrikel: 1234567
  punkte: 
  - blatt: 1
    punkte: 5
    tutor: jb
  - blatt: 2
    punkte: 17
    tutor: dp
- matrikel: 2345678
  punkte: 
  - blatt: 1
    punkte: 4
    tutor: as
  - blatt: 1
    punkte: 7
    tutor: hk
- matrikel: 2345678
  punkte: 
  - blatt: 1
    punkte: 5
    tutor: as
  - blatt: 7
    punkte: 9
    tutor: hk
...

This script tries to cleanup and collect duplicates, but obvisouly it makes 
very little sense to have duplicates inserted. So watch out what you are doing! 

These points are ADDED to anything that comes out of the studentresult app.  



"""

import yaml
import sys
from collections import defaultdict


gradefile = sys.argv[1]

with open(gradefile) as y:
    grades = yaml.load(y)

grades = grades['grades']
# print(grades)

# cleaup possible duplicates

finalgrades = {}
for m in set([x['matrikel'] for x in grades]):
    mgrades = [x
                for x in grades
                if x['matrikel'] == m]
        
    mfinal = defaultdict(int)

    for p in mgrades:
        for b in p['punkte']:
            mfinal[b['blatt']] += b['punkte']
    
    finalgrades[m] = mfinal

print(finalgrades)
