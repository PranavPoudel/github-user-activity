import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="fetch github activity")
    parser.add_argument("username",help = "the github username")
    args = parser.parse_args()
    url =f"https://api.github.com/users/{args.username}/events"
    response = requests.get(url)
    events = response.json()
    # if no events found
    if not events:
        print("no events found")
        return
    for event in events:
        event_type = event ["type"]
        repo = event ["repo"]
        repo_name = repo["name"]
        payload = event.get("payload",{})

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


if __name__ == "__main__":
    main()
