import pickle
import numpy as np
from sklearn.datasets import load_iris
from flask import Flask, render_template, url_for
from forms import QueryForm

# Create the flask app instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Create route handler (Controller)
@app.route("/", methods=["GET", "POST"])
def home():
    form = QueryForm()
    content = ""
    
    if form.validate_on_submit():
        try:
            # load the trained model
            with open("./data/random_forest_model.pkl", "rb") as file:
                model = pickle.load(file)

            # get new data for prediction from web users input
            new_data = np.array([[
                form.sepal_length.data,
                form.sepal_width.data,
                form.petal_length.data,
                form.petal_width.data
            ]])

            # make a prediction
            prediction = model.predict(new_data)

            # prepare output string
            iris = load_iris()
            content = f"Prediction: {iris.target_names[prediction][0]}"

        except Exception as ex:
            content = f"Something bad has happen... {ex}"

    return render_template('home.html', content=content, form=form)