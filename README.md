Meli-proxy:
===========

Proxy for mercadolibre API, it allows controlling and measuring requests to the domain api.mercadolibre.com. Also it
limits the IPs that have access to the api and the number of requests made by them.

# Usage

You must install docker and docker-compose

### Run

```sh
docker-compose up
```

This run four container and these provide two services:

- **Proxy:**  This in charges of routes requests to mercadolibre API and control max quantity to requests.
It was built with Flask and MongoDB. http://localhost:8080

    It can see the management endpoints [here](https://app.swaggerhub.com/apis/maitaoriana/meli-proxy/1.0.0).


- **Monitorieo:** This service gets metrics from proxy then it stores and shows them. It was built with
Prometheus and Grafana. http://localhost:3000

The next image is a diagram of this solution with ability of autoscaling.

![Diagram](./docs/meli-proxy-diagram.jpeg?raw=true)
