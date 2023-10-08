from flask import Flask, jsonify, make_response
import psycopg2
import pandas as pd
from json import loads

app = Flask(__name__)

database_kwargs = {
    "database": "postgres",
    "host": "flask_db",
    "user": "postgres",
    "password": "postgres",
    "port": "5432"
}

with open("dataset/crop_data.sql", "r", encoding="utf8") as sql_file:
    sql_script = sql_file.read()

connection = psycopg2.connect(**database_kwargs)
cursor = connection.cursor()
cursor.execute(sql_script)

# connection.commit()

data = pd.read_sql_query("SELECT * FROM crop.crop_data", connection)

connection.close()

cities = pd.read_json("dataset/ibge_municipios.json", encoding="utf8")
cities = cities.drop_duplicates(subset=["ibge_code"], inplace=False)
cities["municipio"] = cities["municipio"].str.upper()

data = data.merge(cities, how="outer", left_on='cod_municipio', right_on='ibge_code')
data = data.dropna(subset=["cod_municipio"], inplace=False)

def fix_municipio(row):
    if row["ibge_code"] == 0:
        return "MUNICIPIO DESCONHECIDO"
    else:
        return row["municipio"]

data["ibge_code"] = data["ibge_code"].fillna(0)
data["municipio"] = data.apply(fix_municipio, axis=1)
data = data.drop(columns=["ibge_code"], inplace=False, axis=1)

#create a test route
@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'test route'}), 200)

@app.route('/cod_variavel/<int:id>', methods=['GET'])
def get_data_by_cod_variavel(id):
  try:
    filtered_data = data.query(f"cod_variavel == {id}", inplace=False)
    result = filtered_data.to_json(orient="index")
    parsed = loads(result)
    return make_response(jsonify(parsed) , 200)
  except:
    return make_response(jsonify({'message': 'error getting users'}), 500)

@app.route('/cod_produto_lavouras_temporarias/<int:id>', methods=['GET'])
def get_data_by_cod_produto_lavouras_temporarias(id):
  try:
    filtered_data = data.query(f"cod_produto_lavouras_temporarias == {id}", inplace=False)
    result = filtered_data.to_json(orient="index")
    parsed = loads(result)
    return make_response(jsonify(parsed) , 200)
  except:
    return make_response(jsonify({'message': 'error getting users'}), 500)

@app.route('/cod_ano/<int:id>', methods=['GET'])
def get_data_by_cod_ano(id):
  try:
    filtered_data = data.query(f"cod_ano == {id}", inplace=False)
    result = filtered_data.to_json(orient="index")
    parsed = loads(result)
    return make_response(jsonify(parsed) , 200)
  except:
    return make_response(jsonify({'message': 'error getting users'}), 500)

@app.route('/cod_municipio/<int:id>', methods=['GET'])
def get_data_by_cod_municipio(id):
  try:
    filtered_data = data.query(f"cod_municipio == {id}", inplace=False)
    result = filtered_data.to_json(orient="index")
    parsed = loads(result)
    return make_response(jsonify(parsed) , 200)
  except:
    return make_response(jsonify({'message': 'error getting users'}), 500)