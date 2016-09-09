#!/bin/bash

# a simple script to release a pue to participants

# USEAGE: dirname of the pue to be released as single parameter!

ssh jupyterhub@gp1test.cs.upb.de "cd gp1 ; git pull"
ssh root@gp1test.cs.upb.de "python3.4 /home/jupyterhub/gp1/build/copy-file-to-user.py -a -s /home/jupyterhub/gp1/uebungen/pue/ -t pue -c $1 -x .ipynb -d figures "
