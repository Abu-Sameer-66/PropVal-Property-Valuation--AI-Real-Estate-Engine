import pandas as pd
import numpy as np
try:
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.metrics import mean_squared_error, r2_score
except ImportError:
    raise ImportError("Sklearn not found. Please run: pip install scikit-learn")

class RealEstateValuator:
    """
    A pipeline for processing real estate data and training a Gradient Boosting model.
    """

    def __init__(self, train_path, test_path):
        self.train_path = train_path
        self.test_path = test_path
        self.model = GradientBoostingRegressor(
            n_estimators=1000, 
            learning_rate=0.05, 
            max_depth=3, 
            random_state=42
        )
        self.is_fitted = False

    def _load_data(self):
        try:
            train_df = pd.read_csv(self.train_path)
            test_df = pd.read_csv(self.test_path)
            return train_df, test_df
        except FileNotFoundError:
            raise FileNotFoundError(f"Files not found. Check {self.train_path} and {self.test_path}")

    def preprocess(self):
        """
        Loads data, handles missing values, log-transforms target, 
        and performs one-hot encoding.
        """
        train_df, test_df = self._load_data()

        # Log transform target variable
        # Using log1p to handle potential zero values safely
        train_df['SalePrice'] = np.log1p(train_df['SalePrice'])
        self.y = train_df['SalePrice']
        
        # Prepare for concatenation
        train_features = train_df.drop(['SalePrice', 'Id'], axis=1)
        self.test_ids = test_df['Id']
        test_features = test_df.drop(['Id'], axis=1)
        
        # Concat to ensure consistent encoding
        all_data = pd.concat([train_features, test_features]).reset_index(drop=True)
        
        # Impute missing values
        num_cols = all_data.select_dtypes(include=np.number).columns
        cat_cols = all_data.select_dtypes(include='object').columns
        
        # Fill numeric with median, categorical with "None"
        all_data[num_cols] = all_data[num_cols].fillna(all_data[num_cols].median())
        all_data[cat_cols] = all_data[cat_cols].fillna("None")
        
        # One-Hot Encoding
        # CRITICAL FIX: dtype=int ensures output is 0/1, not True/False
        all_data_encoded = pd.get_dummies(all_data, dtype=int)
        
        # Split back into train and submission sets
        self.X = all_data_encoded.iloc[:len(self.y), :]
        self.X_submission = all_data_encoded.iloc[len(self.y):, :]
        
        return self.X, self.y

    def train(self, test_size=0.2):
        """
        Trains the model and returns validation metrics.
        """
        if not hasattr(self, 'X'):
            self.preprocess()

        # Ensure data is in the correct format for sklearn
        X_train, X_val, y_train, y_val = train_test_split(
            self.X, self.y, test_size=test_size, random_state=42
        )
        
        self.model.fit(X_train, y_train)
        self.is_fitted = True
        
        preds = self.model.predict(X_val)
        rmse = np.sqrt(mean_squared_error(y_val, preds))
        r2 = r2_score(y_val, preds)
        
        return {
            'rmse': rmse,
            'r2': r2,
            'y_val': y_val,
            'predicted': preds,
            'feature_names': self.X.columns,
            'importances': self.model.feature_importances_
        }

    def predict_submission(self, filename='submission.csv'):
        """
        Generates predictions for the test set and saves to CSV.
        """
        if not self.is_fitted:
            raise Exception("Model must be trained before generating submission.")
            
        # Inverse log transform to get actual prices
        final_preds = np.expm1(self.model.predict(self.X_submission))
        
        submission = pd.DataFrame({
            'Id': self.test_ids,
            'SalePrice': final_preds
        })
        submission.to_csv(filename, index=False)
        print(f"Submission saved to {filename}")