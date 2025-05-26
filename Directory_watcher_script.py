import os
import time

folder_name = input("Enter the folder name to watch: ").strip()

if not os.path.isdir(folder_name):
    print(f"The folder '{folder_name}' does not exist.")

    exit()

if os.path.isdir(folder_name):
    print(f"Watching the folder: {folder_name}")

    before = set(os.listdir(folder_name))
    while True:
        time.sleep(5) # Check every 5 seconds
        after = set(os.listdir(folder_name))

        added = after - before
        removed = before - after

        if added:
            print(f"Added: {added}")
        if removed:
            print(f"Removed: {removed}")

        before = after
