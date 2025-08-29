import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# ################################## sleepData ##########################################
# def load_sleep_data():

#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     data_folder = os.path.join(current_dir, "..", "data", "BRONZE")
#     data_folder = os.path.abspath(data_folder)  # ensures proper full path

#     sleep_records = []

#     # Walk through files in folder
#     for filename in os.listdir(data_folder):
#         if "sleepData" in filename and filename.endswith(".json"):
#             filepath = os.path.join(data_folder, filename)

#             with open(filepath, "r") as f:
#                 try:
#                     records = json.load(f)

#                     # Check if there are any records 
#                     if isinstance(records, list):
#                         sleep_records.extend(records)
                    
#                     # If one record (dict)
#                     elif isinstance(records, dict):
#                         sleep_records.append(records)
#                 except Exception as e:
#                     print("Skipping {filename}: {e}")

#     # To pd DataFrame
#     #sleep_df = pd.DataFrame(sleep_records)
#     sleep_df = pd.json_normalize(sleep_records, sep="_")


#     # Define which columns should be datetimes
#     date_columns = [
#         "sleepStartTimestampGMT",
#         "sleepEndTimestampGMT",
#         "calendarDate",
#         "spo2SleepSummary_sleepMeasurementStartGMT",
#         "spo2SleepSummary_sleepMeasurementEndGMT"
#     ]

#     # Convert them to datetime, safely (errors="coerce" makes invalid dates into NaT)
#     for col in date_columns:
#         if col in sleep_df.columns:
#             sleep_df[col] = pd.to_datetime(sleep_df[col], errors="coerce")

#     # Sort by date
#     sleep_df = sleep_df[sleep_df["calendarDate"].notna()]
#     sleep_df = sleep_df.sort_values("calendarDate")

#     return sleep_df

# ################################## fitnessAgeData #####################################
# def load_fitness_age():

#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     data_folder = os.path.join(current_dir, "..", "data", "BRONZE")
#     data_folder = os.path.abspath(data_folder)  # ensures proper full path

#     fitness_records = []

#     # Walk through files in folder
#     for filename in os.listdir(data_folder):
#         if "fitnessAgeData" in filename and filename.endswith(".json"):
#             filepath = os.path.join(data_folder, filename)

#             with open(filepath, "r") as f:
#                 try:
#                     records = json.load(f)

#                     # Check if there are any records 
#                     if isinstance(records, list):
#                         fitness_records.extend(records)
                    
#                     # If one record (dict)
#                     elif isinstance(records, dict):
#                         fitness_records.append(records)
#                 except Exception as e:
#                     print("Skipping {filename}: {e}")

#     # To pd DataFrame
#     fintess_age_df = pd.json_normalize(fitness_records, sep="_")

#     # Define which columns should be datetimes
#     date_columns = [
#         "asOfDateGmt"
#     ]

#     # Convert them to datetime, safely (errors="coerce" makes invalid dates into NaT)
#     for col in date_columns:
#         if col in fintess_age_df.columns:
#             fintess_age_df[col] = pd.to_datetime(fintess_age_df[col], errors="coerce")

#     # Sort by date
#     fintess_age_df = fintess_age_df[fintess_age_df["asOfDateGmt"].notna()]
#     fintess_age_df = fintess_age_df.sort_values("asOfDateGmt")

#     return fintess_age_df

# ################################## HydrationLogFile ###################################
# def load_hydration_data():

#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     data_folder = os.path.join(current_dir, "..", "data", "BRONZE")
#     data_folder = os.path.abspath(data_folder)  # ensures proper full path

#     hydration_records = []

#     # Walk through files in folder
#     for filename in os.listdir(data_folder):
#         if "HydrationLogFile" in filename and filename.endswith(".json"):
#             filepath = os.path.join(data_folder, filename)

#             with open(filepath, "r") as f:
#                 try:
#                     records = json.load(f)

#                     # Check if there are any records 
#                     if isinstance(records, list):
#                         hydration_records.extend(records)
                    
#                     # If one record (dict)
#                     elif isinstance(records, dict):
#                         hydration_records.append(records)
#                 except Exception as e:
#                     print("Skipping {filename}: {e}")

#     # To pd DataFrame
#     hydration_df = pd.json_normalize(hydration_records, sep="_")


#     # Define which columns should be datetimes
#     date_columns = [
#         "persistedTimestampGMT"
#     ]

#     # Convert them to datetime, safely (errors="coerce" makes invalid dates into NaT)
#     for col in date_columns:
#         if col in hydration_df.columns:
#             hydration_df[col] = pd.to_datetime(hydration_df[col], errors="coerce")

