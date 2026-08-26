correct_username = "phillip"
correct_pin = "1234"

attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    print("Login attempt: ", attempt, "of", max_attempts)
    
    username = input("Enter Username: ")
    username = username.strip().lower()

    pin = input("Enter PIN: ")

    if correct_username == username and correct_pin == pin:
        print("Access Granted")
        break
    elif correct_username == username:
        print("Invalid PIN")
    else:
        print("Unknown User")
    
    attempt += 1

else:
    print("Max attempts reached. Access Denied")
