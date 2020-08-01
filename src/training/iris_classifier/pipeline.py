import pandas as pd


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
