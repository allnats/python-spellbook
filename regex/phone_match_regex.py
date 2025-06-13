"""Playing with regex in Python."""

from re import compile
"""
compile returns a 'Regex' object

"""

def is_phone_number(phone_number: str) -> bool:
    """Check if the passed string is a phone number using regex."""
    return True


def number_in_message(message: str) -> None:
    """Check if a number exists in the passed message."""
    regex_phone_num = compile(r"\d{3}-\d{3}-\d{4}")
    match_object = regex_phone_num.search(message)
    print(f"Phone number found: {match_object.group()}")


# number1: str = "415-555-4242"
# string1: str = "Moshi Moshi"
# print(f"Is {number1} a phone number? {is_phone_number(number1)}")
# print(f"Is {string1} a phone number? {is_phone_number(string1)}")

message: str = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."

number_in_message(message)
