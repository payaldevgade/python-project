# Bank Management System

A simple command-line/console-style bank account management system written in Python. Account data is persisted locally in a JSON file (`data.json`), so no external database is required.

## Features

- **Create Account** — Register a new customer with name, age, email, and a 5-digit PIN. A unique 10-character alphanumeric account number is auto-generated.
- **Login / Authentication** — Validate a user via account number + PIN.
- **Deposit** — Add funds to an account.
- **Withdraw** — Withdraw funds, with a balance check to prevent overdrafts.
- **Update Details** — Update a user's name and/or email.
- **Delete Account** — Permanently remove an account from the system.
- **Persistent Storage** — All account data is saved to and loaded from `data.json`.

## Requirements

- Python 3.x
- No external dependencies (uses only the standard library: `json`, `random`, `string`, `pathlib`)

## Project Structure

```
python-project/
├── bankmanagement.py     # Core Bank class and logic
├── filehandling project.py
├── streamlit.py
├── data.json              # Auto-created — stores account records
└── README.md
```

## How It Works

The core logic lives in the `Bank` class:

| Method | Description |
|---|---|
| `__init__()` | Loads existing accounts from `data.json` (creates an empty list if the file doesn't exist or is corrupted) |
| `save()` | Writes the current account data back to `data.json` |
| `generate_account()` | Generates a unique 10-character account number (uppercase letters + digits) |
| `create_account(name, age, email, pin)` | Creates a new account after validating age (18+), PIN (5 digits), and email uniqueness |
| `login(account, pin)` | Authenticates a user by account number and PIN |
| `deposit(account, pin, amount)` | Deposits a positive amount into an account |
| `withdraw(account, pin, amount)` | Withdraws funds if sufficient balance is available |
| `update_details(account, pin, name, email)` | Updates name and/or email for an authenticated user |
| `delete_account(account, pin)` | Deletes an authenticated user's account |

## Validation Rules

- **Age**: Must be 18 or older to open an account.
- **PIN**: Must be exactly 5 digits.
- **Email**: Must be unique across all accounts.
- **Amount**: Deposits and withdrawals must be greater than 0.
- **Withdrawal**: Cannot exceed the current account balance.

## Usage Example

```python
from bankmanagement import Bank

bank = Bank()

# Create a new account
success, result = bank.create_account("Payal Devgade", 22, "payal@example.com", "12345")
if success:
    print("Account created:", result)
else:
    print("Error:", result)

# Deposit money
account_number = result["Account Number"]
success, msg = bank.deposit(account_number, "12345", 5000)
print(msg)

# Withdraw money
success, msg = bank.withdraw(account_number, "12345", 1000)
print(msg)

# Update details
success, msg = bank.update_details(account_number, "12345", name="Payal D.", email=None)
print(msg)

# Delete account
success, msg = bank.delete_account(account_number, "12345")
print(msg)
```

## Data Storage Format

Account records are stored in `data.json` as a list of objects:

```json
[
    {
        "Name": "Payal Devgade",
        "Age": 22,
        "Email": "payal@example.com",
        "PIN": "12345",
        "Account Number": "A1B2C3D4E5",
        "Balance": 5000
    }
]
```

## Notes

- This project is intended for learning/demo purposes. PINs are stored in plain text in `data.json`, which is **not secure** for real-world use — consider hashing sensitive data before adapting this for production.
- The repository also includes `filehandling project.py` and `streamlit.py`, which may extend this project with a file-handling exercise and a Streamlit-based UI, respectively.

## License

No license specified.
