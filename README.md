GitHub Activity CLI

A simple command-line tool to fetch and display recent public activity of any GitHub user.

🚀 Features
Fetches latest GitHub activity
Supports multiple event types:
Push (commits)
Issues (opened)
Stars
Clean, readable CLI output
No external dependencies (uses standard library)
📦 Installation
1. Clone the repository
git clone https://github.com/your-username/github-activity.git
cd github-activity
2. Install the package
pip install .

If that fails, make sure you have pyproject.toml in the root directory.

⚙️ Usage

Run the CLI with a GitHub username:

github-activity <username>
Example:
github-activity kamranahmedse
Output:
- Pushed 3 commits to user/repo
- Opened a new issue in user/repo
- Starred user/repo
🧠 How it works

Uses GitHub public API:

https://api.github.com/users/<username>/events
Parses event data and prints formatted output
Handles missing fields safely using .get() to avoid crashes
❗ Error Handling

The tool handles:

Invalid username → User not found
Network issues → Failed to connect
Empty activity → No recent activity found
🛠️ Development
Run locally without installing:
python main.py <username>
Entry point (CLI binding):

Defined in pyproject.toml

[project.scripts]
github-activity = "main:cli"
⚠️ Notes
Only shows latest 5 events
Works with public GitHub activity only
Different users may have different event types

https://roadmap.sh/projects/github-user-activity
