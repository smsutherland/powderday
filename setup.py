from setuptools import setup, find_packages
from importlib.util import find_spec


if find_spec("fsps") is None:
    raise Exception(
        "run `make fsps` or install python-fsps manually, see docs/installation.rst"
    )

if find_spec("hyperion") is None:
    raise Exception(
        "run `make hyperion` or install Hyperion manually, see docs/installation.rst"
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
