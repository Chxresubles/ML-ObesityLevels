from typing import Optional
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report


class ModelTrainer:
    def __init__(self, model: BaseEstimator) -> None:
        self.model = model

    def train(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        crossvalidation: Optional[bool] = False,
        cv_folds: Optional[int] = 5,
        train_split: Optional[int] = 0.8,
        seed: Optional[int] = 42,
    ) -> dict:
        if crossvalidation:
            cv_scores = cross_val_score(self.model, X, y, cv=cv_folds)
            return {
                "cv_scores": cv_scores.tolist(),
                "cv_mean": np.mean(cv_scores),
                "cv_std": np.std(cv_scores),
            }

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=1 - train_split, random_state=seed
        )
        self.model.fit(X_train, y_train)
        return self.evaluate(X_test, y_test)

    def evaluate(self, X: pd.DataFrame, y: pd.Series) -> dict:
        y_pred = self.model.predict(X)
        accuracy = accuracy_score(y, y_pred)
        report = classification_report(y, y_pred)

        return {"accuracy": accuracy, "classification_report": report}

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        return self.model.predict(X)
