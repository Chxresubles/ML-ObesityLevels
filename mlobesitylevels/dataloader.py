from typing import Optional
import pandas as pd
from mlobesitylevels.validators import BaseValidator
from mlobesitylevels.constants import COLUMN_TYPES
from mlobesitylevels.constants import OBESITY_LEVEL


class DataLoader:
    def __init__(
        self, file_path: str, validators: Optional[list[BaseValidator]] = []
    ) -> None:
        self.file_path = file_path
        self.validators = validators
        self.data = None
        self.features = None
        self.labels = None

    def _load_data(self) -> pd.DataFrame:
        specify_dtypes = {}
        for col, values in COLUMN_TYPES.items():
            specify_dtypes[col] = values["type"]
        data = pd.read_csv(self.file_path, dtype=specify_dtypes)
        return data

    def _validate_data(self, data: pd.DataFrame) -> pd.DataFrame:
        for validator in self.validators:
            data = data[validator.validate(data)]
        return data

    def get_data(self) -> tuple[pd.DataFrame, pd.Series]:
        self.data = self._load_data()
        self.data = self.data.drop_duplicates()
        self.data = self._validate_data(self.data)

        self.features = self.data.drop(OBESITY_LEVEL, axis=1)
        self.labels = self.data[OBESITY_LEVEL]

        return self.features, self.labels
