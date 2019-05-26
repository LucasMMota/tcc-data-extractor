#!/usr/bin/env bash


#########################################
# Installing python and necessary packages
# locally. This script will install python
# into the $PYTHON_DSUS_PATH/bin directory and install
# numpy + scipy
#########################################
DSUS_EXTRACTOR_ROOT_PATH=$(dirname $(dirname $0))
PYTHON_DSUS_PATH=$DSUS_EXTRACTOR_ROOT_PATH/.ubuntu-python-src

# installing python 2.7.3
mkdir -p $PYTHON_DSUS_PATH
wget http://www.python.org/ftp/python/2.7.3/Python-2.7.3.tgz
tar xvzf Python-2.7.3.tgz
cd Python-2.7.3
./configure
make
make altinstall prefix=$PYTHON_DSUS_PATH  # specify local installation directory
ln -s $PYTHON_DSUS_PATH/python2.7 $PYTHON_DSUS_PATH/bin/python
cd ..

# install setuptools and pip for package management
wget http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz#md5=7df2a529a074f613b509fb44feefe74e
tar xvzf setuptools-0.6c11.tar.gz
cd setuptools-0.6c11
$PYTHON_DSUS_PATH/bin/python setup.py install  # specify the path to the python you installed above
cd ..
wget http://pypi.python.org/packages/source/p/pip/pip-1.2.1.tar.gz#md5=db8a6d8a4564d3dc7f337ebed67b1a85
tar xvzf pip-1.2.1.tar.gz
cd pip-1.2.1
$PYTHON_DSUS_PATH/bin/python setup.py install  # specify the path to the python you installed above
