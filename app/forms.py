
from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired

description = TextAreaField(u'Description', [validators.DataRequired()])
photo = FileField('Photo', validators=[
    FileRequired(),
    FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
])