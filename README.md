Meli-proxy:
===========

Proxy para la api de mercado libre, el cual permite controlar y medir las solicitudes a el dominio api.mercadolibre.com.
Ademas limita las ip que tienen acceso a la api y la cantidad de solicitudes realizadas por estas.

# Usage

Debe tener instalado docker y docker-compose.

### Run

```sh
docker-compose up
```

Esto desplegara 4 contenedores que proveen dos servicios:

- **Proxy:** El cual enruta las solicitudades a la api de mercado libre, y controlada la cantidad de request. 
Implementado con Flask y MongoDB. http://localhost:8080

- **Monitorieo:** El cual recupera las metricas de el proxy las almacena y muestra.
Implementado con Prometheus y Grafana. http://localhost:3000


La siguiente imagen es el diagrama de esta solucion pero con capacidad
de escalamiento, para asi poder atender 50.000 request/segundo 

![Diagram](./docs/meli-proxy-diagram.jpeg?raw=true)



