from flask import Flask, redirect, request, render_template, url_for


''' adding support for int and float '''

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/success/<name>')
def success(name):
    file = open('test.txt', 'a+')
    file.write(name)
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.debug = True
    app.run()
