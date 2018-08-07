#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:will
@file: csrf.py
@time: 2018/08/01
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login1.html')


if __name__ == "__main__":
    app.run(port=8080)
