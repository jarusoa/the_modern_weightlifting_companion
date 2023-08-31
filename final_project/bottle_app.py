
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, post, get, template, request, static_file

@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/bmi')
def bmiForm():
    return template("bmi.html")
@post('/convert')

def bmiConvert():
    return template("result.html")
@route('/the_modern_lifting_companion')
def liftingHome():
    return template("the_modernlifting_companion.html")
@route('/companion')
def liftingCompanion():
    return template("companion.html")
@post('/companionresult')
def liftingCompanionResult():
    return template("companion_result.html")


application = default_app()

