import subprocess
from datetime import datetime

def run_command(command):
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT).decode('utf-8').strip()
        return result
    except subprocess.CalledProcessError as e:
        return f"Қате: {e.output.decode('utf-8').strip()}"

def get_git_commit_hash():
    return run_command(['git', 'rev-parse', 'HEAD'])

def get_git_commit_date():
    return run_command(['git', 'log', '-1', '--format=%cd'])

def save_build_info():
    commit_hash = get_git_commit_hash()
    commit_date = get_git_commit_date()
    build_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    filename = "PJ11_gitinfo_09.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Студент №9\n")
        file.write(f"Commit hash: {commit_hash}\n")
        file.write(f"Commit date: {commit_date}\n")
        file.write(f"Build time: {build_time}\n")

    print(f"{filename} файлы жаңартылды.")
    return build_time 

def push_to_github(build_time):
    print("GitHub-қа жіберу басталды...")
    commit_message = f"Автоматтық build info жаңартуы: {build_time}"
    print(run_command(['git', 'add', '.']))
    print(run_command(['git', 'commit', '-m', commit_message]))
    print(run_command(['git', 'push', 'origin', 'main']))

if __name__ == "__main__":
    build_time = save_build_info()
    push_to_github(build_time)
import subprocess
from datetime import datetime

def run_command(command):
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT).decode('utf-8').strip()
        return result
    except subprocess.CalledProcessError as e:
        return f"Қате: {e.output.decode('utf-8').strip()}"

def get_git_commit_hash():
    return run_command(['git', 'rev-parse', 'HEAD'])

def get_git_commit_date():
    return run_command(['git', 'log', '-1', '--format=%cd'])

def save_build_info():
    commit_hash = get_git_commit_hash()
    commit_date = get_git_commit_date()
    build_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    filename = "PJ11_gitinfo_09.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Студент №9\n")
        file.write(f"Commit hash: {commit_hash}\n")
        file.write(f"Commit date: {commit_date}\n")
        file.write(f"Build time: {build_time}\n")

    print(f"{filename} файлы жаңартылды.")
    return build_time 

def push_to_github(build_time):
    print("GitHub-қа жіберу басталды...")
    commit_message = f"Автоматтық build info жаңартуы: {build_time}"
    print(run_command(['git', 'add', '.']))
    print(run_command(['git', 'commit', '-m', commit_message]))
    print(run_command(['git', 'push', 'origin', 'main']))

if __name__ == "__main__":
    build_time = save_build_info()
    push_to_github(build_time)
