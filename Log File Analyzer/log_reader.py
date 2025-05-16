import re

file_name = input("Enter the log file name: ")

info_count = 0
error_count = 0
warning_count = 0

try:
    with open(file_name, "r") as file: #open the file in read mode
        for line in file:
            if re.search(r"\bINFO\b", line): #search for the word INFO \b on both sides bind the word
                info_count += 1
            elif re.search(r"\bERROR\b", line):
                error_count += 1
            elif re.search(r"\bWARNING\b", line):
                warning_count += 1

        print(f"INFO: {info_count}")
        print(f"ERROR: {error_count}")
        print(f"WARNING: {warning_count}")
        print("Log file analysis complete.")
        file.close()

except FileNotFoundError:
    print(f"File {file_name} not found.")
    exit(1)
