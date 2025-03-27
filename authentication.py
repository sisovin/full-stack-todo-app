import jwt
import argon2
import redis
from datetime import datetime, timedelta

class UserAuthentication:
    def __init__(self):
        self.ph = argon2.PasswordHasher()
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.jwt_secret = 'your_jwt_secret_key'

    def signup(self, username, password):
        hashed_password = self.ph.hash(password)
        # Store the username and hashed password in the database
        # This is a placeholder, replace with actual database code
        # database.signup_user(username, hashed_password)
        return "Signup successful!"

    def login(self, username, password):
        # Retrieve the hashed password from the database
        # This is a placeholder, replace with actual database code
        # result = database.login_user(username)
        result = None  # Placeholder
        if result and self.ph.verify(result[0], password):
            token = jwt.encode({'username': username, 'exp': datetime.utcnow() + timedelta(hours=1)}, self.jwt_secret, algorithm='HS256')
            self.redis_client.set(token, username)
            return f"Login successful! Token: {token}"
        else:
            return "Invalid username or password"

    def generate_jwt(self, username):
        token = jwt.encode({'username': username, 'exp': datetime.utcnow() + timedelta(hours=1)}, self.jwt_secret, algorithm='HS256')
        return token

    def verify_jwt(self, token):
        try:
            decoded = jwt.decode(token, self.jwt_secret, algorithms=['HS256'])
            return decoded['username']
        except jwt.ExpiredSignatureError:
            return "Token has expired"
        except jwt.InvalidTokenError:
            return "Invalid token"

    def hash_password(self, password):
        return self.ph.hash(password)

    def verify_password(self, hashed_password, password):
        try:
            return self.ph.verify(hashed_password, password)
        except argon2.exceptions.VerifyMismatchError:
            return False

    def set_cache(self, key, value):
        self.redis_client.set(key, value)

    def get_cache(self, key):
        return self.redis_client.get(key)
