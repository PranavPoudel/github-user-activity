import requests

def main():
    url ="https://api.github.com/users/pranavpoudel/events"
    response = requests.get(url)
    events = response.json()
    # if no events found
    if not events:
        print("no events found")
        return
    for event in events:
        print (event)

if __name__ == "__main__":
    main()
