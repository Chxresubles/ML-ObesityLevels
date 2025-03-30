# Machine Learning example - Obesity levels dataset insights and obesity prediciton
An example machine learning project displaying insights on the [Obesity Levels Dataset](https://www.kaggle.com/datasets/fatemehmehrparvar/obesity-levels).
The notebook also trains different machine learning models and displays the resulting accuracies.


## Get started
To get started, download the [Obesity Levels Dataset](https://www.kaggle.com/datasets/fatemehmehrparvar/obesity-levels) CSV file and copy it to a folder named `data` in the root directory of the project.


## Data insights and all ML model trainer
The notebook `data_insight_and_training.ipynb` loads the data from CSV file, displays graphs and descriptions of the data and the different columns.
It also performs a grid search on multiple machine learning problems to find which model is the best fit for this project.

1. Install the required packages
```console
pip install -r requirements.txt
```

2. Run the `data_insight_and_training.ipynb`


## Best model training and validation
The scripts contained in the `scripts` contain the necessary code to train, validate and run the inference of the selected best model.
It uses the local module `mlobesitylevels` containing the project-specific source code.

1. Install the `mlobesitylevels` module
```console
pip install .
```

2. Train the model
```console
python ./scripts/train.py
```
The scripts saves the preprocessor, the model and the test accuracy in the `output` folder.

3. Validate the model on new data
```console
python ./scripts/validation.py --file-path ./data/new_validation_data.csv
```


## Deploy API

### Run locally
The `Dockerfile` contains a minimal environment to deploy an API on port 8000.

1. Install the `mlobesitylevels` module
```console
pip install .
```

2. Deploy the API
```console
python ./scripts/score.py
```

3. Send a test request to the API.
```console
python ./scripts/test_api.py
```

### Using Docker
The `Dockerfile` contains a minimal environment to deploy an API on port 8000.

1. Build the `Dockerfile`
```console
docker build . -t mlobesitylevels-api
```

2. Run the Docker image locally
```console
docker run --rm -p 8000:8000 mlobesitylevels-api
```
You can also use the `-d` option to run the Docker image in the background.

3. Send a test request to the API.
```console
python ./scripts/test_api.py
```
