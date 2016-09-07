

.PHONY: build clean

SOURCE := $(wildcard *.tex)
PICS := $(patsubst %.tex,%.png,$(wildcard *.tex))

build: $(PICS)

$(PICS): %.png: %.tex
	pdflatex -shell-escape $<
	touch $@

clean:
	-rm *png *pdf *aux *log
