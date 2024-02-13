from flask import Flask, request

app = Flask(__name__)

@app.route('/clientes/<id>/transacoes', methods=['POST'])
def post_user_transaction():
    pass

@app.route('/clientes/<id>/extrato', methods=['GET'])
def get_user_transactions():
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

