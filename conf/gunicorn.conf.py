bind = "0.0.0.0:8000"
pid = "/tmp/project-master.pid"
workers = 1
timeout = 60
max_requests = 500
accesslog = '-'  # log to stdout
errorlog = '-'  # log to stderr
limit_request_line = 4094
