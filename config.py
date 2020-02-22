import dlib

dtorr_config = dlib.dtorr_config(log_level=4, log_handler=dlib.CFUNCTYPE(dlib.UNCHECKED(None), dlib.c_int, dlib.String)(0))
