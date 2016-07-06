# Build the various output formats for a lecture chapter

.PHONY: build clean distribute 

SOURCE := $(wildcard *.org)
objects := $(patsubst %.org,%.ipynb,$(wildcard *.org))
pdfs := $(patsubst %.org,%.pdf,$(wildcard *.org))
tgz := $(patsubst %.org,%.tgz,$(wildcard *.org))


build: $(objects) $(pdfs) $(tgz)

$(objects): %.ipynb: %.org
	-mkdir output 
	# building raw files 
	../../build/tangle.sh $< >> ../../build/log
	# note: we just copy the notebook file here and
	# delete it after we have generated the tgz file! 
	cp $@ output
	make clean


$(pdfs): %.pdf: %.tex
	pdflatex $<
	pdflatex $<
	mv $@ output 

$(tgz): %.tgz: %.ipynb
	tar cfz output/$<.tgz $< figures
	rm $<

distribute:
	# move produced outfiles into place
	# copy into all relevant group directories
	echo TODO

clean:
	-rm *.tgz
	-rm *.tex *aux *fdb_latexmk *.fls *.log *.out *.toc
	-rm *.ipynb
