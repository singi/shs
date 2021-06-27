#!/usr/bin/python3

from flask import Flask, render_template, send_from_directory
import ssl

app = Flask(__name__, template_folder='.')

@app.after_request
def set_response_headers(resp):
    resp.headers['Cache-Control'] = "no-cache"
    resp.headers['Pragma'] = "no-cache"
    resp.headers['Expires'] = '0'
    return resp

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/poc")
def poc():
    return render_template('poc.html')

@app.route("/test.js")
def test():
    return send_from_directory('.', 'test.js')

if __name__ == '__main__':
    sslctx = ssl.SSLContext(ssl.PROTOCOL_TLS)
    sslctx.load_cert_chain(certfile="server.pem")
    app.run(host="0.0.0.0", port=8728, ssl_context=sslctx)
