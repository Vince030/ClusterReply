import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Datenanalyse
def analyze_data(data):
    df = pd.DataFrame(data)

    # Gesamtanzahl Datensätze
    total_records = len(df)
    print("Gesamtanzahl der Datensätze:", total_records)

    # Zeitrahmen
    start_time = pd.to_datetime(df['timestamp'].min(), unit='s')
    end_time = pd.to_datetime(df['timestamp'].max(), unit='s')
    print("Zeitrahmen der Datensätze:", start_time, "bis", end_time)

    # Statistische Zusammenfassung
    consumption_stats = df['consumption_kwh'].describe()
    median = df['consumption_kwh'].median()
    print("\nStatistische Zusammenfassung der Verbrauchswerte:")
    print(consumption_stats)
    print("\nMedian des Verbrauchswerts:", median)

    # Visualisierung des Stromverbrauchs über die Zeit
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df.set_index('timestamp', inplace=True)
    df['consumption_kwh'].plot(figsize=(10, 6))
    plt.title('Stromverbrauch über die Zeit der Maschine 123')
    plt.xlabel('Zeit')
    plt.gca().xaxis.set_major_formatter(
        mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.ylabel('Stromverbrauch (kWh)')
    plt.grid(True)
    plt.show()

    return df


if __name__ == "__main__":
    json_file_path = "data.json"
    json_data = read_json_file(json_file_path)
    df = analyze_data(json_data)
