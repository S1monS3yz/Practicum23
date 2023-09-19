"""_summary_"""
import csv
import six

file_location = r"C:\Users\beede\OneDrive\Desktop\Py Projects\scripts\csv_script1.py"

# Names to be removed
names_to_remove = ["Benham", "Arash"]

# Create an empty list for filtered rows
filtered_rows = []


# Define a function to open file with Python 2/3 compatibility
def open_file(mode):
    return six.moves.open(file_location, mode, newline="")


# Read the CSV file and filter rows
with open_file("r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Verify if the first name should be removed
        if row["firstName"] not in names_to_remove:
            filtered_rows.append(row)

# Write the filtered data back to CSV file
with open_file("w") as file:
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(filtered_rows)

print("Rows containing first names 'Benham' and 'Arash' removed")
print("CSV file saved")
