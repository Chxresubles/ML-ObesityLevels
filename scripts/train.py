import json
import pickle
import argparse
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from mlobesitylevels.trainer import ModelTrainer
from mlobesitylevels.dataloader import DataLoader
from mlobesitylevels.preprocessor import ObesityPreprocessor
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
    parser.add_argument(
        "--train-split",
        type=float,
        default=0.8,
        help="Ratio of training data (default: 0.8)",
    )
    parser.add_argument(
        "--crossvalidation", action="store_true", help="Enable cross-validation"
    )
    parser.add_argument(
        "--cv-folds",
        type=int,
        default=5,
        help="Number of cross-validation folds (default: 5)",
    )
    args = parser.parse_args()

    seed = 42

    dataloader = DataLoader(args.file_path, [ColumnValidator(), TypeValidator()])
    preprocessor = ObesityPreprocessor()

    X, y = dataloader.get_data()
    X, y = preprocessor.fit_transform(X, y)

    model = RandomForestClassifier(
        n_estimators=22, max_depth=8, criterion="entropy", random_state=seed
    )

    trainer = ModelTrainer(model)

    accuracy_report = trainer.train(
        X,
        y,
        crossvalidation=args.crossvalidation,
        cv_folds=args.cv_folds,
        train_split=args.train_split,
        seed=seed,
    )

    if args.crossvalidation:
        print(f"Model crossvalidation mean accuracy = {accuracy_report['cv_mean']}")
    else:
        print(f"Model test accuracy = {accuracy_report['accuracy']}")

    out_path = Path(args.output_path)
    out_path.mkdir(parents=True, exist_ok=True)

    with open(out_path / "preprocessor.pkl", "wb") as f:
        pickle.dump(preprocessor, f)

    if not args.crossvalidation:
        with open(out_path / "model.pkl", "wb") as f:
            pickle.dump(model, f)

    with open(out_path / "model_accuracies.json", "w") as f:
        json.dump(accuracy_report, f, indent=2)
