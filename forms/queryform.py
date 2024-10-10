from flask_wtf import FlaskForm
from wtforms import StringField

class QueryForm(FlaskForm):
    sepal_length = StringField("Sepal Length", default="5.1")
    sepal_width = StringField("Sepal Width", default="3.5")
    petal_length = StringField("Petal Length", default="1.4")
    petal_width = StringField("Petal Width", default="0.2")
