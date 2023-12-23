from flask import Flask, jsonify, request, render_template
import socket

app = Flask(__name__)

def fetchDetails():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return str(hostname), str(ip)

@app.route("/")
def root():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return jsonify(
            status="logged in"
        )
    else:
        return jsonify(
            status="login"
        )

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    hostname, ip = fetchDetails()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
