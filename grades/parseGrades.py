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

Formgrade yaml output produces a list of dicts of the following structure: 


   {
    'matrikelnr': '',
    'assignments': [
        {'point': 18.0,
        'group': 'gp1_16_244',
        'assignment': 1,
        'mail': 'None'},
        {'point': 20.0,
        'group': 'gp1_16_291',
        'assignment': 2, 'mail': 'None'},
        {'point': 18.0, 'group': 'gp1_16_83', 'assignment': 3, 'mai
l': 'None'},
        {'point': 0, 'group': 'None', 'assignment': 4, 'mail': 'None'}, {'point': 0, 'group': 'None', 'assignment':
 5, 'mail': 'None'}
        ]
    }


"""


import yaml
import sys
from collections import defaultdict
from pprint import pprint as pp
from jinja2 import Template
import sys 

############

def getManual(gradefile):
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

    return finalgrades

###########

def getFormgrades(gradefile):
    with open(gradefile) as y:
        grades = yaml.load(y)

    grades = grades['submit_details']

    # sanitize the assignment names to match the manual format
    for tmp in grades:
        matrikel = tmp['matrikelnr']
        a = tmp['assignments']
        for aa in a:
            # print(aa)
            aa['assignment'] = int(aa['assignment'][3:])
            aa['manual'] = 0
            
    return grades

############

def merge(formgrades, manualgrades):

    for student in formgrades:
        matrikel = student['matrikelnr']
        assignments = student['assignments']
        try:
            matrikelint = int(matrikel)
        except Exception:
            sys.stderr.write("non-integer matrikelnummer {}".format(matrikel))
        else:
            if int(matrikel) in manualgrades:
                mangrade = manualgrades[int(matrikel)]
                # print('adding {}:  {}'.format(matrikel, mangrade))
                for aa in assignments:
                    try:
                        aa['manual'] = mangrade[aa['assignment']]
                    except Exception:
                        pass

        for aa in assignments:
            aa['total'] = aa['manual']  + aa['point']

                
############

def texescape(s):
    tex_replacements = [
        ('{', r'\{'),
        ('}', r'\}'),
        ('[', r'{[}'),
        (']', r'{]}'),
        ('\\', r'\textbackslash{}'),
        ('$', r'\$'),
        ('%', r'\%'),
        ('&', r'\&'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('~', r'\textasciitilde{}'),
        ('^', r'\textasciicircum{}'),
        ]
    mapping = dict((ord(char), rep) for char, rep in tex_replacements)
    s = s.translate(mapping)
    return s
        
def escape(formgrades, fields):
    """Latex-escape text in fields of assignments"""

    for student in formgrades:
        student['matrikelnr'] = texescape(student['matrikelnr'])
        assignments = student['assignments']
        for aa in assignments:
            for f in fields:
                aa[f] = texescape(aa[f])
            

############

def output(formgrades):

    template = Template(r"""
\documentclass{article}
\begin{document}
\section{Punkteübersicht}
\begin{description}
{% for g in grades %} 
\item[Matrikelnummer {{ g.matrikelnr }} ]~\\
\begin{description}
{% for a in g.assignments %}
\item[Hausblatt {{ a.assignment }}: ]
\begin{description}
\item[Gruppe:] {{ a.group }}
\item[email:] {{ a.mail }}
\item[Punkte regulär:] {{ a.point }}
\item[Punkte manuell:] {{ a.manual }}
\item[Punkte gesamt:] {{ a.total }}
\end{description}
{% endfor %}
\end{description}
{% endfor %}
\end{description}
\end{document}
""")

    out = template.render(grades=formgrades)
    print(out)

############

# Main: 

if __name__ == "__main__":
    manualgrades = getManual(sys.argv[1])
    formgrades = getFormgrades(sys.argv[2])
    merge(formgrades, manualgrades)
    # pp(formgrades)
    escape(formgrades, ['group', 'mail'])
    output(formgrades)
