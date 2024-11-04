# fintual-test
Prueba tecnica para Fintual

## Requerimientos Docker.

- Make 3.81
- Docker version 24.0.2

### Pasos a seguir.

1. ejecutar el siguiente comando para generar la base de datos (sqlite)
```bash
make db-regen
```

2. ejecutar el siguiente comando para construir el contenedor.
```bash
make build
```
3. ejecutar el siguiente comando para que el contenedor se inicie.
```bash
make run
```

## Requerimientos correr directo.

- Python 3.12.5 
- Make 3.81

### Pasos a seguir.

1. validar las versiones minimas requeridas
2. ejecutar el siguiente comando para generar el enviroment
```bash
make env
```
3. ejecutar el siguiente comando para generar la base de datos (sqlite)
```bash
make db-regen
```

4. ejecutar el siguiente comando para iniciar el servidor
```bash
make server
```

## Modelo de datos
![image](https://github.com/worker-8/fintual-test/blob/main/image.png?raw=true)
para lograr el objetivo de la prueba se genero el siguiente modelo de datos
*PD: en la tabla task se añade el campo is_assignment*

## Observaciones

- los datos utilizados provienen de `alphavantage`, dado a que utilice una cuanta demo, la api key presente en `feed_db.py` puede presentar problemas, solo se puede obtener a IBM de forma consistente, la base de datos ya viene incorpada en el proyecto en caso de falla la conexion al proveedor.

- en el caso de `annualized_return` no supe como hacerlos asi que preferi no aventurarme.


## Endpoints.

### find all portfolios

Lista todos los portfolio con sus stocks

```bash
curl --request GET \
  --url http://localhost:5000/api/v1/portfolio \
  --header 'User-Agent: insomnia/10.1.1'
```

### get profit

Obtiene profit segun portfolio y fechas.

```bash
curl --request GET \
  --url 'http://localhost:5000/api/v1/portfolio/{portfolio_name}/profit?initial={YYYY-MM-DD}&end={YYYY-MM-DD}' \
  --header 'User-Agent: insomnia/10.1.1'
```

