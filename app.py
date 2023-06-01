from flask import Flask, render_template, request, redirect, url_for, session, jsonify, __version__
from models.models import db, User, Pub
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
print(__version__)

app.secret_key = os.getenv('app_secret_key')

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('username')}:{os.getenv('password')}@{os.getenv('hostname')}/litraosearcher?sslmode=require"
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

    # Recupera todos os marcadores da tabela "pub"
    markers = Pub.query.all()

    # Renderiza a página de index.html passando os marcadores como uma variável
    return render_template('index.html', username=session.get('username'), markers=markers)

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

@app.route('/add_pub', methods=['POST'])
def add_pub():
    if 'username' not in session:
        return redirect(url_for('home'))  # Redireciona se o usuário não estiver logado

    # Obtém os dados do formulário
    pubname = request.form['pubname']
    description = request.form['description']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    user = session['username']

    # Cria um novo objeto Pub
    pub = Pub(pubname=pubname, description=description, latitude=latitude, longitude=longitude, user=user)

    # Adiciona o objeto Pub ao banco de dados
    db.session.add(pub)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/get_markers', methods=['GET'])
def get_markers():
    markers = Pub.query.all()
    marker_list = []

    for marker in markers:
        marker_data = {
            'pubname': marker.pubname,
            'description': marker.description,
            'latitude': marker.latitude,
            'longitude': marker.longitude,
            'user': marker.user
        }
        marker_list.append(marker_data)

    return jsonify(marker_list)

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)  # Remove o nome de usuário da sessão
    return redirect(url_for('home'))  # Redireciona para a rota '/' (página de login)

if __name__ == '__main__':
    app.run()