from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_folder='Client', static_url_path='/static')

@app.route('/')
def index():
    return send_from_directory('Client', 'app.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('Client', path)

if __name__ == '__main__':
    app.run(debug=True)
