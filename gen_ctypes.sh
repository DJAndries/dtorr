#!/bin/sh
ctypesgen -I ../dtorr/include -L ../dtorr/lib -llibdtorr.so ../dtorr/include/dtorr/*.h -o dlib.py
