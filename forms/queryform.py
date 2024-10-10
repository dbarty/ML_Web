from flask_wtf import FlaskForm
from wtforms import StringField

class QueryForm(FlaskForm):
    input1 = StringField("Input 1", default="5.1")
    input2 = StringField("Input 2", default="3.5")
    input3 = StringField("Input 3", default="1.4")
    input4 = StringField("Input 4", default="0.2")