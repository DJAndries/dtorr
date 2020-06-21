#!/bin/sh
ctypesgen -I ../dtorr/include -L ../dtorr/lib -ldtorr ../dtorr/include/dtorr/*.h -o dlib.py
