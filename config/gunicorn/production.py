"""Gunicorn *production* config file"""

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "book_swap.wsgi:application"
# The granularity of Error log outputs
loglevel = "info"
# The number of worker processes for handling requests
workers = 2
# The socket to bind
bind = "127.0.0.1:8000"
# Restart workers when code changes (development only!)
reload = False
# Write access and error info to /var/log
accesslog = errorlog = "/var/log/gunicorn/dev.log"
# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
pidfile = "/var/run/gunicorn/dev.pid"
# Daemonize the Gunicorn process (detach & enter background)
daemon = True
