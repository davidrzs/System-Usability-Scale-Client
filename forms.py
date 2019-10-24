from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired

class Step1(FlaskForm):
    test1 = RadioField('test1',choices=[('1','Very well'),('2','Not at all'), ('3','Not at all'), ('4','Not at all'), ('5','Not at all')])


class Step2(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

"""

    I think that I would like to use this system frequently.
    I found the system unnecessarily complex.
    I thought the system was easy to use.
    I think that I would need the support of a technical person to be able to use this system.
    I found the various functions in this system were well integrated.
    I thought there was too much inconsistency in this system.
    I would imagine that most people would learn to use this system very quickly.
    I found the system very cumbersome to use.
    I felt very confident using the system.
    I needed to learn a lot of things before I could get going with this system.

"""