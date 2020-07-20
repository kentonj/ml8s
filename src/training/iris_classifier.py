import os
import pickle
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class IrisClassifier(object):
    def __init__(self, model, feature_names, target_names):
        """Class to wrap a model, along with requires features and target outputs."""
        self.model = model
        self.feature_names = feature_names
        self.target_names = target_names
    def predict(self, records):
        """Take records as an array of json objects, transform into a dataframe, predict and then return as an array of json objects."""
        df = pd.DataFrame(records)
        if not all([feature in df.columns for feature in self.feature_names]):
            # make sure that all the required features are present
            raise ValueError(f'not all required features provided: {self.feature_names}')
        predictions = self.model.predict(df)
        return [{'label': self.target_names[x]} for x in predictions]
        

def train():
    # load data from the iris dataset
    iris = load_iris(as_frame=True)
    # do a train test split and load into a data dictionary for ease of use
    train_x, test_x, train_y, test_y = train_test_split(iris.get('data'), iris.get('target'))
    data = {'train_x': train_x, 'test_x': test_x, 'train_y': train_y, 'test_y': test_y}
    model = GradientBoostingClassifier()
    print('fitting model...')
    model.fit(data['train_x'], data['train_y'])
    predictions = model.predict(data['test_x'])
    iris_classifier = IrisClassifier(model, iris.get('feature_names'), iris.get('target_names'))
    print(f"accuracy score on test data: {accuracy_score(data['test_y'], predictions)}")
    model_path = 'src/models/iris_classifier.model'
    if not os.path.exists(os.path.dirname(model_path)):
        os.makedirs(os.path.dirname(model_path))
    print(f'saving model to: {model_path}')
    with open(model_path, 'wb') as f:
        pickle.dump(iris_classifier, f)
    sample_json = [
        {'sepal length (cm)': 5.1, 'sepal width (cm)': 3.5, 'petal length (cm)': 1.4, 'petal width (cm)': 0.2},
        {'sepal length (cm)': 6.7, 'sepal width (cm)': 3.0, 'petal length (cm)': 5.2, 'petal width (cm)': 2.3}
    ]
    iris_classifier.predict(sample_json)
    print('done')


if __name__ == '__main__':
    train()
