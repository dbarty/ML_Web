from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pickle

# load example data
iris = load_iris()
X, y = iris.data, iris.target

# split train- and testdata
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create the model and train
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# model persistence
with open("./data/random_forest_model.pkl", "wb") as file:
    pickle.dump(model, file)