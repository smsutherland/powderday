from setuptools import setup, find_packages
from importlib.util import find_spec
from sys import argv
import os

if "--fsps" in argv:
    argv.remove("--fsps")

    os.system(
        "git submodule update --recursive --init -- vendor/python-fsps"
    )  # Download fsps submodule if it doesn't exist. Does nothing if it does.
    os.chdir("vendor/python-fsps/src/fsps/libfsps/src")
    os.system("make clean")
    os.system("make")
    os.chdir("../../../..")
    os.system("python setup.py install")
    os.chdir("../..")

if "--hyperion" in argv:
    argv.remove("--hyperion")

    os.system("git submodule update --recursive --init -- vendor/hyperion")
    os.chdir("vendor/hyperion")
    os.system("python setup.py install")
    os.system(
        "./configure --prefix=$HOME/local"
    )  # Do we really want to hardcode $HOME/local?
    os.system("make")
    os.system("make install")
    os.chdir("../..")

    os.system("git submodule update --recursive --init -- vendor/hyperion-dust")
    os.chdir("vendor/hyperion-dust")
    os.system("python setup.py build_dust")
    os.chdir("dust_files")
    os.system(
        "wget https://github.com/hyperion-rt/paper-galaxy-rt-model/blob/master/dust/big.hdf5"
    )
    os.system(
        "wget https://github.com/hyperion-rt/paper-galaxy-rt-model/blob/master/dust/vsg.hdf5"
    )
    os.system(
        "wget https://github.com/hyperion-rt/paper-galaxy-rt-model/blob/master/dust/usg.hdf5"
    )
    os.chdir("../../..")


if find_spec("fsps") is None:
    raise Exception(
        "pass `--fsps` or install python-fsps manually, see docs/installation.rst"
    )

if find_spec("hyperion") is None:
    raise Exception(
        "pass `--hyperion` or install Hyperion manually, see docs/installation.rst"
    )

setup(
    name="powderday",
    version="0.1.0",
    packages=find_packages(),
    platforms="any",
    setup_requires=[
        'numpy==1.16; python_version=="2.7"',
        'numpy; python_version>="3.5"',
    ],
    install_requires=[
        'scipy==1.2; python_version=="2.7"',
        'scipy==1.10; python_version>="3.5"',
        'astropy==2.0; python_version=="2.7"',
        'astropy==6; python_version>="3.5"',
        "h5py==3.14.0",
        "yt==4.4.0",
        "unyt==3.0.4",
        "scikit-learn==1.6.1",
        "p_tqdm==1.4.2",
    ],
    scripts=["pd_front_end.py"],
    project_urls={
        "Source": "https://github.com/dnarayanan/powderday.git",
    },
)
