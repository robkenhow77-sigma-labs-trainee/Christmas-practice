import requests
from datetime import datetime, timedelta


def get_total_duration(data: list[dict]) -> float:
    """Gets the total time of events in hours."""
    total_duration = timedelta()
    for entry in data:
        duration = datetime.strptime(entry.get('duration', "00:00"), '%H:%M')
        total_duration += timedelta(hours=duration.hour, minutes=duration.minute)
    return int(round(total_duration.total_seconds() / 3600, 0))


def get_number_of_events_by_country(data: list[dict]) -> dict:
    """Gets the total number of events for each country."""
    countries = {}
    for entry in data:
        country = entry.get('country', "N/A")
        if country in countries.keys():
            countries[country] += 1
        else:
            countries[country] = 1
    return countries


def get_events_by_country(data: list[dict]) -> dict:
    """Gets all event entries for each country."""
    countries = {}
    for entry in data:
        country = entry.get('country', "N/A")
        if country in countries.keys():
            countries[country].append(entry)
        else:
            countries[country] = []
    return countries


if __name__ == "__main__":
    response = requests.get("https://data.nasa.gov/resource/9kcy-zwvn.json")
    data = response.json()
    usa_total_time = get_total_duration(get_events_by_country(data)['USA'])
    russia_total_time = get_total_duration(get_events_by_country(data)['Russia'])
    print(usa_total_time)
    print(russia_total_time)
