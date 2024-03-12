import json
import pandas as pd
import matplotlib.pyplot as plt


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Funktion zur Datenanalyse
def analyze_data(data):
    # Umwandeln der Daten in ein Pandas DataFrame
    df = pd.DataFrame(data)
    # Gesamtanzahl der Datensätze
    total_records = len(df)
    print("Gesamtanzahl der Datensätze:", total_records)
    # Zeitrahmen der Datensätze
    start_time = pd.to_datetime(df['timestamp'].min(), unit='s')
    end_time = pd.to_datetime(df['timestamp'].max(), unit='s')
    print("Zeitrahmen der Datensätze:", start_time, "bis", end_time)
    # Statistische Zusammenfassung der Verbrauchswerte
    consumption_stats = df['consumption_kwh'].describe()
    print("\nStatistische Zusammenfassung der Verbrauchswerte:")
    print(consumption_stats)
    # Visualisierung des Stromverbrauchs über die Zeit
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df.set_index('timestamp', inplace=True)
    df['consumption_kwh'].plot(figsize=(10, 6))
    plt.title('Stromverbrauch über die Zeit')
    plt.xlabel('Zeit')
    plt.ylabel('Stromverbrauch (kWh)')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    json_file_path = "data.json"
    json_data = read_json_file(json_file_path)
    print(json_data)
