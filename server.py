from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ O servidor está rodando! Acesse /roteiro para baixar o roteiro."

@app.route('/roteiro')
def get_roteiro():
    roteiro_path = "roteiro.txt"
    if os.path.exists(roteiro_path):
        return send_file(roteiro_path, as_attachment=True)
    else:
        return "🚫 Nenhum roteiro foi gerado ainda.", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
