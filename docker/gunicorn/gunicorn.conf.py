import os
import multiprocessing

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
_VAR = os.path.join(_ROOT, 'var')
_ETC = os.path.join(_ROOT, 'etc')

bind = '0.0.0.0:5000'
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = 'info'
accesslog = '/dev/app_stdout'
errorlog = '/dev/app_stderr'
timeout = 3 * 60
keepalive = 24 * 60 * 60  # 1 day
capture_output = True
proc_name = 'movidesk-to-trello'
default_proc_name = proc_name
