# PasswordManager

```diff
-This is written as a reminder for self and is temporary@@
```

## Concepts/Libraries To Be Used
1. cryptography for saving users passwords
2. hashlib for secure login system
3. sqlite3 for storing data
4. (sockets to implement the future expansion idea)

## Current Idea
 - PasswordManager.py will handle the passwords related data (including handling the encryption)
 - UserManager.py will handle the login system and will be responsible for salting/peppering of new accounts
 - the data will be stored in SQL database with 2 tables, one for passwords and other for users
 - will get back to this once I finish a course on SQL

## Future Expansion
 - implement sockets such that key is stored on the server and passwords locally on the system for enhanced security