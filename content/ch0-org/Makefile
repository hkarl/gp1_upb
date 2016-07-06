# Build the various output formats for a lecture chapter

SOURCE := $(wildcard *.org)
objects := $(patsubst %.org,%.ipynb,$(wildcard *.org))


build: $(objects)

$(objects): %.ipynb: %.org
	../../build/tangle.sh $< >> ../../build/log


