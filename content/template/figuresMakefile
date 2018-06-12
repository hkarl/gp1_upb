

.PHONY: build clean

SOURCE := $(wildcard *.tex)
PICS := $(patsubst %.tex,%.pdf,$(wildcard *.tex))
PNGS := $(patsubst %.tex,%.png,$(wildcard *.tex))

build: 
	make $(PICS)
	make $(PNGS)

$(PICS): %.pdf: %.tex
	pdflatex -shell-escape $< 

$(PNGS): %.png: %.pdf
	convert -density 300 $< $@

clean:
	-rm *aux *log $(PICS) $(PICS) *.synctex.gz 
