# Top-level makefile

buildall:
	for d in ch* ; do \
		echo $$d ;   \
		[ -f $$d/Makefile ] || ln -s template/Makefile $$d ; \
	done
