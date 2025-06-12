.PHONY: fsps hyperion hyperion-dust all

all: fsps hyperion hyperion-dust

fsps:
	git submodule update --recursive --init -- vendor/python-fsps
	cd vendor/python-fsps/src/fsps/libfsps/src/ && make clean
	cd vendor/python-fsps/src/fsps/libfsps/src/ && make
	cd vendor/python-fsps/ && python setup.py install


hyperion:
	git submodule update --recursive --init -- vendor/hyperion
	cd vendor/hyperion/ && pip install .
	cd vendor/hyperion/ && ./configure --prefix=${HOME}/local
	cd vendor/hyperion/ && make
	cd vendor/hyperion/ && make install

hyperion-dust: hyperion
	git submodule update --recursive --init -- vendor/hyperion-dust
	cd vendor/hyperion-dust/ && python setup.py build_dust
	cd vendor/hyperion-dust/dust_files/ && wget https://github.com/hyperion-rt/paper-galaxy-rt-model/blob/master/dust/big.hdf5
	cd vendor/hyperion-dust/dust_files/ && wget https://github.com/hyperion-rt/paper-galaxy-rt-model/blob/master/dust/vsg.hdf5
	cd vendor/hyperion-dust/dust_files/ && wget https://github.com/hyperion-rt/paper-galaxy-rt-model/blob/master/dust/usg.hdf5
