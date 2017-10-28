from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class SMSForm(FlaskForm):
    to = StringField("To", validators=[DataRequired()])
    body = StringField("Message", validators=[DataRequired()])
