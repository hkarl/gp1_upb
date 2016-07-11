# Top-level makefile

.PHONY: makefiles distribute all cleanall 

# we need an up-to-date rsync to support the chown option (v 3.1 of rsync seems to do the job):
# (on mac: brew install rsync; possibly with a brew tap first)
RSYNC := /usr/local/bin/rsync 

# Webserverdir: this depends on where you mount the group directory 
WEBSERVERDIR := /Volumes/groups/fg-karl/public/http/lehre/ws1617/gp1
# NOTE: resulting URL is: http://groups.uni-paderborn.de/fg-karl/lehre/ws1617/gp1/index.html

# rsync into this directory; this will serve as reference version, with a symbolic link
GP1SERVERDIR := jupyterhub@gp1test.cs.upb.de:output

# use this to ssh in a root
ACCOUNTDIRBASE := root@gp1test.cs.upb.de:/home


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

	# sync into the invidual directories; make sure to set permissions correclty
	# list of acocunts can be optained via a little script, extracting from yaml files
	# NOTE: watch out for the trailing / in the src directory; without it; chown does not work properly
	source ~/.venvs/ansible/bin/activate; cd ../installation/accounts ; python createText.py > account.tmp
	cat ../installation/accounts/account.tmp
	while read acc ; do \
		echo $${acc} ; \
		${RSYNC} -vazhog --chown $${acc}:user ../output/vorlesung/ ${ACCOUNTDIRBASE}/$${acc}/vorlesung-copy ; \
	done <../installation/accounts/account.tmp
	rm ../installation/accounts/account.tmp


makefiles:
	-for d in ch* ; do \
		echo $$d ;   \
		[ ! -f $$d/Makefile ] && ln -s ../template/Makefile $$d ; \
	done


