gunicorn -D \
--access-logfile access.log \
--error-logfile error.log \
--pid process.pid \
--bind 0.0.0.0:35000 \
wsgi:app

