# setuptools required to allow for use of python setup.py develop, may also be important for
# cython/compiling if it is used
import setuptools  

from distutils.core import setup

setup(
    name = 'eegmlwidgets',
    version='0.1.0',
    description="""jupyter widgets eeg lab work""",
    author="""Chris Lee-Messer""",
    # url="https://gitlab.lee-messer.net/cleemesser/eegml-signal",
    # download_url="",
    classifiers=['Topic :: Science :: EEG'],
    packages=['eegmlwidgets'],
    # package_data={}
    # data_files=[],
    # scripts = [],
    )
