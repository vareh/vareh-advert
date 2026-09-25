from flask import Flask

app = Flask(__name__)
app.config['secret_key'] = 'vareh203'
@app.route('/')
def hello_world():  # put application's code here
    return 'hello world'


if __name__ == '__main__':
    app.run()
