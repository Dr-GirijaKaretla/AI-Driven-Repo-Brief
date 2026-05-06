import os
import time
import subprocess

REPO_PATH = os.path.dirname(os.path.dirname(__file__))   # AI-Driven-Repo-Brief/
CHECK_INTERVAL = 5  # seconds

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def has_changes():
    status = run_cmd(f"cd {REPO_PATH} && git status --porcelain")
    return status != ""

def auto_commit_push():
    print("🔄 Changes detected — committing and pushing...")
    run_cmd(f"cd {REPO_PATH} && git add .")
    run_cmd(f'cd {REPO_PATH} && git commit -m "Auto-sync update"')
    run_cmd(f"cd {REPO_PATH} && git push origin main")
    print("✅ Auto-sync complete!")

def main():
    print("🚀 Auto Git Sync started. Watching for changes...")
    while True:
        if has_changes():
            auto_commit_push()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
