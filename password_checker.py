password = input("Enter your password: ")

# List of common/leaked passwords
common_passwords = ["password", "12345678", "1234567890", "password123", "admin123", "123123" , "112233"]

if password.lower() in common_passwords:
    print("Weak password ❌ (This is a commonly leaked password!)")
else:
    has_length = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_symbol = any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password)

    score = sum([has_length, has_digit, has_upper, has_symbol])

    if score == 4:
        print("Strong password ✅")
    elif score >= 2:
        print("Medium password ⚠️")
    else:
        print("Weak password ❌")