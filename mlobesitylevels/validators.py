import pandas as pd
import numpy as np
from mlobesitylevels.constants import DATA_COLUMNS, COLUMN_TYPES


class BaseValidator:
    def validate(self, data: pd.DataFrame) -> np.ndarray:
        raise NotImplementedError("Subclasses should implement this method")


class ColumnValidator(BaseValidator):
    def validate(self, data: pd.DataFrame) -> np.ndarray:
        missing_columns = [col for col in DATA_COLUMNS if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing columns: {', '.join(missing_columns)}")
        return np.array([True] * len(data))


class TypeValidator(BaseValidator):
    def validate(self, data: pd.DataFrame) -> np.ndarray:
        valid_rows = np.ones((len(data)), dtype=bool)
        for col, constraints in COLUMN_TYPES.items():
            if data[col].dtype != constraints["type"]:
                raise ValueError(
                    f"Wrong column type: {col} ({data[col].dtype} should be {constraints["type"]})"
                )
            if constraints["type"] in [int, float]:
                valid_rows = np.logical_and(valid_rows, data[col] >= constraints["min"])
                valid_rows = np.logical_and(valid_rows, data[col] <= constraints["max"])
            elif constraints["type"] is str:
                valid_rows = np.logical_and(
                    valid_rows, data[col] in constraints["values"]
                )
        return valid_rows
