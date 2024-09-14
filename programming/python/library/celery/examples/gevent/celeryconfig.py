import os
import sys

sys.path.insert(0, os.getcwd())

# ## Note: Start worker with -P gevent,
# do not use the worker_pool option.
broker_url='redis://localhost:6379/0',
result_backend='redis://localhost:6379/0'
#broker_url = 'amqp://guest:guest@localhost:5672//'
#result_backend = 'amqp'
result_expires = 30 * 60

imports = ('tasks',)
