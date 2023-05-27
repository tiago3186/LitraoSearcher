from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)

app.secret_key = '87144798'

# Configuração do caminho para a pasta "templates"
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
app.template_folder = template_dir

# Estrutura de dados temporária para armazenar pares de login e senha
users = {
    'admin': 'admin'
}

@app.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verifica se o par login/senha existe na estrutura de dados
        if username in users and users[username] == password:
            session['username'] = username  # Armazena o nome de usuário na sessão
            return redirect(url_for('index'))  # Redireciona para a rota '/index/' usando o método GET

    # Renderiza a página de login se o login falhar ou se for uma solicitação GET
    return render_template('index.html', username=session.get('username'))

@app.route('/')
def home():
    # Verifica se o usuário está logado
    if 'username' in session:
        return redirect(url_for('index'))  # Redireciona para a rota '/index/' se estiver logado

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verifica se o par login/senha existe na estrutura de dados
        if username in users and users[username] == password:
            session['username'] = username  # Armazena o nome de usuário na sessão
            return redirect(url_for('index'))  # Redireciona para a rota '/index/' se o login for bem-sucedido

    return render_template('login.html')  # Renderiza a página de login se ainda não estiver logado

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)  # Remove o nome de usuário da sessão
    return redirect(url_for('home'))  # Redireciona para a rota '/' (página de login)

if __name__ == '__main__':
    app.run()