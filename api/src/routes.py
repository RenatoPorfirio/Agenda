from flask import Flask, request, make_response
from controllers import Controller

app = Flask(__name__)
controller = Controller()

@app.route('/', methods=['GET'])
def root():
    return controller.root()

@app.route('/registro', methods=['GET','POST'])
def registro():
    return controller.registro(request)

@app.route('/tarefas', methods=['GET'])
def tarefas():
    return controller.tarefas()

@app.route('/view', methods=['GET'])
def view():
    return controller.view(request)