from flask import Flask, render_template, request, redirect,session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event.db'
db = SQLAlchemy(app)
app.secret_key = "hello"  

class tblcontact(db.Model):
    c_id=db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.TEXT)
    last_name = db.Column(db.TEXT)
    email_id = db.Column(db.TEXT)
    phone_no = db.Column(db.TEXT)
    event_date = db.Column(db.TEXT)
    def __repr__(self):
       return f"tblcontact('{self.first_name}', '{self.last_name}', '{self.email_id}',{self.phone_no}',{self.event_date}')"


@app.route("/",methods=["POST","GET"])
def index():
    return render_template('index.html')

@app.route("/contact",methods=["POST","GET"])
def contact():
     message=""
     if request.form:
          first_name=request.form.get("txtfname")#Getting the values from html form 
          last_name=request.form.get("txtlname")
          email_id=request.form.get("txtemail")
          phone_no=request.form.get("txtphoneno")
          event_date=request.form.get("txteventdate")
          contact_us=tblcontact(first_name=first_name,last_name=last_name,email_id=email_id,phone_no=phone_no,event_date=event_date)
          db.session.add(contact_us)
          db.session.commit()
          message="Your Data Has been Submited!!Thanks For CONTACT US!"
     return render_template('Contact.html',message=message)

@app.route("/login",methods=["POST","GET"])
def login():
    mes=""
    if request.method=="POST":
        mes=""
        username=request.form.get('txtname')
        userpass=request.form.get('txtpass')
        if username=="admin" and userpass=="admin":
            session['admin']=username
            contact_us=tblcontact.query.all()
            return render_template('users.html',contactus=contact_us)
        else:
            mes="Wrong Details!!"
            return render_template('login.html',mes=mes)
    else:
        mes="Wrong Details!!"
        return render_template('login.html',mes=mes)

@app.route("/users",methods=["GET","POST"])
def view_contacts():
    contact_us=tblcontact.query.all()
    return render_template('users.html',contactus=contact_us)

@app.route("/update/<c_id>",methods=["GET"])
def edit(c_id):
    contact_us=tblcontact.query.filter_by(c_id=c_id).first()
    return render_template("update.html",contact_us=contact_us)

@app.route("/update",methods=["POST"])
def update():
    c_id=request.form.get("txtc_id")
    first_name=request.form.get("txtfname")#Getting the values from html form 
    last_name=request.form.get("txtlname")
    email_id=request.form.get("txtemail")
    phone_no=request.form.get("txtphoneno")
    event_date=request.form.get("txteventdate")
    
    contact_us=tblcontact.query.filter_by(c_id=c_id).first()
    
    contact_us.first_name=first_name
    contact_us.last_name=last_name
    contact_us.email_id=email_id
    contact_us.phone_no=phone_no
    contact_us.event_date=event_date
    db.session.commit()
    return redirect('/users')

@app.route("/delete",methods=["POST"])
def delete():
    c_id=request.form.get("c_id")
    
    contact_us=tblcontact.query.filter_by(c_id=c_id).first()
    db.session.delete(contact_us) 
    db.session.commit()
    return redirect('/users')

   
@app.route("/about",methods=["get","post"])
def about():
    return render_template('About.html')

@app.route("/birthday",methods=["get","post"])
def birthday():
    return render_template('birthday.html')

@app.route("/wedding",methods=['get'])
def wedding():
    return render_template('wedding.html')
    
@app.route("/exhibition",methods=['get'])
def exhibition():
    return render_template('exhibition.html')

@app.route("/award",methods=['get'])
def award():
    return render_template('award.html')

@app.route("/rock",methods=['get'])
def rock():
    return render_template('rock.html')

@app.route("/reception",methods=['get'])
def reception():
    return render_template('reception.html')

@app.route("/gallery",methods=['get'])
def gallery():
    return render_template('Gallery.html')

@app.route("/gallery2",methods=['get'])
def gallery2():
    return render_template('Gallery2.html')

if __name__ == '__main__':
    app.run(debug=True)


