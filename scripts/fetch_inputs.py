import requests

def fetch_input(day, session_cookie):
    url = f"https://adventofcode.com/2024/day/{day}/input"
    headers = {"Cookie": f"session={session_cookie}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(f"input/day{day:02}.txt", "w") as f:
            f.write(response.text.strip())
    else:
        print(f"Error fetching input for day {day}: {response.status_code}")
