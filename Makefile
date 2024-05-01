CURRENT_DIR := $(shell pwd)
EMQX_CONF := $(CURRENT_DIR)/emqx.conf

run-broker:
	docker run --rm -d --name emqx \
		-p 1883:1883 -p 8083:8083 \
		-p 8084:8084 -p 8883:8883 \
		-p 18083:18083 \
		-p 14567:14567/udp \
		-e EMQX_LISTENERS__QUIC__DEFAULT__keyfile="etc/certs/key.pem" \
		-e EMQX_LISTENERS__QUIC__DEFAULT__certfile="etc/certs/cert.pem" \
		-e EMQX_LISTENERS__QUIC__DEFAULT__ENABLED=true \
		emqx/emqx:5.6.1
# -v $(EMQX_CONF):/etc/emqx.conf \

stop-broker:
	docker stop emqx || true
	docker rm emqx || true

restart-broker: stop-broker run-broker

build-python-client-docker-image:
	docker build -t local/python-mqtt-client -f python/Dockerfile python/

run-python-client:
	docker run --rm -it --name python-mqtt-client local/python-mqtt-client

check-config:
	docker exec emqx bash -c "emqx ctl listeners"

run-compose:
	docker-compose up -d

stop-compose:
	docker-compose down

clean-install-pynng-mqtt:
	rm -rf pynng-mqtt/mbedtls/build/
	rm -rf pynng-mqtt/nng/build/
	cd pynng-mqtt && pip3 install --user asyncio && pip3 install -e .
