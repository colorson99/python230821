import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.search(pattern, email) is not None

# Test the function with various email addresses
email_addresses = [
    "user@example.com",
    "john.doe123@gmail.com",
    "invalid_email",
    "missing@tld.",
]

for email in email_addresses:
    if is_valid_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
