.PHONY: all fb get view pdf out studentgrade studentmail studentmail-test

fb:
	ssh jupyterhub@gp1.cs.upb.de "cd gp1 ; nbgrader feedback $(ch)"

studentgrade:
	ssh jupyterhub@gp1.cs.upb.de "cd gp1 ; nbgrader studentgrade $(ch)"

studentmail:
	ssh jupyterhub@gp1.cs.upb.de "cd gp1 ; nbgrader studentmail $(ch)"

studentmail-test:
	ssh jupyterhub@gp1.cs.upb.de "cd gp1 ; nbgrader studentmail $(ch) test"

get:
	ssh jupyterhub@gp1.cs.upb.de "cd gp1 ; ./getgrades.sh" > formgrade.yaml

view:
	python parseGrades.py additionalGrades.yaml formgrade.yaml 9

pdf:
	pdflatex grades.tex
	pdflatex grades.tex

put:
	scp grades.pdf jupyterhub@gp1.cs.upb.de:


all: fb studentgrade studentmail-test  get view pdf put 


