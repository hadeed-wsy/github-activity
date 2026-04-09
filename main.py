import sys
import json
import urllib.request

def cli():
    if len(sys.argv) == 1:
        print ("please provide username:")
    elif len(sys.argv) > 2:
        print ("please write the correct input")
    else:
        cmd = sys.argv[1]
        url = f"https://api.github.com/users/{cmd}/events"
        try:
            response = urllib.request.urlopen(url)
            data = response.read()
            data_str = data.decode("utf-8")
            data = json.loads(data_str)
            if not data:
                print("No recent activity found")
            else:
                for event in data[:5]:
                    event_type = event.get("type")
                    payload = event.get("payload", {})
                    repo = event.get("repo", {}).get("name", "unknown")

                    if event_type == "PushEvent":
                        commits = len(payload.get("commits", [])) 
                        print(f"- Pushed {commits} commits to {repo}")

                    elif event_type == "IssuesEvent":
                        if payload.get("action") == "opened":
                            print(f"- Opened a new issue in {repo}")

                    elif event_type == "WatchEvent":
                        print(f"- Starred {repo}")

                    else:
                        print(f"- {event_type} in {repo}")

        except urllib.error.HTTPError as e:
            if e.code == 404:
                 print("User not found")
            else:
                 print("HTTP error:", e.code)
        except urllib.error.URLError:
            print("Failed to connect to GitHub API")
        except json.JSONDecodeError:
            print("Error parsing response")
        
if __name__ == "__main__":
    cli()
        