import os
import pickle
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.training.iris_classifier.pipeline import IrisClassifier


def train(model_path):
    """Load data from the iris dataset, train a model and pickle save it."""
    # load data from the iris dataset
    iris = load_iris(as_frame=True)
    # do a train test split and load into a data dictionary for ease of use
    train_x, test_x, train_y, test_y = train_test_split(iris.get('data'), iris.get('target'))
    data = {'train_x': train_x, 'test_x': test_x, 'train_y': train_y, 'test_y': test_y}
    model = GradientBoostingClassifier()
    print('fitting model...')
    model.fit(data['train_x'], data['train_y'])
    predictions = model.predict(data['test_x'])
    # wrap the model in the IrisClassifier class that we created
    iris_classifier = IrisClassifier(model, iris.get('feature_names'), iris.get('target_names'))
    print(f"accuracy score on test data: {accuracy_score(data['test_y'], predictions)}")
    # create directory and save model
    if not os.path.exists(os.path.dirname(model_path)):
        os.makedirs(os.path.dirname(model_path))
    print(f'saving model to: {model_path}')
    with open(model_path, 'wb') as f:
        pickle.dump(iris_classifier, f)


def test(model_path):
    """Load the model at the specified path and predict on some sample data."""
    # pickle load the model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    sample_json = [
        {'sepal length (cm)': 5.1, 'sepal width (cm)': 3.5, 'petal length (cm)': 1.4, 'petal width (cm)': 0.2},
        {'sepal length (cm)': 6.7, 'sepal width (cm)': 3.0, 'petal length (cm)': 5.2, 'petal width (cm)': 2.3}
    ]
    # predict on a sample of data
    predictions = model.predict(sample_json)
    print(f'here are some predictions: \n{predictions}')


if __name__ == '__main__':
    model_path = 'src/models/iris_classifier.model'
    train(model_path)
    test(model_path)
