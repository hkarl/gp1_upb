# Top-level makefile

.PHONY: makefiles distribute all cleanall newch  slidetitles uebungen book

# we need an up-to-date rsync to support the chown option (v 3.1 of rsync seems to do the job):
# (on mac: brew install rsync; possibly with a brew tap first)
RSYNC := /usr/local/bin/rsync 

# Webserverdir: this depends on where you mount the group directory 
WEBSERVERDIR := /Volumes/groups/fg-karl/public/http/lehre/ws1617/gp1
# NOTE: resulting URL is: http://groups.uni-paderborn.de/fg-karl/lehre/ws1617/gp1/index.html

# rsync into this directory; this will serve as reference version, with a symbolic link
# GP1SERVERDIR := jupyterhub@gp1test.cs.upb.de:output
GP1SERVERDIR := jupyterhub@gp1.cs.upb.de:output

# use this to ssh in a root
ACCOUNTDIRBASE := root@gp1test.cs.upb.de:/home


all: buildall book distribute

buildall: makefiles
	for d in ch* ; do \
		echo $$d ;   \
		make -C $$d build ; \
	done

book:
	cd book ; bash ./make.sh

cleanall: makefiles
	for d in ch* ; do \
		make -C $$d clean ; \
	done

depingo:
	# depingo: remove the pingo headers from the generated ipynb
	ipynbs=`find ../output/vorlesung -name "*ipynb"`; for d in $$ipynbs ; do echo $$d ; python depingo.py $$d > pingotmp ; mv pingotmp $$d  ; done 

distribute: depingo

	# generate the file list ; maybe that has to be constructed from indiviaul parts?
	# sourcing: we need a few modules :-( ; note that this has be done in ONE shell invocation!
	source ~/.venvs/ansible/bin/activate; \
	python ../build/createWebpage.py --org . --released ./released.yaml --html ../output/vorlesung/index.html

	# how to deal with audio files?

	# rsync into the webserver
	rsync -vah ../output/ ${WEBSERVERDIR}

	# rsync into gp1 server jupyerhub account; referenced by symbolic links 
	rsync -vazh ../output/ ${GP1SERVERDIR}

	# sync into the invidual directories; make sure to set permissions correclty
	ssh root@gp1.cs.upb.de "python3.4 /home/jupyterhub/bin/copy-file-to-user.py -a -s /home/jupyterhub/output/vorlesung/ -t vorlesung -c ch -x .ipynb -x .tgz -x .pdf -d figures -d uml"



makefiles:
	-for d in ch* ; do \
		echo $$d ;   \
		[ ! -f $$d/Makefile ] && ln -s ../template/Makefile $$d ; \
	done


newch:
	echo "this needs to be called make newch ch=bla"
	mkdir $(ch)
	mkdir $(ch)/figures
	mkdir $(ch)/uml
	cp template/template.org $(ch)/$(ch).org
	ln -s ../template/Makefile $(ch)
	ln -s ../../template/uml.Makefile $(ch)/uml/Makefile


slidetitles: 
	find . -name "*.org" |  xargs grep "^\*\* "  | grep  -v UEBUNG | grep -v TODO | grep -v tmp | grep -v "#+TODO:" | grep -v toc | grep -v template | sed s#\./.*/ch## | sed "s/-\(.*\)org:/ /" | sort -n -k1,1 -s > slidetitles.tmp
	python3 groupby.py 30 "" < slidetitles.tmp > slidetitles
	python3 groupby.py 29 "1 ** Fertig" < slidetitles.tmp > remainingslides


uebungen: slidetitles 
	find . -name "*.org" |  xargs grep "^\*\*\*\? "  | grep -v TODO | grep -v tmp | grep -v "#+TODO:" | grep -v toc | grep -v template | sed s#\./.*/ch## | sed "s/-\(.*\)org:/ /" | sort -n -k1,1 -s > uebungen.tmp
	python uebungen.py 30 < uebungen.tmp > uebungen
	rm uebungen.tmp
