import os

# Get user of system
user = os.getcwd().split('\\')[2]
disc = os.getcwd().split('\\')[0]

# dir default with user
folder_download = f"{disc}\\Users\\{user}\\Downloads"

print(folder_download)