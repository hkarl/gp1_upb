"""Setup the home directory of a user,  populating it with 
the required directories and symbolic links. 

Can be called two different ways: 
-u username : only works on this user 
-f filename : a yaml file with users; checks for different formats in use 

Typically needs to be run as root or as the user itself (empty -u is ok)
"""

import argparse
import os
import pwd
import sys
from pathlib import Path
import yaml
import shutil 

sourcevorlesung = Path("/home/jupyterhub/output/vorlesung")
yamlfiles = [
    "/home/jupyterhub/gp1/installation/accounts/accounts.yaml",
    "/home/jupyterhub/gp1/installation/accounts/groupaccounts.yaml",
    "/home/jupyterhub/gp1/installation/accounts/students.yaml",
]

def setup_parser():
    parser = argparse.ArgumentParser(description="Setup user home directories")

    parser.add_argument("--user", "-u",
                            nargs='?',
                            default=None,
                            help="username to setup")
    
    parser.add_argument("--filename", "-f",
                            help="filename to read usernames from")

    parser.add_argument("--all", "-a",
                        default=None,
                        action='store_true',
                        help="Process all user acounts according to yaml files")
    return parser


def handle_file(filename):
    """read in yaml file, call handle_user for each user"""

    with open(filename, "r") as f:
        cfg = yaml.load(f)

    if "groupaccounts" in cfg:
        accounts = [x['acc'] for x in cfg['groupaccounts']]
    elif "students" in cfg:
        accounts = cfg['students']
    elif "admin" in cfg:
        accounts = cfg['admin']
    elif "grader" in cfg:
        accounts = cfg['grader']
    else:
        accounts = []

    for a in accounts:
        print("user: ", a)
        handle_user(user=a)
        
    return None


##################################

def ensure_directories():
    print("Creating directories for user {}".
              format(os.geteuid()))

    username = pwd.getpwuid(os.geteuid())[0]
    home = os.path.expanduser("~" + username)

    print(home)

    Vorlesung  = Path(home) / Path("vorlesung")
    
    try: 
        os.chdir(home)

        try:
            Vorlesung.mkdir()
        except FileExistsError:
            pass
        
        # iterate over all the relevant directories in sourcevorlesung
        for d in sourcevorlesung.glob("ch*"):
            chapter = d.relative_to(sourcevorlesung)
            print(chapter)
            try:
                (Vorlesung / chapter).mkdir()
            except FileExistsError:
                pass

            # And make the various symbolic links:
            for suffix in ['.ipynb', '.tgz', '.pdf']:
                linkpath = Vorlesung / chapter / chapter.with_suffix(suffix)
                targetpath = d / chapter.with_suffix(suffix)
                # print(linkpath)
                # print(targetpath)
                try:
                    linkpath.symlink_to(targetpath)
                except FileExistsError:
                    pass

            # symblink for the figures subdirectory:
            for subdir in ['figures', 'uml']: 
                linkpath = Vorlesung / chapter / Path(subdir)
                targetpath = d / Path(subdir)
                try:
                    linkpath.symlink_to(targetpath)
                    print(linkpath)
                    print(targetpath)
                except FileExistsError:
                    pass
            
            # and finally, a copy of the ipynb file, read/write, owned by user
            source = Vorlesung / chapter / chapter.with_suffix('.ipynb')
            target = Vorlesung / chapter / Path(chapter.stem + "-copy.ipynb")
            # print(source)
            # print(target)
            try:
                shutil.copyfile(str(source), str(target), follow_symlinks=True)
            except Exception as e:
                print("Exception while copying {} to {}: {}".format(
                    source, target, e))
                pass
            
    except Exception as e:
        sys.exit("Unexpected exception: {}".format(e))
    

def handle_user(user=None, uid=None):
    """try to switch to this user; create dirs; switch back to root"""

    # make sure we have a uid
    try:
        if not uid:
            uid = pwd.getpwnam(user)[2]
    except Exception as e:
        print("Failed to get uid for user {}; exception: {}".
                  format(user, e))
        sys.exit("No such user")

    gid = pwd.getpwnam(user)[3]
        
    if os.getuid() != uid:
        # switch to non-root user; work under that uuid
        os.setegid(gid)
        os.seteuid(uid)

    print(uid, os.getuid(), os.geteuid(), os.getegid())
    
    ensure_directories()

    # regain root privilege for next user, if we were root
    # or simply stay this user
    try:
        os.seteuid(os.getuid())
    except:
        print("Failed to regain root from user {}".
                  format(uid))
        sys.exit("Unable to regain root")
        
    
    return None

##################################

if __name__ == "__main__":
    args = setup_parser().parse_args()

    if args.all:
        for f in yamlfiles:
            handle_file(f)
    elif args.filename:
        handle_file(args.filename)
    else:
        if args.user:
            handle_user(user=args.user)
        else:
            # use uid of current user
            handle_user(uid=os.getuid())
