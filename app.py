from flask import Flask, jsonify
import csv

app = Flask(__name__)

def leer_csv():
    productos = {}
    with open('productos.csv', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            sku = fila['sku']
            productos[sku] = {
                'precio': float(fila['precio']),
                'existencia': int(fila['existencia'])
            }
    return productos

@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    return jsonify(leer_csv())

if __name__ == '__main__':
    app.run()
