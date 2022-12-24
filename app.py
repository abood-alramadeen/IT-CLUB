from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contentData.db'
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False


db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    phone_number = db.Column(db.String(20), unique=True)
    comment = db.Column(db.Text, default='No comment')
    email = db.Column(db.String(500), unique=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    

    def __repr__(self):
        return f'<User {self.id}: {self.full_name}>'


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
    
        phone_number = request.form['phone']
        full_name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        userData = User(comment=message, phone_number=phone_number, email=email,full_name=full_name)

        try: 
            db.session.add(userData)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(e)
            return f"Error Occured ,{e}"
    else :
        return render_template('index.html')
    



if __name__ == "__main__":

    app.run(debug=True)


