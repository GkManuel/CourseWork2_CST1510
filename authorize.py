import bcrypt

def hash_password(plain_text_password):
    # Encode the password to bytes, required by bcrypt
    pass_bytes = plain_text_password.encode('utf-8')
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(pass_bytes, salt)
    return hashed_pass

passwd = "secret"
pass_hash = hash_password(passwd)
print(f"Password: {passwd} Hash: {str(pass_hash)}")