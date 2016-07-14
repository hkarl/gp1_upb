
# THIS IS BUGGY DO NOT USE!!

# NB: ch0-org/ch0-org.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.ipynb
# copyTo /home/jrossel/vorlesung/ch0-org/ch0-org.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.ipynb
# NB: ch0-org/ch0-org.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.ipynb
# copyTo /home/jrossel/vorlesung/ch0-org/ch0-org.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.ipynb
# NB: ch0-org/ch0-org.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.ipynb
# copyTo /home/jrossel/vorlesung/ch0-org/ch0-org.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.edit.ipynb


""" copy a new version of a lecture notebooks into the students' home directory.
but only there is an unmodified version.

assumption: this is executed by root; cwd is unclear; use absolute paths 

"""

from pathlib import Path
import shutil

HOME="/home"
JUPYTER="jupyterhub"
TARGETDIR = "vorlesung"
SOURCEDIR = "output" 

def get_accounts():
    """turn the yaml account files into simple text files:
    one line per acocunt, just the acocunt name"""

    import yaml

    res = []

    p = Path(HOME)
    p = p / JUPYTER / "gp1/installation/accounts"
    
    with open(str(p / 'groupaccounts.yaml'), 'r') as f:
        cfg = yaml.load(f)

    res = [x['acc'] for x in cfg['groupaccounts']]

    with open(str(p / 'students.yaml'), 'r') as f:
        cfg = yaml.load(f)
    res += cfg['students']
    
    with open(str(p / 'accounts.yaml'), 'r') as f:
        cfg = yaml.load(f)

    res += cfg['admin']
    res += cfg['grader']

    return res

accounts = get_accounts()
print(accounts)
home = Path(HOME)
source = home / JUPYTER / SOURCEDIR /"vorlesung"

for a in accounts: 
    avorlesung = home / a / TARGETDIR

    # go over all notebooks in the sourcedir
    # copy them if needed

    print ('A: ', a, avorlesung, source)
    
    for nb in source.glob('*/*.ipynb'):
        print ('NB:', nb.relative_to(source))
        copyTo = avorlesung / nb.relative_to(source).with_suffix('.edit.ipynb')
    	# os.makedirs(str(copyTo))    

        print ('copyTo', copyTo)
        if not copyTo.exists():
            # then copy the notebook, but give it a different name:
            print ("copy from: ", str(nb), "to: ", copyTo)
            shutil.copy(str(nb), str(copyTo))
            shutil.chown(str(copyTo), user=a, group="user")

