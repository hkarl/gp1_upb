

get:
	ssh jupyterhub@gp1.cs.upb.de "cd gp1 ; ./getgrades.sh" > formgrade.yaml

view:
	python parseGrades.py additionalGrades.yaml formgrade.yaml 

pdf:
	pdflatex grades.tex

put:
	scp grades.pdf jupyterhub@gp1.cs.upb.de:


all: get view pdf put 


