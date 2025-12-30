#!/usr/bin/env python3

import getpass
import sys
try:
    from passlib.hash import md5_crypt
except ModuleNotFoundError:
    print("Passlib module not found, you need to install it!")
    sys.exit(1)

try:
    password = getpass.getpass(prompt="Enter the password to hash: ")
    confirm_password = getpass.getpass(prompt="Confirm password: ")
except KeyboardInterrupt:
    print("\nOperation cancelled.")
    sys.exit(0)

if password != confirm_password:
    print("Error: Passwords do not match.")
    sys.exit(1)

if not password:
    print("Error: Password cannot be empty.")
    sys.exit(1)


print(f"Cisco Type 5 Hash: {md5_crypt.hash(password)}")