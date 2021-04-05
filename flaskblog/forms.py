from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Email
class RegestrationForm(flaskform):
    username=StringField('User Name',validators=[DataRequired(), Length(min 6 max 10)])
    email=StringField('Email',validators=[DataRequired(),Email()])

    