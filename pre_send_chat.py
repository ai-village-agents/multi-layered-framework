import subprocess
import time

def ensure_push():
    try:
        subprocess.run(["git", "fetch", "--all"], check=True, cwd="/home/computeruse/multi-layered-framework")
        subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=True, cwd="/home/computeruse/multi-layered-framework")
        subprocess.run(["git", "push", "origin", "main"], check=True, cwd="/home/computeruse/multi-layered-framework")
        with open("/home/computeruse/multi-layered-framework/tmp_pre_chat", "w") as f:
            f.write(str(time.time()))
    except Exception as e:
        print(f"Error ensuring git push: {e}")

if __name__ == "__main__":
    ensure_push()
