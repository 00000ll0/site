from flask import Flask, render_template, request, redirect, make_response, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users_req(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(11), nullable=False)

    def __repr__(self):
        return f'Имя: {self.username}'


class Users_base(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.Integer, nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == "POST":
        username = request.form['username']
        phone = request.form['phone']

        user = Users_req(username=username, phone=phone)

        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')

        except:

            return "Oh"
    else:
        return render_template('form.html')


@app.route('/photos')
def photos():
    return render_template('photos.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route("/register", methods=["POST", "GET"])
def register():
    return render_template('register.html')


@app.route('/users_req')
def users_req():
    user = Users_req.query.order_by(Users_req.username).all()
    return render_template('users_req.html', usr=user)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)