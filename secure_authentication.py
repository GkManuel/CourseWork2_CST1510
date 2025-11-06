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
    return hashed_password

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
    with open(user_data_files, 'r') as f:
        for line in f:
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
    with open("users.txt", "a") as f:
        f.write(f"{username}, {hashed_password}\n")
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

    with open("users.txt", 'r') as f:
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
    return

def validate_username(username):
    """ Validates username format
    Args:
        username (str): username to validate
    Returns:
        a valid message if the username is in the right format else gives an error message
    """

