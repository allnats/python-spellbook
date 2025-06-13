"""Playing with regex in Python."""

def is_phone_number_basic(phone_number: str) -> bool:
    """Check if the passed string is a phone number without regex."""
    # Validate if the passed string argument is exactly 12 characters.
    if len(phone_number) != 12:
        return False

    # Validate if the first three characters are decimal.
    for i in range(0, 3):
        if not phone_number[i].isdecimal():
            return False

    if phone_number[3] != "-":
        return False

    for i in range(4, 7):
        if not phone_number[i].isdecimal():
            return False

    if phone_number[7] != "-":
        return False

    for i in range(8, 12):
        if not phone_number[i].isdecimal():
            return False

    return True


def number_in_message_basic(message: str) -> None:
    for i in range(len(message)):
        chunk: str = message[i:i + 12]
        if is_phone_number_basic(chunk):
            print(f"Phone number found: {chunk}")

    print("Done")

number1: str = "415-555-4242"
string1: str = "Moshi Moshi"
print(f"Is {number1} a phone number? {is_phone_number_basic(number1)}")
print(f"Is {string1} a phone number? {is_phone_number_basic(string1)}")

message: str = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."

number_in_message_basic(message)
