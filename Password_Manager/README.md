#  Password Manager (Python)

A simple password manager built in Python using **cryptography.Fernet** for encryption.  
It allows you to securely store, retrieve, and manage passwords with a master password.

---

##  Features
- Set and verify a **master password** (stored as a key file)
- Encrypt and save passwords in `password.json`
- View saved sites
- Retrieve and decrypt stored passwords
- Simple menu-driven interface

---

##  Usage
1. Install dependencies:
   ```bash
   pip install cryptography

 - - Run the script
   python password_manager.py
--First run → set a master password.

--Use the menu:
  1 - Add password
  2 - View sites
  3 - Get password
  4 - Exit

# Example
-----password manager-----
1-Add password:
2-View Sites:
3-Get password:
4-Exit
choice: 1
website: github.com
Username: anshu
Password: mySecret123
password saved..


