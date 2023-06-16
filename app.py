from flask import Flask,render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def default_route():
    return render_template('homepage.html')


if __name__ == '__main__':
    app.run()