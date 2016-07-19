import json
import threading

from app import flask_app
from app.battle_field import Battlefield
from app.log_saver import LogSaver
from flask import render_template, request, redirect


@flask_app.route('/')
@flask_app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@flask_app.route('/battle', methods=['GET', 'POST'])
def battle():
    if not request.form['num_armies'].isdigit() or int(request.form['num_armies']) == 0:
        return redirect('/')
    num_armies = int(request.form['num_armies'])
    Bf = Battlefield(num_armies)
    t = threading.Thread(target=Bf.start)
    t.start()
    return render_template("battle.html")


@flask_app.route('/log', methods=['GET'])
def log():
    return json.dumps(LogSaver.get_log())


