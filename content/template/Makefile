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

$(objects): %.ipynb: %.org
	mkdir -p output
	# check whether there is an UML directory to build in
	-[ -d uml ] && (cd uml ; make)
	# building raw files 
	../../build/tangle.sh $< >> ../../build/log
	cp $@ ${OUTPUTDIR}
	cp -r figures ${OUTPUTDIR}

$(pdfs): %.pdf: %.tex
	pdflatex -shell-escape $<
	pdflatex -shell-escape $<
	cp $@ ${OUTPUTDIR} 
	# -[ -z $$DEBUG ] && rm -f *.tex *.tex~ *aux *fdb_latexmk *.fls *.log *.out *.toc 

%.tex: %.org
	../../build/tangle.sh $< >> ../../build/log

$(tgz): %.tgz: %.ipynb
	tar cfz ${OUTPUTDIR}/$*.tgz $< figures

clean:
	-rm *.tgz
	-rm *.tex *.tex~ *aux *fdb_latexmk *.fls *.log *.out *.toc
	-rm *.ipynb *.ipynb~
	-rm *.pdf
	-rm -rf _minted-ch*

