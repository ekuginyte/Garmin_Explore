import os
import json
import pandas as pd


# Concat all available sleep data
def load_sleep_data():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(current_dir, "..", "data", "BRONZE")
    data_folder = os.path.abspath(data_folder)  # ensures proper full path

    sleep_records = []

    # Walk through files in folder
    for filename in os.listdir(data_folder):
        if "sleepData" in filename and filename.endswith(".json"):
            filepath = os.path.join(data_folder, filename)

            with open(filepath, "r") as f:
                try:
                    records = json.load(f)

                    # Check if there are any records 
                    if isinstance(records, list):
                        sleep_records.extend(records)
                    
                    # If one record (dict)
                    elif isinstance(records, dict):
                        sleep_records.append(records)
                except Exception as e:
                    print("Skipping {filename}: {e}")

    # To pd DataFrame
    #sleep_df = pd.DataFrame(sleep_records)
    sleep_df = pd.json_normalize(sleep_records, sep="_")


    # Define which columns should be datetimes
    date_columns = [
        "sleepStartTimestampGMT",
        "sleepEndTimestampGMT",
        "calendarDate",
        "spo2SleepSummary_sleepMeasurementStartGMT",
        "spo2SleepSummary_sleepMeasurementEndGMT"
    ]

    # Convert them to datetime, safely (errors="coerce" makes invalid dates into NaT)
    for col in date_columns:
        if col in sleep_df.columns:
            sleep_df[col] = pd.to_datetime(sleep_df[col], errors="coerce")

    # Sort by date
    sleep_df = sleep_df[sleep_df["calendarDate"].notna()]
    sleep_df = sleep_df.sort_values("calendarDate")

    return sleep_df

if __name__ == "__main__":
    df = load_sleep_data()
    print("Sleep data combined!")
    print(df.head())

    # Save to SILVER folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_dir, "..", "data", "SILVER", "sleep_data.csv")
    df.to_csv(output_path, index=False)
    print("Saved data to SILVER!")


