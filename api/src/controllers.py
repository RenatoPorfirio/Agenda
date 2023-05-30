from flask import render_template, request, jsonify
from datetime import datetime
import quicksort
import json

DATABASE_PATH = 'databases/database.json'

class Controller:
    def root(self):
        return render_template('index.html')
    
    def registro(self, request):
        if request.method == 'GET':
            return render_template('registro.html')
        else:
            content = dict(request.form)
            try:
                with open(DATABASE_PATH, 'r') as database_file:
                    database = json.load(database_file)
            except:
                database = {}

            date = content['data']
            now = str(datetime.now())
            
            try:
                database[date][now] = content
            except:
                database[date] = {}
                database[date][now] = content
                
            dates = []
            for date, _ in database.items():
                dates.append(date)
            quicksort.hoare(dates, 0, len(dates) - 1)

            ord_database = {}
            for date in dates:
                ord_database[date] = database[date]
            with open(DATABASE_PATH, 'w') as database_file:
                json.dump(ord_database, database_file, indent=4, ensure_ascii=False)
            return 'OK'
    
    def tarefas(self):
        with open('databases/database.json', 'r') as database:
            return database.read()
        
    def view(self, request):
        with open('databases/database.json', 'r') as db_file:
            database = json.load(db_file)
        date = request.args.get('date')
        task = request.args.get('task')
        obj = database[date][task]
        page = '<!DOCTYPE html><html><body><div><h1>'+obj['titulo']+'</h1><br><h2>'+obj['descricao']+'</h2></div></body></html>'
        return page