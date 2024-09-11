# PasswordManager

## Features
 - will be a CLI based app but it will have an attractive UI (rich will be used)
 - will have a secure login system where login passwords will be salted and peppered
 - user can save passwords for various apps which will be encrypted then stored in SQL db
 - encrypted passwords will be saved locally on the users system and the encryption key will be saved on the server for enhanced security
 - bonus idea: implement the ability to store passwords directly from the CSV file obtained from google password manager

## Basic Working
 - PasswordManager.py will manage CRUD operations (including encryption/decryption) of the users saved passwords
 - UserManager.py will handle the login system and will be responsible for salting/peppering of login passwords of new accounts
 - main.py will have the menu loop, will use PasswordManager, UserManager and rich to perform the required functions
 - the data will be stored in SQL database with 2 tables, one for passwords and other for users

## Concepts/Libraries To Be Used
1. cryptography for saving users passwords
2. hashlib for secure login system
3. sqlite3 for storing data
4. sockets to implement the server client idea
5. rich for the ui