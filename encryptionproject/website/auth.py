from flask import Blueprint,request,render_template,flash,redirect,url_for
import string
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user
 

auth=Blueprint('auth',__name__)

@auth.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
         email=request.form.get('email')
         password=request.form.get('password')
         user=User.query.filter_by(email=email).first()
         if user:
              if check_password_hash(user.password,password):
                   flash('Logged in successfully!',category='valid')
                   login_user(user,remember=True)
                   
                   return redirect(url_for('views.home'))
              else:
                   flash('Incorrect password. Please try again',category='invalid')
         else:
              flash("There is no account associated with this email.",category='invalid')
    return render_template("login.html",user=current_user)
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/signup", methods=["POST", "GET"])
def signup():
   
   
   if request.method == "POST":
     email = request.form.get('email')
     username = request.form.get('username')
     password = request.form.get('password')
     password1 = request.form.get('password1')
     user=User.query.filter_by(email=email).first()
     user_username=User.query.filter_by(username=username).first()
     
     if user:
          flash('An account is already associated with this email.',category="invalid")
     
     elif user_username:
          flash('This username is not available. Please use a different username',category='invalid')
     elif len(email) < 4:
         flash("please enter a valid email.", category="invalid")
     elif len(username) < 3:
            flash("This username is too short. Please choose a longer username.", category="invalid")
     elif password != password1:
            flash("Your Password do not match.", category="invalid")
     elif len(password) < 8 or password == "" or not any(char.isdigit() for char in password) or not any( char in string.punctuation for char in password) or not any(char.islower() for char in password):
            flash("Password must be greater than 8 characters, contain at least 1 digit, one special character, and one uppercase letter.", category="invalid")
     else:
            newuser=User(email=email,username=username,password=generate_password_hash(password1,method='sha256'))
            db.session.add(newuser)
            db.session.commit()
            login_user(newuser,remember=True)
            flash("Account created successfully.", category="valid")
            return redirect(url_for('views.home'))

   return render_template("signup.html",user=current_user)






