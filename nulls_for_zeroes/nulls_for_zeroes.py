import prometheus_client as prom
from prometheus_client import start_http_server, Summary, Counter
import random
import time

reg = prom.CollectorRegistry()

c = Counter('test_counter', 'help', labelnames=['lbl'], registry=reg)
do_inc = True
removed = False

def process_request(t):
    global do_inc

    if do_inc:
        c.labels('test').inc()

    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000, registry=reg)
    start = time.time()
    # Generate some requests.
    while True:
        if time.time() - start > 60:
            do_inc = False

        if time.time() - start > 90 and reg.get_sample_value('test_counter_total', {'lbl': 'test'}):
            c.remove('test')

        process_request(random.random())