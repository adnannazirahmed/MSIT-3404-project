from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from Flask backend!</h1><p><a href="/image">See image</a></p>'

@app.route('/image')
def image():
    return send_from_directory('static', 'sample.jpg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
