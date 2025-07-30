.PHONY: fsps hyperion hyperion-dust all

all: fsps hyperion hyperion-dust

fsps:
	git submodule update --recursive --init -- vendor/python-fsps
	$(MAKE) -C vendor/python-fsps/src/fsps/libfsps/src clean
	$(MAKE) -C vendor/python-fsps/src/fsps/libfsps/src
	cd vendor/python-fsps/ && python setup.py install


hyperion:
	git submodule update --recursive --init -- vendor/hyperion
	cd vendor/hyperion/ && pip install .
	cd vendor/hyperion/ && ./configure --prefix=${HOME}/local
	$(MAKE) -C vendor/hyperion
	$(MAKE) -C vendor/hyperion install

hyperion-dust: hyperion
	git submodule update --recursive --init -- vendor/hyperion-dust
	cd vendor/hyperion-dust/ && python setup.py build_dust
	cd vendor/hyperion-dust/dust_files/ && wget https://github.com/hyperion-rt/paper-galaxy-rt-model/blob/master/dust/big.hdf5
	cd vendor/hyperion-dust/dust_files/ && wget https://github.com/hyperion-rt/paper-galaxy-rt-model/blob/master/dust/vsg.hdf5
	cd vendor/hyperion-dust/dust_files/ && wget https://github.com/hyperion-rt/paper-galaxy-rt-model/blob/master/dust/usg.hdf5
