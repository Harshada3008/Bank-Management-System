# 🏦 Bank Management System
<img width="1501" height="899" alt="Screenshot 2026-05-15 214525" src="https://github.com/user-attachments/assets/5b0afc4f-ad62-4140-8770-28e4ed6bf6f0" />
<img width="1608" height="942" alt="Screenshot 2026-05-15 214712" src="https://github.com/user-attachments/assets/015d7832-5246-498c-968e-457903b5666d" />
<img width="1497" height="877" alt="Screenshot 2026-05-15 214812" src="https://github.com/user-attachments/assets/59a17f6d-c030-4d0f-9b3b-b30abdd2b79c" />
<img width="1526" height="820" alt="Screenshot 2026-05-15 215010" src="https://github.com/user-attachments/assets/4d420362-c3c2-47fb-9a72-86d426da5f8d" />
<img width="1502" height="903" alt="Screenshot 2026-05-15 215057" src="https://github.com/user-attachments/assets/ec358915-dcf7-49c7-83d4-e17292ce48b6" />
<img width="1537" height="927" alt="Screenshot 2026-05-15 215129" src="https://github.com/user-attachments/assets/c462c1fa-730b-4e84-bdcb-128f06fbc32c" />
<img width="1495" height="980" alt="Screenshot 2026-05-15 215155" src="https://github.com/user-attachments/assets/4a73505d-903a-41c1-9819-50456476fce3" />


## 📌 Project Overview

The **Bank Management System** is a web-based banking application developed using **Python Flask**. It allows users to securely register, log in, manage account balances, deposit money, withdraw money, transfer funds, and track transaction history.

This project demonstrates:

* User Authentication
* Banking Operations
* Session Management
* Flask Web Development
* Transaction Tracking
* Backend Logic Implementation

---

# 🚀 Features

## ✅ User Authentication

* User Registration
* Secure Login
* Logout Functionality
* Session Handling

## ✅ Banking Operations

* Deposit Money
* Withdraw Money
* Transfer Funds
* Real-time Balance Update

## ✅ Transaction Management

* View Transaction History
* Track Deposits
* Track Withdrawals
* Track Transfers

## ✅ Dashboard

* User Welcome Section
* Current Balance Display
* Banking Forms
* Transaction Table

---

# 🛠️ Tech Stack

| Technology | Usage               |
| ---------- | ------------------- |
| Python     | Backend Programming |
| Flask      | Web Framework       |
| HTML       | Frontend Structure  |
| CSS        | Styling             |
| Jinja2     | Template Rendering  |

---

# 📂 Project Structure

```bash
Bank-Management-System/
│
├── app.py
├── main.py
├── requirements.txt
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/
│   └── style.css
│
├── src/
│   ├── bank.py
│   ├── user.py
│   └── transaction.py
│
└── README.md
```

---

# ⚙️ Installation Steps

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/Bank-Management-System-Flask.git
```

## 2️⃣ Move to Project Folder

```bash
cd Bank-Management-System-Flask
```

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 6️⃣ Run Application

```bash
python app.py
```

---

# 🌐 Application Routes

| Route        | Description       |
| ------------ | ----------------- |
| `/register`  | User Registration |
| `/login`     | User Login        |
| `/dashboard` | User Dashboard    |
| `/deposit`   | Deposit Money     |
| `/withdraw`  | Withdraw Money    |
| `/transfer`  | Transfer Funds    |
| `/logout`    | Logout User       |

---

# 🔐 Authentication Flow

1. User registers an account
2. User logs into the system
3. Session stores user email
4. User accesses dashboard
5. Banking operations are performed securely
6. Logout clears session

---

# 💳 Banking Functionalities

## Deposit

Users can add money to their account balance.

## Withdraw

Users can withdraw money if sufficient balance exists.

## Transfer

Users can transfer money to another registered user using email.

---

# 📊 Dashboard Functionalities

The dashboard displays:

* Current Balance
* Deposit Form
* Withdrawal Form
* Transfer Form
* Transaction History

---

# 📸 Project Screenshots

## 🔑 Login Page

* Secure user login interface

## 📝 Registration Page

* New user account creation

## 📈 Dashboard

* Balance display and banking operations

## 💰 Deposit & Withdraw

* Money transaction forms

## 📜 Transaction History

* Complete banking records

---

# 🧠 Core Concepts Used

* Flask Routing
* Session Management
* Object-Oriented Programming
* Form Handling
* Data Validation
* Transaction Processing

---

# 📦 Python Files Description

## `app.py`

Main Flask application containing:

* Routes
* Authentication
* Banking operations
* Session management

## `main.py`

CLI-based banking application version with:

* Register/Login
* Deposit/Withdraw
* Transfer
* Transaction View

## `requirements.txt`

Project dependencies:

* Flask
* pytest

---

# 🎯 Future Improvements

* Database Integration (MySQL/PostgreSQL)
* Password Encryption
* Email Verification
* Admin Dashboard
* Account Statement PDF
* REST API Integration
* Responsive UI

---

# 👩‍💻 Author

**Harshada Rane**
Aspiring Data Analyst & Python Developer

---

# 🏷️ GitHub Topics

Add these topics in your GitHub repository:

* flask
* python
* banking-system
* web-development
* flask-project
* python-project
* authentication
* banking-app

---

# 📌 GitHub Repository Description

```text
A Flask-based Bank Management System with user authentication, deposits, withdrawals, transfers, and transaction tracking.
```

---

# ⭐ Suggested Commit Message

```bash
git commit -m "Initial commit - Added Flask Bank Management System project"
```
