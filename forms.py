from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class Step1(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
# Ich kann mir sehr gut vorstellen, das System regelmäßig zu nutzen.


class Step2(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
