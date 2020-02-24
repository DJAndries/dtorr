import dlib
import log

dtorr_config = dlib.dtorr_config(log_level=3, log_handler=dlib.CFUNCTYPE(dlib.UNCHECKED(None), dlib.c_int, dlib.String)(log.handle_log))
