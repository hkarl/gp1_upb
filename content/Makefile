# Top-level makefile

.PHONY: makefiles

# so far, just support for lectures: 
DISTRIBUTE := ch0-org ch1-zweck 

buildall: makefiles
	for d in ch* ; do \
		echo $$d ;   \
		make -C $$d build ; \
	done

distribute: makefiles buildall
	# copy output files into the public website: 
	for d in ${DISTRIBUTE} ; do \
		make -C $$d build ; \
		make -C $$d distribute ; \
	done
	# generate the file list ; maybe that has to be constructed from indiviaul parts?
	# how to deal with audio files?
	# copy into gp1 servers user directories; for group and student users 

makefiles:
	-for d in ch* ; do \
		echo $$d ;   \
		[ ! -f $$d/Makefile ] && ln -s ../template/Makefile $$d ; \
	done


