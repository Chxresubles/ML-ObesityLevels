AGE = "Age"
GENDER = "Gender"
HEIGHT = "Height"
WEIGHT = "Weight"
ALCOHOL_FREQUENCY = "CALC"
HIGH_CALORIE = "FAVC"
VEGETABLES_IN_MEALS = "FCVC"
MEALS_PER_DAY = "NCP"
CALORIE_MONITORING = "SCC"
SMOKE = "SMOKE"
WATER_INTAKE = "CH2O"
FAMILY_HISTORY_OVERWEIGHT = "family_history_with_overweight"
PHYSICAL_ACTIVITIES = "FAF"
TECHNOLOGY_TIME = "TUE"
SNACK_FREQUENCY = "CAEC"
TRANSPORT = "MTRANS"
OBESITY_LEVEL = "NObeyesdad"

BMI = "BMI"
WATER_PER_KG = "Water_Intake_Per_Kg"

DATA_COLUMNS = [
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
    OBESITY_LEVEL,
]

COLUMN_TYPES = {
    AGE: {
        "type": "float",
        "min": 10,
        "max": 100,
    },
    GENDER: {
        "type": "object",
        "values": ["Female", "Male"],
    },
    HEIGHT: {
        "type": "float",
        "min": 1,
        "max": 2.7,
    },
    WEIGHT: {
        "type": "float",
        "min": 30,
        "max": 440,
    },
    ALCOHOL_FREQUENCY: {
        "type": "object",
        "values": ["no", "Sometimes", "Frequently", "Always"],
    },
    HIGH_CALORIE: {
        "type": "object",
        "values": ["no", "yes"],
    },
    VEGETABLES_IN_MEALS: {
        "type": "float",
        "min": 1,
        "max": 3,
    },
    MEALS_PER_DAY: {
        "type": "float",
        "min": 1,
        "max": 5,
    },
    CALORIE_MONITORING: {
        "type": "object",
        "values": ["no", "yes"],
    },
    SMOKE: {
        "type": "object",
        "values": ["no", "yes"],
    },
    WATER_INTAKE: {
        "type": "float",
        "min": 1,
        "max": 3,
    },
    FAMILY_HISTORY_OVERWEIGHT: {
        "type": "object",
        "values": ["no", "yes"],
    },
    PHYSICAL_ACTIVITIES: {
        "type": "float",
        "min": 0,
        "max": 3,
    },
    TECHNOLOGY_TIME: {
        "type": "float",
        "min": 0,
        "max": 2,
    },
    SNACK_FREQUENCY: {
        "type": "object",
        "values": ["no", "Sometimes", "Frequently", "Always"],
    },
    TRANSPORT: {
        "type": "object",
        "values": [
            "Walking",
            "Bike",
            "Public_Transportation",
            "Motorbike",
            "Automobile",
        ],
    },
    OBESITY_LEVEL: {
        "type": "object",
        "values": [
            "Insufficient_Weight",
            "Normal_Weight",
            "Overweight_Level_I",
            "Overweight_Level_II",
            "Obesity_Type_I",
            "Obesity_Type_II",
            "Obesity_Type_III",
        ],
    },
}

COLUMNS_TO_SCALE = [
    AGE,
    HEIGHT,
    WEIGHT,
    VEGETABLES_IN_MEALS,
    MEALS_PER_DAY,
    WATER_INTAKE,
    PHYSICAL_ACTIVITIES,
    TECHNOLOGY_TIME,
    BMI,
    WATER_PER_KG,
]

COLUMN_ENCODING = {
    GENDER: {
        "Female": 0,
        "Male": 1,
    },
    ALCOHOL_FREQUENCY: {
        "no": 0,
        "Sometimes": 1,
        "Frequently": 2,
        "Always": 3,
    },
    HIGH_CALORIE: {
        "no": 0,
        "yes": 1,
    },
    CALORIE_MONITORING: {
        "no": 0,
        "yes": 1,
    },
    SMOKE: {
        "no": 0,
        "yes": 1,
    },
    FAMILY_HISTORY_OVERWEIGHT: {
        "no": 0,
        "yes": 1,
    },
    SNACK_FREQUENCY: {
        "no": 0,
        "Sometimes": 1,
        "Frequently": 2,
        "Always": 3,
    },
    TRANSPORT: {
        "Walking": 0,
        "Bike": 1,
        "Public_Transportation": 2,
        "Motorbike": 3,
        "Automobile": 4,
    },
    OBESITY_LEVEL: {
        "Insufficient_Weight": 0,
        "Normal_Weight": 1,
        "Overweight_Level_I": 2,
        "Overweight_Level_II": 3,
        "Obesity_Type_I": 4,
        "Obesity_Type_II": 5,
        "Obesity_Type_III": 6,
    },
}
