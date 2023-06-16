from flask import Flask,render_template
from flask import send_from_directory, send_file

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

@app.route('/download')
def download():
    return send_file('./data/代码.txt',
                )


if __name__ == '__main__':
    app.run()