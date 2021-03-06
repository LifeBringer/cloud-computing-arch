from flask import Flask, request, jsonify
import random
app = Flask(__name__)

seed = random.randint(0, 100)

@app.route('/', methods = ['POST', 'GET'])
def resp():
    global seed
    if request.method == 'POST':
        seed = int(request.json.get('num'))
        print(f'POST: {seed}')
        return jsonify(success=True)
    else:
        print(f'GET: {seed}')
        return str(seed)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
