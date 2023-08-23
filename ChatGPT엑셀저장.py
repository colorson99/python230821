import openpyxl
from datetime import datetime

# Create a new Excel workbook and select the active worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Set column headers
headers = ["Product Name", "Price", "Quantity", "Date of Sale"]
worksheet.append(headers)

# Sample sales data (replace this with your actual data)
sales_data = [
    ("Product A", 100, 5, "2023-08-01"),
    ("Product B", 150, 3, "2023-08-02"),
    # ... add more data here
]

# Write sales data to the worksheet
for sale in sales_data:
    worksheet.append(sale)

# Save the workbook to the specified path
file_path = "c:\\work\\sales.xlsx"
workbook.save(file_path)

print(f"Sales data saved to {file_path}")