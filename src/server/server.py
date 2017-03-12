from flask import Flask, request, render_template_string, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    print 'home'
    return render_template_string("<body>Yo!!!</body>")

@app.route('/read_url')
def read_url():
    url = request.args.get('url')
    return render_template_string('You sent us this <a href="{}">link</a>'.format(url))


if __name__ == '__main__':
    # print "password is: bubblepopper"
    # http://www.akadia.com/services/ssh_test_certificate.html
    # passphrase: bubblepopper
    context = ('./certs/server.crt', './certs/server.key')
    app.run(host="localhost", port=5000, debug=True, threaded=False, ssl_context=context)
