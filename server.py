#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:will
@file: server.py
@time: 2018/08/01
"""

from flask import Flask, make_response, render_template, redirect, url_for, request,flash,session
from flask_wtf.csrf import CSRFProtect, generate_csrf

app = Flask(__name__)
app.config['SECRET_KEY'] = '454615s4d51a6s5d4f5s1ad6f54s5d1f3a1sdf'
CSRFProtect(app)


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        if username == '123' and pwd == '123':
            print(username, pwd)
            result = make_response(redirect(url_for('transfer')))
            result.set_cookie('username', username)
            return result
        else:
            flash('用户名或密码错误')
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/transfer', methods=['POST', 'GET'])
def transfer():
    cookie_name = request.cookies.get('username', None)
    if not cookie_name:
        return redirect(url_for('login'))
    if request.method == 'POST':
        account = request.form.get('account')
        money = request.form.get('money')
        form_token = request.form.get('csrf_token')
        cookie_token = request.cookies.get('csrf_token')
        if form_token == cookie_token:
            return '转账%s到账户：%s' % (money, account)
        else:
            return '非法转账'
    csrf_token = generate_csrf()
    result = make_response(render_template('transfer.html', csrf_token=csrf_token))
    result.set_cookie('csrf_token', csrf_token)
    return result


if __name__ == "__main__":
    app.run(debug=True)

