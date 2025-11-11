import os
import bcrypt
import re
user_data_files = "users.txt"
# Function to hash a password
def hash_password(plain_text_password):
    """Hashes a password using bcrypt, with automatic salt generation
    Args:
        plain_text_password (str): Plain text password to hash
    Returns:
        str: Hashed password
        """
    # Encode the password to bytes, required by bcrypt
    password_bytes = plain_text_password.encode('utf-8')
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password.decode("utf-8")

# Function to verify a password
def verify_password(plain_password, hashed_password):
    """Verifies a plaintext password against a stored bcrypt hash
    Args:
        plain_password (str): Plain text password to verify
        hashed_password (str): The stored hash to check against
    Returns:
        True if the password matches, False otherwise
        """
    # Encoding both plain text and stored hash to bytes
    password_bytes = plain_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    # bcrypt.checkpw handles extracting the salt and comparing
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)

# Function to check if the username exists in the database
def user_exists(username):
    """Checks if username already exists in the database
    Args:
        username (str): Username to check
    Returns:
        True if the username already exists, False otherwise
        """
    # Case when the file doesn't exist yet
    if not os.path.exists(user_data_files):
        return False
    # Reading the file and checking each line if username exists
    with open(user_data_files, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            stored_username, stored_hash=line.split(',', 1)
            if stored_username == username:
                return True
    return False

# Function to register user
def register(username, password):
    """Registers a new user with a given username, hashes their password and stores everything in the database
    Args:
        username (str): Username to register
        password (str): Password to hash and store
    Returns:
        True if registration was successful, False if username already exists
    """
    # Checking if username exists
    if user_exists(username):
        print(f"Username: {username} already exists")
        return False

    # Hashing the password
    hashed_password = hash_password(password)

    # Writing username and hashed password into file
    with open(user_data_files, "a", encoding="utf-8") as f:
        f.write(f"{username},{hashed_password}\n")
    print(f"User {username} registered successfully")
    return True

# Login function
def login_user(username, password):
    """Authenticates a user by verifying their username and password
    Args:
        username (str): username to authenticate
        password (str): plain text password to verify
    Returns true if authentication was successful, false otherwise
    """

    #Case when no user is registered yet
    if not os.path.exists(user_data_files):
        print("No user registered yet")
        return False

    with open(user_data_files, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            if not line:
                continue
            stored_username, stored_hash = line.strip().split(',',1)
            #if username matches then verify password
            if stored_username == username:
                if verify_password(password,stored_hash):
                    print(f"Welcome {username}")
                    return True
                else:
                    print("Invalid password")
                    return False
    print("Username not found")
    return False

def validate_username(username):
    """ Validates username format
    Args:
        username (str): username to validate
    Returns:
        tuple: (bool, str)- (is_valid, error_msg)
    """
    if not (3<=len(username)<=20):
        return False, "Username must be 3-20 characters long"
    if  not re.fullmatch(r"[A-Za-z0-9]+", username):
        return False, "Username must only contain alphanumeric characters"
    return True,""

def validate_password(password):
    """ Validates password strength
    Args:
        password (str): plain text password to validate
    Returns:
        tuple: (bool, str)- (is_valid, error_msg)
    """
    if not (8<=len(password)<=50):
        return False, "Password must be 8-50 characters long"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain atleast one uppercase character"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain atleast one lowercase character"
    if not re.search(r"[0-9]", password):
        return False, "Password must contain atleast one numeric character"
    return True, ""

def display_menu():
    """Displays the menu options"""
    print("\n" + "="*50)
    print("  MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print("  Secure Authentication System")
    print("="*50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-"*50)

def main():
    """Main program loop"""
    while True:
        display_menu()
        choice = input("\nPlease select an option(1-3): ").strip()
        if choice == "1":

            # Registration flow
            print("\n--USER REGISTRATION--")
            username = input("Enter a username: ").strip()

            # Validate username
            is_valid, error_msg = validate_username(username)
            if not is_valid:
                print(f"Error:{error_msg}")
                continue
            password = input("Enter a password: ").strip()
            is_valid, error_msg = validate_password(password)
            if not is_valid:
                print(f"Error:{error_msg}")
                continue

            # Confirm password
            password_confirm = input("Confirm password: ").strip()
            if password_confirm != password:
                print("Error: Password do not match")
                continue

            # Register user
            register(username, password)

        elif choice == "2":
            # Login flow
            print("\n--USER LOGIN--")
            username = input("Enter a username: ").strip()
            password = input("Enter a password: ").strip()
            # Attempt login
            if login_user(username, password):
                print(f"\n Welcome: {username}")
                print("\n You're now logged in")
                input("Press enter to return to main menu")

        elif choice == "3":
            print("\nThank you for using authentication system")
            print("Exiting...")
            break
        else:
            print("Invalid option, Please select 1, 2, or 3")

if __name__ == "__main__":
    main()