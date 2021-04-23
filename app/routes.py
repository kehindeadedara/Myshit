from app import app
from flask import render_template
from app.forms import LoginForm
from flask import Flask, jsonify, request, redirect, session, url_for
from app.config import Config
from pymongo import MongoClient
import bcrypt

client = MongoClient(Config.MONGO_URI)
database = client.get_database('GPASWE')
records = database.GPA


@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET','POST'])
def register():
    message = ''
    if 'username' in session:
        return redirect(url_for('logged_in'))
    if request.method == 'POST':
        username = request.form.get('username')
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        password1 = request.form.get('password1')


        username_found = records.find_one({"username": username})

        if username_found:
            message = 'Username found! Try another username'
            return render_template('home.html')
        else:
            hashed = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
            user_input = {
                'username': username,
                'password': hashed,
                'firstname': first_name,
                'lastname': last_name
            }
            records.insert_one(user_input)

            user_data = records.find_one({"username": username})
            user = user_data['username']

            return render_template('logged_in.html', user = user)


    return render_template('register.html')

@app.route('/login', methods = ["POST", "GET"])
def login():
    if 'username' in session:
        return redirect(url_for('logged_in'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        # password = request.form.get('password')
        # print(username, password)

        username_found = records.find_one({'username' : username})
        print(username_found)

        if username_found:
            username_check = username_found['username']
            # password_check = username_found['password']

            # if bcrypt.checkpw(password.encode('utf-8'), password_check):
            #     session['username'] = username_check
            #     return redirect(url_for('logged_in'))
            # else:
            #     if 'username' in session:
            #         return redirect(url_for('logged_in'))
            #     message = 'wrong password'
                # return render_template('login.html')
            session['username'] = username_check
            return redirect(url_for('logged_in'))
    return render_template('login.html')


@app.route('/logged_in')
def logged_in():
    if "username" in session:
        user = session["username"]
        return render_template('logged_in.html', user = user)
    else:
        return redirect(url_for("login"))


@app.route('/logout')
def log_out():
    if 'username' in session:
        session.pop('username')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))










