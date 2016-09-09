#!/bin/sh

# TODO: It looks like PyPi no longer has permalinks to tarballs.
COMMONS=materiality.commons-0.1.21

if [ ! -e .bootstrap/src ]; then
    mkdir -p .bootstrap
    curl https://pypi.python.org/packages/source/m/materiality.commons/${COMMONS}.tar.gz \
      -o .bootstrap/${COMMONS}.tar.gz -sS
    tar xfz .bootstrap/${COMMONS}.tar.gz -C .bootstrap
    ln -s ${COMMONS}/src .bootstrap/src
fi
