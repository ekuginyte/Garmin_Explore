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
    sleep_df = pd.DataFrame(sleep_records)

    # Sort by date
    if "calendarDate" in sleep_df.columns:
        df = df.sort_values("calendarDate")

    return sleep_df

if __name__ == "__main__":
    df = load_sleep_data()
    print("Sleep data combined!")
    print(df.head())

    # Save to SILVER folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_dir, "..", "data", "SILVER", "sleep_data.xlsx")
    df.to_excel(output_path, index=False)
    print("Saved data to SILVER!")