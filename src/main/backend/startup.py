import os
import redis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

DEFAULT_ADMIN = os.getenv("DEFAULT_ADMIN_USER", "admin")
DEFAULT_ADMIN_PASSWORD = os.getenv("DEFAULT_ADMIN_PASSWORD", "admin")

redis_user_db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=1) # Redis DB for user

# insert default user

if not redis_user_db.get(DEFAULT_ADMIN):
    redis_user_db.set(DEFAULT_ADMIN, DEFAULT_ADMIN_PASSWORD)
    print(f"Default user {DEFAULT_ADMIN} created with password {DEFAULT_ADMIN_PASSWORD}")
else:
    print(f"Default user {DEFAULT_ADMIN} already exists")

print("Startup completed")