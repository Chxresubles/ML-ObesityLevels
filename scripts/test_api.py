import argparse
import pandas as pd
import requests
from mlobesitylevels.constants import (
    AGE,
    GENDER,
    HEIGHT,
    WEIGHT,
    ALCOHOL_FREQUENCY,
    HIGH_CALORIE,
    VEGETABLES_IN_MEALS,
    MEALS_PER_DAY,
    CALORIE_MONITORING,
    SMOKE,
    WATER_INTAKE,
    FAMILY_HISTORY_OVERWEIGHT,
    PHYSICAL_ACTIVITIES,
    TECHNOLOGY_TIME,
    SNACK_FREQUENCY,
    TRANSPORT,
)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test obesity prediction API")
    parser.add_argument(
        "--uri",
        type=str,
        default="http://127.0.0.1:8000/predict",
        help="API endpoint URI (default: http://127.0.0.1:8000/predict)",
    )
    args = parser.parse_args()

    # Load sample CSV data into DataFrame
    df = pd.DataFrame(
        [
            [
                21,
                "Female",
                1.62,
                64,
                "no",
                "no",
                2,
                3,
                "no",
                "no",
                2,
                "yes",
                0,
                1,
                "Sometimes",
                "Public_Transportation",
            ]
        ],
        columns=[
            AGE,
            GENDER,
            HEIGHT,
            WEIGHT,
            ALCOHOL_FREQUENCY,
            HIGH_CALORIE,
            VEGETABLES_IN_MEALS,
            MEALS_PER_DAY,
            CALORIE_MONITORING,
            SMOKE,
            WATER_INTAKE,
            FAMILY_HISTORY_OVERWEIGHT,
            PHYSICAL_ACTIVITIES,
            TECHNOLOGY_TIME,
            SNACK_FREQUENCY,
            TRANSPORT,
        ],
    )

    # Convert DataFrame to dict for JSON payload
    payload = df.to_dict(orient="records")[0]

    try:
        # Send POST request to API
        response = requests.post(args.uri, json=payload)

        # Check response
        if response.status_code == 200:
            print("Success!")
            print("Response:", response.json())
        else:
            print(f"Error: Status code {response.status_code}")
            print("Response:", response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")


if __name__ == "__main__":
    main()
