from flask import Flask, render_template, request
import ssl

app = Flask(__name__)

@app.route('/hello')
def index():
    #return "Hello Everon Laboratory"
    return render_template('test01.html')

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port="443", ssl_context='adhoc')


from flask import Flask, render_template, request
import ssl

app = Flask(__name__)

@app.route('/hello')
def index():
    #return "Hello Everon Laboratory"
    return render_template('test01.html')

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    app.debug = True

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(certfile='cert.pem', keyfile='key.pem', password='louie')
    app.run(host="0.0.0.0", port=443, ssl_context=ssl_context)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(ssl_context='adhoc')

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))


from flask import Flask
import ssl

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

if __name__ == "__main__":
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(certfile='newcert.pem', keyfile='newkey.pem', password='secret')
    app.run(host="0.0.0.0", port=443, ssl_context=ssl_context)



@app.before_request
def before_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)
    
from flask import Flask
 
app = Flask(__name__)
 
 
@app.route('/')
def hello():
    return '<h1>This is HTTP site</h1>'
 
if __name__ == '__main__':
    app.run('0.0.0.0', 9999, debug=True)


from flask import Flask
import eventlet
import eventlet.wsgi
 
app = Flask(__name__)
 
 
@app.route('/')
def hello():
    return '<h1>This is HTTPS site</h1>'
 
if __name__ == '__main__':
    server = eventlet.wrap_ssl(eventlet.listen(('0.0.0.0', 9999)), certfile='secrets/cert.pem', keyfile='secrets/key.pem', server_side=True)
    eventlet.wsgi.server(server, app)
