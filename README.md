# VizFaDa

VizFaDa, for visualisation of FAANG data, aims at adding data visualisations to the [FAANG data portal](https://data.faang.org).

## Requirements

* Docker version > 19.03

## Run locally with Docker

To start the application:
```bash
docker run -dp 8080:8080 lauramble/vizfada-django-test
docker run -dp 4200:4200 lauramble/vizfada-ng-test
```

You can access the back-end and the front-end separately on your browser through your local host (127.0.0.1) :

* Front-end : [127.0.0.1:4200](http://127.0.0.1:4200) or [localhost:4200](http://localhost:4200/)
* Back-end : [127.0.0.1:8080](http://127.0.0.1:8080) or [localhost:8080](http://localhost:8080/)

To stop the application, first get container id using `docker ps`, then:

```bash
docker stop <ID>
```
