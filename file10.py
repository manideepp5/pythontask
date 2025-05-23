import re

def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

print(valid_email("test@example.com"))
