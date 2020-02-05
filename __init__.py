# -*- coding: utf-8 -*-

import logging
import warnings


__author__ = 'SmoothGlide'
__email__ = 'davemorrow@hotmail.com'
__version__ = '0.0.1'


# Set up logging to ``/dev/null`` like a library is supposed to.
# http://docs.python.org/3.3/howto/logging.html#configuring-logging-for-a-library
class NullHandler(logging.Handler):  # pragma: no cover
    def emit(self, record):
        pass


with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

logging.getLogger('ingot').addHandler(NullHandler())
