## Intro
A sample app that send a counter that increments for a while, then stops incrementing, then removes metric from registry.

The purpose of this app is to test what happens in this situation, how it looks in storage and how functions works over such data.

## Prepare
1. `pip install prometheus_client`
2. (If not running on mac: fix hostname in prometheus.yml)

## Run
1. `python3 nulls_for_zeroes.py`
2. ```
    docker run \
    -it \
    --rm \
    --name prom \
    -p 9090:9090 \
    -v `pwd`/prometheus.yml:/etc/prometheus/prometheus.yml \
    prom/prometheus
   ```
3. Check what is fetched: `while true; do date; curl -s localhost:8000 | grep lbl | grep total; sleep 5; done;`
