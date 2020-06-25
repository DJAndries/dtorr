#!/bin/sh
ctypesgen -I ../libdtorr/include -L ../libdtorr/lib -ldtorr ../libdtorr/include/dtorr/*.h -o dlib.py
