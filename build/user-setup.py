"""Setup the home directory of a user,  populating it with 
the required directories and symbolic links. 

Can be called two different ways: 
-u username : only works on this user 
-f filename : a yaml file with users; checks for different formats in use 

Typically needs to be run as root or as the user itself (empty -u is ok)
"""

import argparse
import os
from pwd import getpwnam
import sys
from pathlib import Path
import yaml


def setup_parser():
    parser = argparse.ArgumentParser(description="Setup user home directories")

    parser.add_argument("--user", "-u",
                            nargs='?',
                            default="",
                            help="username to setup")
    
    parser.add_argument("--filename", "-f",
                            help="filename to read usernames from")

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
        account = []

    for a in account:
        handle_user(user=a)
        
    return None


##################################

def ensure_directories():
    print("Creating directories for user {}".
              format(os.getuid))


def handle_user(user=None, uid=None):
    """try to switch to this user; create dirs; switch back to root"""

    # make sure we have a uid
    try:
        if not uid:
            uid = getpwnam(user)[2]
    except Exception as e:
        print("Failed to get uid for user {}; exception: {}".
                  format(user, e))
        sys.exit("No such user")
        
    
    if os.getuid() is not uid:
        # switch to non-root user; work under that uuid
        os.setresuid(uid, uid, 0)

    ensure_directories()

    # regain root privilege for next user
    try:
        os.setuid(os.getsid())
    except:
        print("Failed to regain root from user {}".
                  format(uid))
        sys.exit("Unable to regain root")
        
    
    return None

##################################

if __name__ == "__main__":
    args = setup_parser().parse_args()
    print(args)

    if args.filename:
        handle_file(args.filename)
    else:
        if args.user:
            handle_user(user=args.user)
        else:
            # use uid of current user
            handle_user(uid=os.getuid())
