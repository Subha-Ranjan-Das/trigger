import os
import subprocess

def make_change():
    # Create or update the content in `sample_file.txt`
    with open("sample_file.txt", "a") as file:
        file.write("New line added to sample_file.txt\n")

    # Stage the file
    subprocess.run(["git", "add", "sample_file.txt"])

    # Commit the change
    commit_message = "Updated sample_file.txt"
    subprocess.run(["git", "commit", "-m", commit_message])

if __name__ == "__main__":
    make_change()
