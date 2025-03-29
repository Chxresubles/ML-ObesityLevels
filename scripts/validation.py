import json
import pickle
import argparse
from pathlib import Path
from mlobesitylevels.trainer import ModelTrainer
from mlobesitylevels.dataloader import DataLoader
from mlobesitylevels.validators import ColumnValidator, TypeValidator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train obesity level classifier")
    parser.add_argument(
        "--file-path",
        type=str,
        default="./data/ObesityDataSet_raw_and_data_sinthetic.csv",
        help="Path to input CSV data file",
    )
    parser.add_argument(
        "--output-path",
        type=str,
        default="./output",
        help="Path to output folder",
    )
    args = parser.parse_args()

    out_path = Path(args.output_path)
    with open(out_path / "preprocessor.pkl", "rb") as f:
        preprocessor = pickle.load(f)
    with open(out_path / "model.pkl", "rb") as f:
        model = pickle.load(f)

    dataloader = DataLoader(args.file_path, [ColumnValidator(), TypeValidator()])
    X, y = dataloader.get_data()
    X, y = preprocessor.transform(X, y)

    validator = ModelTrainer(model)

    accuracy_report = validator.evaluate(X, y)

    print(f"Model test accuracy = {accuracy_report['accuracy']}")

    with open(out_path / "model_validation_accuracies.json", "w") as f:
        json.dump(accuracy_report, f, indent=2)
