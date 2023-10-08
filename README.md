# Flask-API

This repository aims to share the Rest API developed by using the Flask Python framework.
The API serves the purpose of allowing the user to retrieve data from the `data_crop.sql` file as well as
the `ibge_municipios.json` file. These two files can be found in the `dataset` folder.

We have decided to use the `docker` and `docker compose` to deploy the API. In order to deploy the API on a docker container,
make sure you have these two tools installed on your machine. Please, refer to the official [Docker Pages](https://docs.docker.com/compose/install/).

In order to deploy and use the API, you will need to do the following steps. We are assuming that you have the necessary tools installed,
i.e. `docker` and `docker compose`

## Setting The Environment Up

First of all, you will need to clone this repository. Once you have made that, you will need to reach the root of the
repository:

```
cd flask_api
```

After that, you will need to run some `docker` commands:

```
docker compose up -d flask_db
docker compose build
docker compose up -d flask_api
```

Make sure that all containers were initialized in the correct way.

```
docker ps
```

Finally, you can use the API. To do that, you will need to inform the following URL in your browser:

```
http://localhost:4000/test
```

This is a test URL. If you have set up the environment correctly, the following message will appear in your browser:

```
message	"test route"
```

## Routes

### To filter by cod_variavel

```
http://localhost:4000/cod_variavel/{id}
```

### To filter by cod_produto_lavouras_temporarias

```
http://localhost:4000/cod_produto_lavouras_temporarias/{id}
```

### To filter by cod_ano

```
http://localhost:4000/cod_ano/{id}
```

### To filter by cod_municipio

```
http://localhost:4000/cod_municipio/{id}
```
