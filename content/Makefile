# Top-level makefile

.PHONY: makefiles

# Webserverdir: this depends on where you mount the group directory 
WEBSERVERDIR := /Volumes/groups/fg-karl/public/http/lehre/ws1617/gp1

# NOTE: resulting URL is: http://groups.uni-paderborn.de/fg-karl/lehre/ws1617/gp1/index.html


buildall: makefiles
	for d in ch* ; do \
		echo $$d ;   \
		make -C $$d build ; \
	done

distribute: buildall
	# generate the file list ; maybe that has to be constructed from indiviaul parts?
	# sourcing: we need a few modules :-( ; note that this has be done in ONE shell invocation!
	source ~/.venvs/ansible/bin/activate; \
	python ../build/createWebpage.py --org . --released ./released.yaml --html ../output/vorlesung/index.html

	# how to deal with audio files?

	# rsync into gp1 servers user directories; for group and student users
	rsync -vah ../output/ ${WEBSERVERDIR}

makefiles:
	-for d in ch* ; do \
		echo $$d ;   \
		[ ! -f $$d/Makefile ] && ln -s ../template/Makefile $$d ; \
	done


