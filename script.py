import subprocess
import os


# Example 1: Run a simple command
# result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, text=True)
# print(result.stdout)

# Example 1: Run a simple command
# Use 'dir' instead of 'ls' on Windows
subprocess.run("git add .", shell=True, stdout=subprocess.PIPE, text=True)

        # commit_message = f'Automated commit - {datetime.now()}'
        
        # Commit the changes with the generated commit message
subprocess.run(f"git commit -m 'w", shell=True, stdout=subprocess.PIPE, text=True)
# Print the output
# print(result.stdout)

# Example 2: Run a command with user input
# user_input = input("Enter a command: ")
# result = subprocess.run(user_input, shell=True, stdout=subprocess.PIPE, text=True)
# print(result.stdout)
