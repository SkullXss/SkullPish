# SkullPish.py

## Descrição
O SkullPish é um script Python que utiliza o framework Flask para criar um servidor web que tem a capacidade de mascarar um link do Ngrok, exibindo um formulário falso de login de redes sociais para os usuários. Ele é utilizado para fins educacionais e de demonstração, com o objetivo de conscientizar sobre a importância da segurança cibernética.

## Funcionalidades
- Gera um link disfarçado do Ngrok.
- Exibe um formulário falso de login de redes sociais.
- Captura e salva informações inseridas no formulário.
- Obtém o IP do usuário e informações de localização (latitude e longitude) usando o IP.

## Requisitos
- Flask==2.0.2
- requests==2.26.0
- Werkzeug==2.0.2

## Uso
1. Certifique-se de instalar as dependências listadas no arquivo `requirements.txt`.
2. Execute o script SkullPish.py para iniciar o servidor.
3. Acesse o servidor usando o link do Ngrok gerado.
4. Os usuários verão o formulário de login falso.
5. As informações inseridas serão capturadas e salvas em arquivos de texto com o nome do usuário.

## Página Inicial
O servidor Flask possui uma rota inicial que exibe o formulário de login falso. O arquivo HTML desse formulário está localizado em `templates/index.html`.

## Rotas
- `/`: Rota inicial para exibir o formulário falso.
- `/get_location`: Rota para obter o IP do usuário.
- `/submit_info`: Rota para submissão do formulário e captura de informações.

## Importante
Este script é estritamente para fins educacionais e de conscientização em segurança cibernética. Não é destinado a ser usado para fins maliciosos ou ilegais. Use com responsabilidade.

## Créditos
Desenvolvido por [SkullDev](https://github.com/SkullXss).

## Licença
Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

[Link para o repositório no GitHub](https://github.com/SkullXss/SkullPish/)
