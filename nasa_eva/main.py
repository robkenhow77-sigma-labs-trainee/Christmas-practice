import requests

if __name__ == "__main__":
    response = requests.get("https://data.nasa.gov/resource/9kcy-zwvn.json")
    data = response.json()
