#!/bin/sh
# -*- mode: shell-script -*-
#
# tangle files with org-mode
#
DIR=`pwd`
FILES=""

# on Holger's Mac: 
EMACS="/Applications/Aquamacs 2.app/Contents/MacOS/Aquamacs"

# in general, Linux: 
# EMACS="emacs"

# on Holger's Mac: 
EMACSDIR="/Users/hkarl/lectures/gp1/installation/emacs.d"
# in general: 
# EMACSDIR="~/.emacs.d"

# wrap each argument in the code required to call tangle on it
for i in $@; do
    FILES="$FILES \"$i\""
done

"$EMACS" -Q --batch \
           --eval "(progn
     ; (add-to-list 'load-path (expand-file-name \"~/src/org/lisp/\"))∑
     ; (add-to-list 'load-path (expand-file-name \"~/src/org/contrib/lisp/\" t))
     (add-to-list 'load-path (expand-file-name \"${EMACSDIR}\"))
     (add-to-list 'load-path (expand-file-name \"${EMACSDIR}/elpa/org-20160704\"))
     (add-to-list 'load-path (expand-file-name \"${EMACSDIR}/elpa/json-mode-1.6.0\"))
     (add-to-list 'load-path (expand-file-name \"${EMACSDIR}/elpa/json-snatcher-20150511.2047\"))
     (add-to-list 'load-path (expand-file-name \"${EMACSDIR}/elpa/json-reformat-20160212.53\"))
     (require 'org)
     ; (require 'org-exp)
     (require 'ob)(require 'ob-tangle)
     (require 'json-mode)
     (require 'ox-juslides)
     (require 'ox-julatex)
     ; setup package options
     (add-to-list 'org-latex-packages-alist '(\"newfloat\" \"minted\")) 
     (add-to-list 'org-latex-packages-alist '(\"\" \"tikz\")) 
     (add-to-list 'org-latex-packages-alist '(\"\" \"forest\")) 
     (setq org-latex-listings 'minted)
     (setq org-latex-minted-options
        '((\"frame\" \"lines\") (\"linenos=true\") (\"mathescape\" \"true\")))
     ; undecided: do I want automatic runnign of all code blocks? 
     ; or manual control in the buffer? currently, left in buffer
     ; (setq org-export-babel-evaluate t)
     ; (setq org-confirm-babel-evaluate nil)
     (mapc (lambda (file)
            (find-file (expand-file-name file \"$DIR\"))
            (org-babel-tangle)
            (org-julatex-export-to-file)
            (message (org-version))
            (org-juslides-export-to-file)
            (kill-buffer)) '($FILES)))" 2>&1
