# Build the various output formats for a LECTURE chapter
# (uebungen still to be decided)

.PHONY: build clean distribute outputdir 

BASETARGETDIR := "/Users/hkarl/lectures/groups/gp1/vorlesung"
DIRNAME := $(shell basename `pwd`)

# OUTPUTDIR: where to collect produced files 
OUTPUTDIR := "../../output/vorlesung/${DIRNAME}"


SOURCE := $(wildcard *.org)
objects := $(patsubst %.org,%.ipynb,$(wildcard *.org))
pdfs := $(patsubst %.org,%.pdf,$(wildcard *.org))
tgz := $(patsubst %.org,%.tgz,$(wildcard *.org))


build: outputdir $(objects) $(pdfs) $(tgz)

outputdir:
	echo "Ensuring ${OUTPUTDIR} exists"
	mkdir -p ${OUTPUTDIR}
	mkdir -p ${OUTPUTDIR}/uml

$(objects): %.ipynb: %.org ../template/header.org
	mkdir -p output
	# check whether there is an UML directory to build in
	-[ -d uml ] && (cd uml ; make)
	# building raw files 
	../../build/tangle.sh $< >> ../../build/log
	# This is a dirty hack; tangle.sh ignores org-latex-classes
	sed -i bak -e '1,/article/s/article/memoir/' *.tex
	# And one more dirty hack: un-center img directives
	sed -i ibak -e 's!<center>\(.*\)</center>!\1!' *.ipynb 
	# This is another dirty hack: change to java notebooks if magic file exists
	-[ -f javakernel ] && make java 
	cp $@ ${OUTPUTDIR}
	cp -r figures ${OUTPUTDIR}
	-cp uml/*png ${OUTPUTDIR}/uml

$(pdfs): %.pdf: %.tex
	pdflatex -shell-escape $<
	pdflatex -shell-escape $<
	cp $@ ${OUTPUTDIR} 
	# -[ -z $$DEBUG ] && rm -f *.tex *.tex~ *aux *fdb_latexmk *.fls *.log *.out *.toc 

%.tex: %.org
	../../build/tangle.sh $< >> ../../build/log

$(tgz): %.tgz: %.ipynb
	touch uml/none.png
	-tar cfz ${OUTPUTDIR}/$*.tgz $< figures uml/*.png

java:
	sed -i "" 's/"display_name": "Python 3"/"display_name": "Java 9"/' *ipynb
	sed -i "" 's/"language": "python"/"languag": "java"/' *ipynb
	sed -i "" 's/"name": "python3"/"name": "java"/' *ipynb

clean:
	-rm *.tgz
	-rm *.tex *.tex~ *aux *fdb_latexmk *.fls *.log *.out *.toc *.lof *.loe
	-rm *.ipynb *.ipynb~
	-rm *.pdf
	-rm -rf _minted-ch*
	-rm *.java *.class *.java.exp *.java.exp.out

copy:
	cp ch*.ipynb ch*.pdf ${OUTPUTDIR}
