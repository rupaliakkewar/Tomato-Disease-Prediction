import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier


# ============================================================
# 🍅 TOMATO DISEASE PREDICTION SYSTEM
# ============================================================

print("\n🍅 TOMATO DISEASE PREDICTION SYSTEM")
print("=" * 50)


# ============================================================
# 1. PROJECT PATHS
# ============================================================

# main.py च्या location वरून project folder शोधणे
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "tomato_disease_dataset.csv"
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "output"
)

OUTPUT_FILE = os.path.join(
    OUTPUT_DIR,
    "prediction_output.txt"
)


# ============================================================
# 2. CHECK DATASET
# ============================================================

if not os.path.exists(DATASET_PATH):
    print("\n❌ ERROR: Dataset file not found!")
    print("Expected location:")
    print(DATASET_PATH)
    input("\nPress Enter to exit...")
    exit()


# ============================================================
# 3. LOAD DATASET
# ============================================================

try:
    data = pd.read_csv(DATASET_PATH)

except Exception as e:
    print("\n❌ Error while loading dataset:")
    print(e)
    input("\nPress Enter to exit...")
    exit()


print("\n✅ Dataset loaded successfully!")
print("Number of records:", len(data))


# ============================================================
# 4. CHECK REQUIRED COLUMNS
# ============================================================

required_columns = [
    "Temperature",
    "Humidity",
    "Rainfall",
    "Soil_pH",
    "Season",
    "Disease"
]

missing_columns = [
    column for column in required_columns
    if column not in data.columns
]

if missing_columns:
    print("\n❌ Missing columns in dataset:")
    print(missing_columns)

    print("\nRequired columns are:")
    print(required_columns)

    input("\nPress Enter to exit...")
    exit()


# ============================================================
# 5. REMOVE MISSING VALUES
# ============================================================

data = data.dropna()

if len(data) == 0:
    print("\n❌ Dataset contains no valid records.")
    input("\nPress Enter to exit...")
    exit()


# ============================================================
# 6. ENCODE SEASON
# ============================================================

season_encoder = LabelEncoder()

data["Season"] = season_encoder.fit_transform(
    data["Season"].astype(str)
)


# ============================================================
# 7. FEATURES AND TARGET
# ============================================================

features = [
    "Temperature",
    "Humidity",
    "Rainfall",
    "Soil_pH",
    "Season"
]

X = data[features]
y = data["Disease"].astype(str)


# ============================================================
# 8. TRAIN RANDOM FOREST MODEL
# ============================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

print("✅ Machine Learning model trained successfully!")


# ============================================================
# 9. USER INPUT
# ============================================================

print("\n" + "=" * 50)

location = input("Enter Location: ").strip()
crop = input("Enter Crop Name: ").strip()

try:
    soil_ph = float(input("Enter Soil pH: ").strip())

except ValueError:
    print("\n❌ Please enter a valid Soil pH number.")
    input("\nPress Enter to exit...")
    exit()


season = input("Enter Season: ").strip()


# ============================================================
# 10. VALIDATE CROP
# ============================================================

if crop.lower() != "tomato":

    print("\n❌ This system is designed only for Tomato crop.")

    input("\nPress Enter to exit...")
    exit()


# ============================================================
# 11. VALIDATE SEASON
# ============================================================

available_seasons = list(
    season_encoder.classes_
)

season_match = None

for s in available_seasons:

    if s.lower() == season.lower():
        season_match = s
        break


if season_match is None:

    print("\n❌ Invalid season.")

    print("Available seasons:")

    for s in available_seasons:
        print("-", s)

    input("\nPress Enter to exit...")
    exit()


# ============================================================
# 12. WEATHER INFORMATION
# ============================================================
# Demo weather values
# These can later be replaced with Weather API values.
# ============================================================

weather_data = {

    "wani": {
        "temperature": 25.3,
        "humidity": 85,
        "rainfall": 0
    },

    "nagpur": {
        "temperature": 28.0,
        "humidity": 78,
        "rainfall": 5
    },

    "pune": {
        "temperature": 26.0,
        "humidity": 70,
        "rainfall": 3
    },

    "mumbai": {
        "temperature": 29.0,
        "humidity": 82,
        "rainfall": 8
    }
}


location_key = location.lower()


if location_key in weather_data:

    temperature = weather_data[location_key]["temperature"]
    humidity = weather_data[location_key]["humidity"]
    rainfall = weather_data[location_key]["rainfall"]

else:

    # Default weather values
    temperature = 26.0
    humidity = 75.0
    rainfall = 2.0


# ============================================================
# 13. ENCODE USER SEASON
# ============================================================

season_encoded = season_encoder.transform(
    [season_match]
)[0]


# ============================================================
# 14. CREATE INPUT DATAFRAME
# ============================================================
# This avoids feature-name warnings.
# ============================================================

input_data = pd.DataFrame(
    [[
        temperature,
        humidity,
        rainfall,
        soil_ph,
        season_encoded
    ]],
    columns=features
)


# ============================================================
# 15. MACHINE LEARNING PREDICTION
# ============================================================

prediction = model.predict(input_data)[0]


# ============================================================
# 16. PREDICTION CONFIDENCE
# ============================================================

probabilities = model.predict_proba(input_data)[0]

confidence = max(probabilities) * 100


# ============================================================
# 17. RISK LEVEL
# ============================================================

if prediction.lower() == "healthy":

    risk = "LOW"

elif "early" in prediction.lower():

    risk = "MEDIUM"

elif "late" in prediction.lower():

    risk = "HIGH"

else:

    risk = "HIGH"


# ============================================================
# 18. RECOMMENDATION
# ============================================================

if risk == "LOW":

    recommendation = [
        "Tomato plant condition appears healthy.",
        "Continue regular monitoring.",
        "Maintain proper irrigation and nutrition."
    ]

elif risk == "MEDIUM":

    recommendation = [
        "Take preventive measures.",
        "Monitor tomato plants regularly.",
        "Avoid excessive moisture on leaves."
    ]

else:

    recommendation = [
        "Take preventive measures immediately.",
        "Monitor tomato plants regularly.",
        "Remove severely affected leaves if necessary.",
        "Consult an agricultural expert for proper treatment."
    ]


# ============================================================
# 19. DISPLAY RESULT
# ============================================================

result = f"""
==================================================
             🍅 PREDICTION RESULT
==================================================

Location           : {location}
Crop               : {crop}
Season             : {season_match}

🌦 WEATHER INFORMATION
--------------------------------------------------
Temperature        : {temperature} °C
Humidity           : {humidity} %
Rainfall           : {rainfall} mm

🌱 SOIL INFORMATION
--------------------------------------------------
Soil pH            : {soil_ph}

🤖 ML PREDICTION
--------------------------------------------------
Predicted Disease  : {prediction}
Confidence         : {confidence:.2f} %
Risk Level         : {risk}

💡 RECOMMENDATION
--------------------------------------------------
"""


for item in recommendation:

    result += f"{item}\n"


result += "==================================================\n"


print(result)


# ============================================================
# 20. SAVE OUTPUT FILE
# ============================================================

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "🍅 TOMATO DISEASE PREDICTION SYSTEM\n"
    )

    file.write(result)


print(f"✅ Output saved to:")
print(OUTPUT_FILE)

print("\n🎉 Prediction completed successfully!")