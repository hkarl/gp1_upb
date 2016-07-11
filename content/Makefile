# Top-level makefile

.PHONY: makefiles distribute all cleanall 

# Webserverdir: this depends on where you mount the group directory 
WEBSERVERDIR := /Volumes/groups/fg-karl/public/http/lehre/ws1617/gp1
GP1SERVERDIR := jupyterhub@gp1test.cs.upb.de:output

# NOTE: resulting URL is: http://groups.uni-paderborn.de/fg-karl/lehre/ws1617/gp1/index.html

all: buildall distribute 

buildall: makefiles
	for d in ch* ; do \
		echo $$d ;   \
		make -C $$d build ; \
	done

cleanall: makefiles
	for d in ch* ; do \
		make -C $$d clean ; \
	done


distribute: 
	# generate the file list ; maybe that has to be constructed from indiviaul parts?
	# sourcing: we need a few modules :-( ; note that this has be done in ONE shell invocation!
	source ~/.venvs/ansible/bin/activate; \
	python ../build/createWebpage.py --org . --released ./released.yaml --html ../output/vorlesung/index.html

	# how to deal with audio files?

	# rsync into the webserver
	rsync -vah ../output/ ${WEBSERVERDIR}

	# rsync into gp1 server jupyerhub account; referenced by symbolic links 
	rsync -vazh ../output/ ${GP1SERVERDIR}

makefiles:
	-for d in ch* ; do \
		echo $$d ;   \
		[ ! -f $$d/Makefile ] && ln -s ../template/Makefile $$d ; \
	done


