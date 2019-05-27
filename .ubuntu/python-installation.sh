#!/bin/bash

if ! hash python; then
	sudo apt-get install python
fi

# install setuptools and pip for package management
if ! hash pip; then
	sudo apt-get install python-pip
fi

ping localhost