import os
import json
import pandas as pd
import matplotlib.pyplot as plt


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


df = pd.read_csv(r"/Users/ernakuginyte/Desktop/Project/Garmin_Explore/data/SILVER/sleep_data.csv")

# Sleep Stages Duration Plot
sleep_stages = df[["calendarDate", "deepSleepSeconds", "lightSleepSeconds", "remSleepSeconds", "awakeSleepSeconds"]].copy()

# Convert seconds → hours
for col in ["deepSleepSeconds", "lightSleepSeconds", "remSleepSeconds", "awakeSleepSeconds"]:
    sleep_stages[col] = sleep_stages[col] / 3600

sleep_stages.set_index("calendarDate", inplace=True)

plt.figure(figsize=(12,6))
sleep_stages.plot(kind="bar", stacked=True, figsize=(14,7), colormap="viridis", alpha=0.9)
plt.ylabel("Hours")
plt.title("Sleep Stages Breakdown by Night", fontsize=16)
plt.legend(title="Stage")
plt.tight_layout()
plt.show()

# Sleep Scores Trend
plt.figure(figsize=(14,7))
plt.plot(df["calendarDate"], df["sleepScores_overallScore"], marker="o", label="Overall Score", linewidth=2, color="black")
plt.plot(df["calendarDate"], df["sleepScores_qualityScore"], marker="s", label="Quality Score", alpha=0.8)
plt.plot(df["calendarDate"], df["sleepScores_durationScore"], marker="^", label="Duration Score", alpha=0.8)
plt.plot(df["calendarDate"], df["sleepScores_recoveryScore"], marker="d", label="Recovery Score", alpha=0.8)

plt.title("Sleep Scores Trend", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Score")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()