#     # Sort by date
#     hydration_df = hydration_df[hydration_df["persistedTimestampGMT"].notna()]
#     hydration_df = hydration_df.sort_values("persistedTimestampGMT")

#     return hydration_df

# ################################## TrainingReadiness ##################################
# def load_training_data():

#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     data_folder = os.path.join(current_dir, "..", "data", "BRONZE")
#     data_folder = os.path.abspath(data_folder)  # ensures proper full path

#     training_records = []

#     # Walk through files in folder
#     for filename in os.listdir(data_folder):
#         if "TrainingReadiness" in filename and filename.endswith(".json"):
#             filepath = os.path.join(data_folder, filename)

#             with open(filepath, "r") as f:
#                 try:
#                     records = json.load(f)

#                     # Check if there are any records 
#                     if isinstance(records, list):
#                         training_records.extend(records)
                    
#                     # If one record (dict)
#                     elif isinstance(records, dict):
#                         training_records.append(records)
#                 except Exception as e:
#                     print("Skipping {filename}: {e}")

#     # To pd DataFrame
#     training_df = pd.json_normalize(training_records, sep="_")


#     # Define which columns should be datetimes
#     date_columns = [
#         "timestamp"
#     ]

#     # Convert them to datetime, safely (errors="coerce" makes invalid dates into NaT)
#     for col in date_columns:
#         if col in training_df.columns:
#             training_df[col] = pd.to_datetime(training_df[col], errors="coerce")

#     # Sort by date
#     training_df = training_df[training_df["timestamp"].notna()]
#     training_df = training_df.sort_values("timestamp")

#     return training_df

################################## USDFile ############################################
def load_usd_file():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(current_dir, "..", "data", "BRONZE")
    data_folder = os.path.abspath(data_folder)  # ensures proper full path

    usd_records = []

    # Walk through files in folder
    for filename in os.listdir(data_folder):
        if "UDSFile" in filename and filename.endswith(".json"):
            filepath = os.path.join(data_folder, filename)

            with open(filepath, "r") as f:
                try:
                    records = json.load(f)

                    # Check if there are any records 
                    if isinstance(records, list):
                        usd_records.extend(records)
                    
                    # If one record (dict)
                    elif isinstance(records, dict):
                        usd_records.append(records)
                except Exception as e:
                    print("Skipping {filename}: {e}")

    # To pd DataFrame
    usd_df = pd.json_normalize(usd_records, sep="_")
    
    # Define which columns should be datetimes
    date_columns = [
        "calendarDate",
        "statTimestamp",
        "wellnessStartTimeGmt",
        "wellnessEndTimeGmt"
    ]

    # Convert them to datetime, safely (errors="coerce" makes invalid dates into NaT)
    for col in date_columns:
        if col in usd_df.columns:
            usd_df[col] = pd.to_datetime(usd_df[col], errors="coerce")

    # Sort by date
    usd_df = usd_df[usd_df["calendarDate"].notna()]
    usd_df = usd_df.sort_values("calendarDate")

    return usd_df

################################## Extract ############################################
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    silver_dir = os.path.join(current_dir, "..", "data", "SILVER")
    os.makedirs(silver_dir, exist_ok=True)

    # # Sleep Data
    # sleep_df = load_sleep_data()
    # print("Sleep data combined!")
    # print(sleep_df.head())
    # sleep_path = os.path.join(silver_dir, "sleep_data.csv")
    # sleep_df.to_csv(sleep_path, index=False)
    # print(f"Saved sleep data to {sleep_path}")

    # # Fitness Age Data
    # fitness_age_df = load_fitness_age()
    # fitness_age_path = os.path.join(silver_dir, "fitness_age.csv")
    # fitness_age_df.to_csv(fitness_age_path, index=False)
    # print(f"Saved fitness age data to {fitness_age_path}")

    # # Hydration Data
    # hydration_df = load_hydration_data()
    # hydration_path = os.path.join(silver_dir, "hydration_data.csv")
    # hydration_df.to_csv(hydration_path, index=False)
    # print(f"Saved hydration data to {hydration_path}")

    # # Training Data
    # training_df = load_training_data()
    # training_path = os.path.join(silver_dir, "training_data.csv")
    # training_df.to_csv(training_path, index=False)
    # print(f"Saved training data to {training_path}")

    # USD File
    usd_df = load_usd_file()
    usd_path = os.path.join(silver_dir, "usd_data.csv")
    usd_df.to_csv(usd_path, index=False)
    print(f"Saved USD data to {usd_path}")


