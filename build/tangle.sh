#!/bin/sh
# -*- mode: shell-script -*-
#
# tangle files with org-mode
#
DIR=`pwd`
FILES=""

# wrap each argument in the code required to call tangle on it
for i in $@; do
    FILES="$FILES \"$i\""
done

emacs -Q --batch \
           --eval "(progn
     ; (add-to-list 'load-path (expand-file-name \"~/src/org/lisp/\"))∑
     ; (add-to-list 'load-path (expand-file-name \"~/src/org/contrib/lisp/\" t))
     (add-to-list 'load-path (expand-file-name \"/home/jupyterhub/.emacs.d\"))
     (add-to-list 'load-path (expand-file-name \"/home/jupyterhub/.emacs.d/elpa/org-20160704\"))
     (add-to-list 'load-path (expand-file-name \"/home/jupyterhub/.emacs.d/elpa/json-mode-1.6.0\"))
     (add-to-list 'load-path (expand-file-name \"/home/jupyterhub/.emacs.d/elpa/json-snatcher-20150511.2047\"))
     (add-to-list 'load-path (expand-file-name \"/home/jupyterhub/.emacs.d/elpa/json-reformat-20160212.53\"))
     (require 'org)
     ; (require 'org-exp)
     (require 'ob)(require 'ob-tangle)
     (require 'json-mode)
     (require 'ox-juslides)
     (mapc (lambda (file)
            (find-file (expand-file-name file \"$DIR\"))
            (org-babel-tangle)
            (org-latex-export-to-latex)
            (message (org-version))
            (org-juslides-export-to-file)
            (kill-buffer)) '($FILES)))" 2>&1
