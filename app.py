from flask import Flask, redirect, request, render_template
app = Flask(__name__)

@app.route('/<name>')
def index(name):
    if name == 'Ousman':
        return 'Salam %s'%name
    return 'hello salam alaikum edi mubarak just %s' %name

if __name__ == '__main__':
    app.debug = True
    app.run()
