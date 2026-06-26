import requests
import argparse

def main():
    #taking an argument from the command line

    parser = argparse.ArgumentParser(description="fetch github activity")
    #naming the first argument as username
    parser.add_argument("username",help = "the github username")
    args = parser.parse_args()
    # url for the user's api from github
    url =f"https://api.github.com/users/{args.username}/events"
    #making a get request
    response = requests.get(url)
    # checking if the response is ok or not
    if response.status_code !=200:
        print(f"User not found : {response.status_code}")
        return
    #parsing the response to json and assigning to events
    events = response.json()
    # if no events found
    if not events:
        print("no events found")
        return
    #for each json component in events, categorizing their name and type and payload
    for event in events:
        event_type = event ["type"]
        repo = event ["repo"]
        repo_name = repo["name"]
        payload = event.get("payload",{})

# displaying the type of interation 
        if event_type == "PushEvent":
            commit_count = len(payload.get("commits",[]))
            print(f"-Pushed {commit_count} commits to {repo_name}")
        elif event_type == "IssuesEvent":
            action = payload.get("action")
            print(f" - {action.capitalize()} an issue in {repo_name}")
        elif event_type == "WatchEvent":
            print(f"- Starred {repo_name}")
        elif event_type =="ForkEvent":
            print(f"- Forked {repo_name}")
        else:
            clean_type = event_type.replace("Event","")
            print(f"- Performed {clean_type} in {repo_name}")

#magic variable to make standalone
if __name__ == "__main__":
    main()
