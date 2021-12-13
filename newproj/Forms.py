from flask_wtf import Form

from wtforms.fields import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms.validators import Email, DataRequired


class ContactForm(Form):
    Name = StringField("Name Of Student", [DataRequired("Please enter your name.")])
    Gender = RadioField("Gender", choices=[("M", "Male"), ("F", "Female")])
    Address = TextAreaField("Address")
    Email = StringField("Email", [DataRequired("Please enter your email"), Email("Please enter your email")])
    Age = IntegerField("Age")
    Language = SelectField("Languages", choices=[("cpp", "C++"), ("py", "Python")])
    Submit = SubmitField("Send")
