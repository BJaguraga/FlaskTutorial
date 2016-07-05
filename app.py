from flask import Flask, redirect, request, render_template
app = Flask(__name__)

''' adding support for int and float '''


@app.route('/<int:name>')
def index(name):
    if name == 10:
        return 'Salam welcome . Your lucky number is  %s'%name
    return 'hello salam alaikum  %s' %name


@app.route('/<float:post_id>')
def float_num(post_id):
    return 'Float is {}'.format(post_id)


if __name__ == '__main__':
    app.debug = True
    app.run()
