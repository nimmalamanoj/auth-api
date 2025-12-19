# 🔐 Flask JWT Authentication API

A secure backend authentication system built using **Flask**, **MySQL**, and **JWT**.  
This project provides user registration, login, and protected routes using token-based authentication.

---

## 🚀 Features

- User Registration with password hashing (bcrypt)
- User Login with credential verification
- JWT (JSON Web Token) generation
- Token-based protected routes
- MySQL database integration
- Secure environment variable management using `.env`
- REST API tested using Postman / curl

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **MySQL**
- **JWT (PyJWT)**
- **bcrypt**
- **python-dotenv**
- **Git & GitHub**

---

## 📁 Project Structure

# 🔐 Flask JWT Authentication API

A secure backend authentication system built using **Flask**, **MySQL**, and **JWT**.  
This project provides user registration, login, and protected routes using token-based authentication.

---

## 🚀 Features

- User Registration with password hashing (bcrypt)
- User Login with credential verification
- JWT (JSON Web Token) generation
- Token-based protected routes
- MySQL database integration
- Secure environment variable management using `.env`
- REST API tested using Postman / curl

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **MySQL**
- **JWT (PyJWT)**
- **bcrypt**
- **python-dotenv**
- **Git & GitHub**

---

## 📁 Project Structure

auth-api/
│
├── app.py # Main Flask application
├── auth.py # Authentication routes (register, login, profile)
├── db.py # Database connection logic
├── .env # Environment variables (not committed)
├── .gitignore # Git ignore rules
└── venv/ # Virtual environment (not committed)


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/nimmalamanoj/auth-api.git
cd auth-api

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install Dependencies
pip install flask mysql-connector-python bcrypt python-dotenv PyJWT

### 4️⃣ Configure Environment Variables
Create a .env file in the project root:
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=auth_db
JWT_SECRET_KEY=your_secret_key

### 5️⃣ Create Database & Table
CREATE DATABASE auth_db;

USE auth_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);
Server will start at:
http://127.0.0.1:5000

🔑 API Endpoints
▶️ Register User
POST /register


Request Body:

{
  "name": "Manoj",
  "email": "manoj@gmail.com",
  "password": "manoj123"
}

▶️ Login User
POST /login


Request Body:

{
  "email": "manoj@gmail.com",
  "password": "manoj123"
}


Response:

{
  "token": "JWT_TOKEN"
}

🔒 Protected Route
GET /profile


Headers:

Authorization: JWT_TOKEN


Response:

{
  "message": "Access granted",
  "user": {
    "user_id": 1,
    "email": "manoj@gmail.com"
  }
}

🧠 Learning Outcomes

Backend API development using Flask

Secure password storage using hashing

JWT-based authentication and authorization

MySQL database design and CRUD operations

Environment variable security

API testing using Postman and curl

Git and GitHub version control

👨‍💻 Author

Nimmala Manoj
GitHub: https://github.com/nimmalamanoj

📌 Note

This project is for learning and demonstration purposes.
Do not use in production without additional security enhancements.