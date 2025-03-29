import pandas as pd
from typing import Optional, Self
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin
from mlobesitylevels.constants import (
    BMI,
    HEIGHT,
    WEIGHT,
    WATER_INTAKE,
    WATER_PER_KG,
    OBESITY_LEVEL,
    COLUMN_ENCODING,
    COLUMNS_TO_SCALE,
)


class ObesityPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.fitted = False
        self.scaler = StandardScaler()

    def _scale_data(self, data: pd.DataFrame) -> pd.DataFrame:
        scaled_data = data.copy()

        scaled_data_subset = self.scaler.transform(
            scaled_data[COLUMNS_TO_SCALE].to_numpy()
        )
        scaled_data[COLUMNS_TO_SCALE] = scaled_data_subset

        return scaled_data

    def _encode_data(self, data: pd.DataFrame) -> pd.DataFrame:
        encoded_data = data.copy()

        for col, encodings in COLUMN_ENCODING.items():
            if col in encoded_data:
                encoded_data[col] = pd.to_numeric(encoded_data[col].map(encodings))

        return encoded_data

    def _add_new_features(self, data: pd.DataFrame) -> pd.DataFrame:
        added_data = data.copy()
        added_data[BMI] = added_data[WEIGHT] / (added_data[HEIGHT]) ** 2
        added_data[WATER_PER_KG] = added_data[WATER_INTAKE] / added_data[WEIGHT]
        return added_data

    def fit(self, X: pd.DataFrame, y: Optional[pd.Series] = None) -> Self:
        X_copy = X.copy()

        X_copy = self._add_new_features(X_copy)
        self.scaler = self.scaler.fit(X_copy[COLUMNS_TO_SCALE].to_numpy())

        self.fitted = True
        return self

    def transform(
        self, X: pd.DataFrame, y: Optional[pd.Series] = None
    ) -> tuple[pd.DataFrame, Optional[pd.Series]]:
        if not self.fitted:
            raise ValueError("Preprocessor needs to be fitted first")

        X_transformed = X.copy()

        X_transformed = self._add_new_features(X_transformed)
        X_transformed = self._encode_data(X_transformed)
        X_transformed = self._scale_data(X_transformed)

        if y is None:
            return X_transformed

        y_transformed = y.copy()
        y_transformed = pd.to_numeric(y_transformed.map(COLUMN_ENCODING[OBESITY_LEVEL]))

        return X_transformed, y_transformed

    def fit_transform(
        self, X: pd.DataFrame, y: Optional[pd.Series] = None
    ) -> tuple[pd.DataFrame, Optional[pd.Series]]:
        return self.fit(X, y).transform(X, y)
