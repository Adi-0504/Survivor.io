from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/init_level')
def init_level():
    # 隨機生成 5 隻蝙蝠
    enemies = []
    for _ in range(5):
        enemies.append({
            "id": random.randint(1000, 9999),
            "x": random.randint(100, 700),
            "y": random.randint(100, 400),
            "hp": 50,
            "speed": random.uniform(1.0, 2.0)
        })
    
    # 隨機生成 3 個水晶
    crystals = []
    for _ in range(3):
        crystals.append({
            "id": random.randint(1000, 9999),
            "x": random.randint(200, 600),
            "y": random.randint(200, 400),
            "hp": 100,
            "max_hp": 100
        })

    return jsonify({"enemies": enemies, "crystals": crystals})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
