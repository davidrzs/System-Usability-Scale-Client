from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class Step1(FlaskForm):
    q1 = RadioField("Frage 1",validators=[DataRequired()],choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q2 = RadioField("Frage 2",validators=[DataRequired()],choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q3 = RadioField("Frage 3",validators=[DataRequired()],choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q4 = RadioField("Frage 4",validators=[DataRequired()],choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q5 = RadioField("Frage 5",choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q6 = RadioField("Frage 6",choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q7 = RadioField("Frage 7",choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q8 = RadioField("Frage 8",choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q9 = RadioField("Frage 9",choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])
    q10 = RadioField("Frage 10",choices=[('1','Stimme voll zu'),('2',''), ('3',''), ('4',''), ('5','Stimme gar nicht zu')])


class Step2(FlaskForm):
    open1 = StringField('Frage 1', widget=TextArea(), validators=[DataRequired()])
    open2 = StringField('Frage 2', widget=TextArea(), validators=[DataRequired()])
    open3 = StringField('Frage 3', widget=TextArea(), validators=[DataRequired()])
    open4 = StringField('Frage 4', widget=TextArea(), validators=[DataRequired()])
    open5 = StringField('Frage 5', widget=TextArea(), validators=[DataRequired()])
    open6 = StringField('Frage 6', widget=TextArea(), validators=[DataRequired()])