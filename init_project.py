import os

project_structure = {
    "leetcode": ["__init__.py", "fetcher.py", "solver.py", "submitter.py", "utils.py"],
    "github": ["__init__.py", "updater.py"],
    "solutions": [],
}

base_files = ["main.py", "config.yaml", "requirements.txt", "README.md", ".gitignore"]

def create_structure():
    for folder, files in project_structure.items():
        os.makedirs(folder, exist_ok=True)
        for file in files:
            open(os.path.join(folder, file), "w").close()

    for file in base_files:
        with open(file, "w") as f:
            if file == "README.md":
                f.write("# 🤖 LeetCode Bot\n\nAutomates solving, submitting, and syncing LeetCode problems with GitHub.\n")
            elif file == "requirements.txt":
                f.write("requests\npyyaml\ngitpython\nbeautifulsoup4\nplaywright\nPyGithub\n")
            elif file == "config.yaml":
                f.write("leetcode:\n  username: YOUR_USERNAME\n  password: YOUR_PASSWORD\n\ngithub:\n  token: YOUR_GITHUB_TOKEN\n  repo: YOUR_USERNAME/leetcode-bot\n")
            elif file == ".gitignore":
                f.write("__pycache__/\n.env\n*.log\n")
            else:
                f.write("")  # Empty for now

if __name__ == "__main__":
    create_structure()
    print("✅ LeetCode bot structure ready.")
