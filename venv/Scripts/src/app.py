from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)
# rota para a página inicial
@app.route('/')
def index():
    return render_template('index1.html')

# Função para conectar ao banco de dados
def connect_db():
    conn = sqlite3.connect('robot.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rota para retornar a posição atual do robô
@app.route('/robot/position', methods=['GET'])
def get_robot_position():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM robot ORDER BY id DESC LIMIT 1')

    row = cursor.fetchone()
    if row is None:
        return jsonify({'message': 'Position not found'}), 404
    else:
        return jsonify({'positionX': row['positionX'], 'positionY': row['positionY'], 'positionZ': row['positionZ'], 'rotation': row['rotation']}), 200

# Rota para atualizar a posição do robô
@app.route('/robot/position', methods=['PUT'])
def update_robot_position():
    conn = connect_db()
    cursor = conn.cursor()
    data = request.json
    positionX = data.get('positionX')
    positionY = data.get('positionY')
    positionZ = data.get('positionZ')
    rotation = data.get('rotation')
    if positionX and positionY and positionZ and rotation is None:
        return jsonify({'message': 'Position not provided'}), 400
    cursor.execute('INSERT INTO robot (positionX, positionY, positionZ, rotation) VALUES (?,?,?,?)', (positionX,positionY,positionZ,rotation))
    # cursor.execute('INSERT INTO robot (positionY) VALUES (?)', (positionY))
    # cursor.execute('INSERT INTO robot (positionZ) VALUES (?)', (positionZ))
    conn.commit()
    return jsonify({'message': 'Positions updated successfully'}), 200

# Rota para retornar o histórico de deslocamentos do robô
@app.route('/robot/history', methods=['GET'])
def get_robot_history():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM robot')
    rows = cursor.fetchall()
    if len(rows) == 0:
        return jsonify({'message': 'History not found'}), 404
    else:
        history = [{'id': row['id'], 'positionX': row['positionX'], 'positionY': row['positionY'], 'positionZ': row['positionZ'], 'rotation':row['rotation']} for row in rows]
        return jsonify({'history': history}), 200
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
