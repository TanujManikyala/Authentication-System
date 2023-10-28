import secrets

def generate_secret_key():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(-_=+)'
    key = ''.join(secrets.choice(chars) for i in range(50))
    return key

print(generate_secret_key())
