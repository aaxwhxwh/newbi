from flask import Flask, redirect, render_template, session,request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect, generate_csrf

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'sshieslppgsdfnenixlsdj13j355235j2kjkjklp'
CSRFProtect(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    user = db.relationship('User', backref='role')

    def __repr__(self):
        return 'Role id:%s, name:%s' % (self.id, self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'Role id:%s, name:%s, email:%s, password:%s' % (self.id, self.name, self.email, self.password)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    csrf_token = generate_csrf()
    response = render_template('index.html', csrf_token=csrf_token)
    response.set_cookie()
    return render_template('index.html', csrf_token=csrf_token)


@app.route('/user')
def user():
    return '%s，欢迎登陆个人邮箱' % session['name']


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()
    ro2 = Role(name='user')
    db.session.add(ro2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
    us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
    us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
    us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
    us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
    us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
    db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    db.session.commit()
    app.run(debug=True)

"""
查询所有用户数据
查询有多少个用户
查询第1个用户
查询id为4的用户[3种方式]
查询名字结尾字符为g的所有数据[开始/包含]
查询名字不等于wang的所有数据[2种方式]
查询名字和邮箱都以 li 开头的所有数据[2种方式]
查询password是 `123456` 或者 `email` 以 `itheima.com` 结尾的所有数据
查询id为 [1, 3, 5, 7, 9] 的用户列表
查询name为liu的角色数据
查询所有用户数据，并以邮箱排序
每页3个，查询第2页的数据
"""