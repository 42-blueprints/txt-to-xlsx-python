import re
import phonenumbers
from email_validator import validate_email, EmailNotValidError

def is_phone_number(text):
    try:
        if not text.isdigit():
            return False
        if len(text) < 6:
            return False
    except phonenumbers.phonenumberutil.NumberParseException:
        return ""
    return True

def is_email(text):
    try:
        #validate_email(text)
        if "@" not in text:
            return False
        return True
    except EmailNotValidError:
        return False

def is_name(text):
    pattern = re.compile(r"^[A-Za-z]+(?:\s[A-Za-z]+)*$")
    return bool(pattern.match(text))

def is_cuantia(text):
    return "income" in text.lower()
