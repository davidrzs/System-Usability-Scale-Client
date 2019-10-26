from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class Step1(FlaskForm):
    q1 = RadioField('test1',validators=[DataRequired()],choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q2 = RadioField('test1',validators=[DataRequired()],choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q3 = RadioField('test1',validators=[DataRequired()],choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q4 = RadioField('test1',validators=[DataRequired()],choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q5 = RadioField('test1',choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q6 = RadioField('test1',choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q7 = RadioField('test1',choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q8 = RadioField('test1',choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q9 = RadioField('test1',choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q10 = RadioField('test1',choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])


class Step2(FlaskForm):
    open1 = StringField('name', widget=TextArea(), validators=[DataRequired()])
    open2 = StringField('name', widget=TextArea(), validators=[DataRequired()])
    open3 = StringField('name', widget=TextArea(), validators=[DataRequired()])
    open4 = StringField('name', widget=TextArea(), validators=[DataRequired()])
    open5 = StringField('name', widget=TextArea(), validators=[DataRequired()])
    open6 = StringField('name', widget=TextArea(), validators=[DataRequired()])