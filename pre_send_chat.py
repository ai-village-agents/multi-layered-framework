import subprocess
import os

def check_status():
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True, cwd='/home/computeruse/multi-layered-framework')
    if result.stdout.strip() != "":
        print("Git repository is not clean. Changes must be committed or stashed before sending messages to chat.")
        return False
    return True

if __name__ == '__main__':
    if check_status():
        print("READY")
    else:
        print("BLOCKED")
