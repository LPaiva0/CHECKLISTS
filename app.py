from flask import Flask, session
import os
from checklist_web_routes import checklist_web_bp
from secrets import token_hex

app = Flask(__name__)

# Chave secreta necessária para usar o 'session' e 'flash'
app.secret_key = token_hex(16)

# Registra o seu Blueprint (seu script de rotas)
app.register_blueprint(checklist_web_bp)

# Rota principal para não dar erro ao abrir o endereço base
@app.route('/')
def home():
    # Simula um login automático para o portfólio funcionar de cara
    session['user_id'] = 1
    session['user_nome'] = "Recrutador Demo"
    return "<h1>Sistema de Checklist Rodando!</h1><p>Acesse <a href='/checklist/dashboard'>/checklist/dashboard</a></p>"

if __name__ == '__main__':
    # Roda o servidor local na porta 5000
    print("Sistema iniciado! Acesse: http://127.0.0.1:5000")
    app.run(debug=True)