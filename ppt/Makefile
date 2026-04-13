.PHONY: all clean cleandist install release

all:
	make -C source/ all

clean:
	make -C source/ clean

cleandist:
	make -C source/ cleandist

install:
	sudo ./install/unix.sh

release:
	./makerelease ./release/
