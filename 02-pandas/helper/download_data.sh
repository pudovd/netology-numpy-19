#!/bin/sh

BASE_URL=https://files.grouplens.org/datasets/movielens/

if [ -d 'ml-latest-small' ]; then
	echo "Data already downloaded."
	echo "Current files:"
	echo "====================="
	find ml-latest-small/
	echo "====================="
else
	wget ${BASE_URL}ml-latest-small.zip --no-check-certificate
	unzip ml-latest-small.zip
	rm ml-latest-small.zip
fi

