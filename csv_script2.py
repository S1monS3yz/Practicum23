import csv
import six
from datetime import datetime

# Display file location
file_location = r"C:\Users\beede\OneDrive\Desktop\Py Projects\scripts\csv_script2.py"

# Define the API integrations to check
api_integrations_to_remove = ["Benham", "Arash", "Fin"]

# Create an empty list to store filtered rows
filtered_rows = []


# Define a function to open file with Python 2/3 compatibility
def open_file(mode):
    return six.moves.open(file_location, mode, newline="")


# Read the CSV file and filter rows
with open_file("r") as file:
    reader = csv.DictReader(file)

    if "employees" in reader.fieldnames:
        api_key_column = "employees"
    else:
        api_key_column = None

    for row in reader:
        # Check if API key column exists & check if value is in list of integrations to remove
        if api_key_column and row[api_key_column] not in api_integrations_to_remove:
            # Check if start date is valid != ("00-00-0000")
            start_date = row.get("startDate", "")
            if start_date != "00-00-0000":
                filtered_rows.append(row)
        elif "firstName" in reader.fieldnames and "lastName" in reader.fieldnames:
            # If "employees" column does not exist; check 'firstName' 'lastName'
            full_name = row.get("firstName", "") + " " + row.get("lastName", "")
            if full_name.strip() not in api_integrations_to_remove:
                # Check if start date is valid != ("00-00-0000")
                start_date = row.get("startDate", "")
                if start_date != "00-00-0000":
                    filtered_rows.append(row)

# Write the filtered data back to the CSV file
with open_file("w") as file:
    fieldNames = reader.fieldnames
    writer = csv.DictWriter(file, fieldnames=fieldNames)

    writer.writeheader()
    writer.writerows(filtered_rows)

print("API integrations removed, invalid start dates filtered, CSV file saved.")
