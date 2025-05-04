import os
import subprocess
import random
import string

# Configuration
REPO_NAME = "shiny-octo-giggle"  # Replace with your repository name
CO_AUTHOR = "ScriptXeno <noktisorg@gmail.com>"  # Replace with co-author details
CO_AUTHOR_ME = "OCEANOFANYTHING <work.oceanofanything@gmail.com>"  # Replace with co-author details

# Function to run shell commands
def run_command(command):
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(f"Output: {result.stdout}")
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        raise Exception(f"Command failed: {command}")
    return result.stdout

# Step 1: Create a new branch
def create_branch(branch_name):
    print(f"Creating branch: {branch_name}")
    run_command(f"git checkout -b {branch_name}")

# Step 2: Make changes to a text file
def make_changes(file_path, content):
    print(f"Making changes to {file_path}")
    with open(file_path, "w") as f:
        f.write(content)

# Step 3: Commit changes with co-author
def commit_changes(commit_message):
    print("Committing changes")
    co_author_trailer = f"Co-authored-by: {CO_AUTHOR}"
    co_author_me_trailer = f"Co-authored-by: {CO_AUTHOR_ME}"
    full_commit_message = f"{commit_message}\n\n{co_author_trailer}\n{co_author_me_trailer}"
    run_command(f"git add .")
    run_command(f"git commit -m \"{full_commit_message}\"")

# Step 4: Push branch to remote
def push_branch(branch_name):
    print(f"Pushing branch: {branch_name}")
    run_command(f"git push origin {branch_name}")

# Step 5: Create a pull request
def create_pull_request(branch_name, title, body):
    print(f"Creating pull request for branch: {branch_name}")
    run_command(f"gh pr create --title \"{title}\" --body \"{body}\" --head {branch_name} --base main")

# Function to generate a random but meaningful branch name
def generate_branch_name():
    adjectives = ["quick", "bright", "happy", "bold", "calm"]
    nouns = ["fox", "tree", "river", "cloud", "stone"]
    return f"{random.choice(adjectives)}-{random.choice(nouns)}-{random.randint(1, 100)}"

# Function to generate random content for the file
def generate_random_content():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=20))

# Main bot logic
def main():
    num_pull_requests = int(input("Enter the number of pull requests to create: "))
    file_path = "file.txt"  # File to modify
    pr_title_template = "Update file.txt with random content"
    pr_body_template = "This pull request updates file.txt with random content."

    for _ in range(num_pull_requests):
        branch_name = generate_branch_name()
        commit_message = f"Update {file_path} with random content"

        # Execute steps
        create_branch(branch_name)
        make_changes(file_path, generate_random_content())
        commit_changes(commit_message)
        push_branch(branch_name)
        create_pull_request(branch_name, pr_title_template, pr_body_template)

if __name__ == "__main__":
    main()