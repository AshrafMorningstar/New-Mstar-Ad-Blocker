import os
import random
import subprocess
from datetime import datetime, timedelta

def git_commit(message, commit_date):
    # Stage the changes
    subprocess.run(['git', 'add', 'info.txt'])
    
    # Create commit with specified date
    env = os.environ.copy()
    env['GIT_COMMITTER_DATE'] = commit_date.strftime('%Y-%m-%dT%H:%M:%S')
    subprocess.run(['git', 'commit', '-m', message, '--date', commit_date.strftime('%Y-%m-%dT%H:%M:%S')], env=env)

def git_push():
    # Push the changes to the remote repository
    subprocess.run(['git', 'push'])

# Main function to create files for a range of dates
def fake_commits(start_date, end_date, min_commits, max_commits, skipping=False, max_skip_days=1):
    file_path = "info.txt"  # Single file at the script's level

    current_date = start_date
    while current_date <= end_date:
        # skip days randomly, if skiping is enabled
        if skipping and random.choice([True, False]):
            skip_days = random.randint(0, max_skip_days)
            print(f"\n\nSkipping {skip_days} days from {current_date.strftime('%d-%b-%Y')}")
            current_date += timedelta(days=skip_days)
            continue

        # Random number of commits for the current date
        n_commits = random.randint(min_commits, max_commits)
        print(f"\n\n{n_commits} commits for date: {current_date.strftime('%d-%b-%Y')}")

        with open(file_path, "a") as file:  # Append mode
            for i in range(1, n_commits + 1):
                info = f"Date: {current_date.strftime('%d-%b-%Y')}, Commit #: {i}"     
                with open(file_path, "w") as file:
                    file.write("")  # Clear the file if it exists
                    file.write(info)
                print(info)
                git_commit(info, current_date)

        # Move to the next day
        current_date += timedelta(days=1)
    
    # Push all the changes
    git_push()

# Set the date range
start_date = datetime(2024, 11, 9)
end_date = datetime(2025, 1, 12)

# Set the min and max number of commits per day
min_commits = 3
max_commits = 22

fake_commits(start_date, end_date, min_commits, max_commits, skipping=True, max_skip_days=1)