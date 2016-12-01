

get:
	ssh jupyterhub@gp1.cs.upb.de "cd gp1 ; ./getgrades.sh" > formgrade.yaml

view:
	python parseGrades.py additionalGrades.yaml formgrade.yaml > grades.tex

pdf:
	pdflatex grades.tex



