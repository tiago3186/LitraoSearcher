from flask import Flask, render_template, request, redirect, url_for, session
from models.models import db, User, Pub

app = Flask(__name__)

app.secret_key = '87144798'

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Quadrado86?@localhost/litraosearcher'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialize o objeto SQLAlchemy com o aplicativo Flask
db.init_app(app)

@app.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Consulta o banco de dados para verificar se o usuário existe e a senha está correta
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['username'] = username  # Armazena o nome de usuário na sessão
            return redirect(url_for('index'))  # Redireciona para a rota '/index/' usando o método GET
        else:
            error_message = "Usuário e/ou senha inválidos."
            return render_template('login.html', error_message=error_message)

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

        # Consulta o banco de dados para verificar se o usuário existe e a senha está correta
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['username'] = username  # Armazena o nome de usuário na sessão
            return redirect(url_for('index'))  # Redireciona para a rota '/index/' se o login for bem-sucedido

    return render_template('login.html')  # Renderiza a página de login se ainda não estiver logado

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)  # Remove o nome de usuário da sessão
    return redirect(url_for('home'))  # Redireciona para a rota '/' (página de login)

if __name__ == '__main__':
    app.run()