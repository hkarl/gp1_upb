# Build the various output formats for a lecture chapter

.PHONY: build clean distribute 

BASETARGETDIR := "/Users/hkarl/lectures/groups/gp1/vorlesung"
DIRNAME := $(shell basename `pwd`)
TARGETDIR := ${BASETARGETDIR}/${DIRNAME}

SOURCE := $(wildcard *.org)
objects := $(patsubst %.org,%.ipynb,$(wildcard *.org))
pdfs := $(patsubst %.org,%.pdf,$(wildcard *.org))
tgz := $(patsubst %.org,%.tgz,$(wildcard *.org))


build: $(objects) $(pdfs) $(tgz)

$(objects): %.ipynb: %.org
	mkdir -p output 
	# building raw files 
	../../build/tangle.sh $< >> ../../build/log
	cp $@ output

$(pdfs): %.pdf: %.tex
	pdflatex $<
	pdflatex $<
	cp $@ output 
	# -[ -z $$DEBUG ] && rm -f *.tex *.tex~ *aux *fdb_latexmk *.fls *.log *.out *.toc 

%.tex: %.org
	../../build/tangle.sh $< >> ../../build/log

$(tgz): %.tgz: %.ipynb
	tar cfz output/$*.tgz $< figures

distribute:
	# move produced outfiles into place
	# copy into all relevant group directories
	# cp -r output ${TARGETDIR}
	echo copying into ${TARGETDIR} 

clean:
	-rm *.tgz
	-rm *.tex *.tex~ *aux *fdb_latexmk *.fls *.log *.out *.toc
	-rm *.ipynb *.ipynb~
	-rm *.pdf

