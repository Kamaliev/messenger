import sqlite3

from flask import Flask, request, jsonify
from database import Events, Students

app = Flask(__name__)

event = Events()
user = Students()


@app.route('/get', methods=['GET'])
def get_message():
    data = request.json
    last_id = data['id']
    login = data['login']
    user.update_online(login)
    return jsonify({'data': event.get(id=last_id), 'online': user.get_online()})


@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    text = data.get('message')
    login = data.get('login')
    event.add(login, text)
    return jsonify({'status': True})


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    login = data.get('login', '')
    password = data.get('password', '')
    found = user.check(login, password)
    username = user.get_username(login)
    return jsonify({'login': found, 'username': username})


@app.route('/check_login', methods=['POST'])
def check_login():
    data = request.json
    login = data.get('login', '')
    found = user.check_login(login)
    return jsonify({'login': found})


@app.route('/registrate', methods=['POST'])
def registrate():
    data = request.json
    credits = data.get('data', '')
    try:
        user.add(*credits)
    except sqlite3.Error as e:
        return jsonify({'error': e})
    else:
        return jsonify({'status': True})


@app.route('/delete', methods=['POST'])
def drop_table():
    data = request.json
    secret = data.get('secret', '')
    try:
        user.add(*credits)
    except sqlite3.Error as e:
        return jsonify({'error': e})
    else:
        return jsonify({'status': True})


if __name__ == '__main__':
    app.run()
