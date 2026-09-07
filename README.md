# 💼 Online Job Application System

A **Python and MySQL-based Online Job Application System** designed to manage candidates, companies, job opportunities, and job applications efficiently.

This project demonstrates how Python can be integrated with a relational database to perform **CRUD operations, database relationships, and application-status management**.

---

## 📌 Project Overview

The Online Job Application System provides a simple, menu-driven platform for managing the complete job application workflow.

The system maintains four major entities:

* 👤 **Candidates**
* 🏢 **Companies**
* 💼 **Jobs**
* 📝 **Applications**

Users can add, view, update, and delete records while also managing job applications and their current status.

---

## 🎯 Objectives

* Manage candidate information efficiently.
* Store and manage company details.
* Create and maintain job postings.
* Allow candidates to apply for available jobs.
* Track application status.
* Demonstrate database relationships using MySQL.
* Implement CRUD operations using Python.
* Practice Python-MySQL connectivity.

---

## 🚀 Key Features

### 👤 Candidate Management

* Add a new candidate
* View candidate details
* Update candidate information
* Delete candidate records
* Store candidate name, email, phone number, and skills

### 🏢 Company Management

* Add company details
* View registered companies
* Update company information
* Delete company records
* Store company name, location, and email

### 💼 Job Management

* Add job opportunities
* View available jobs
* Update job information
* Delete job postings
* Store job title, job type, salary, and associated company

### 📝 Application Management

* Apply for a job
* View submitted applications
* Update application status
* Delete applications
* Track application date and status

### 📊 Application Status

Applications can be managed using statuses such as:

* `Applied`
* `Shortlisted`
* `Rejected`
* `Selected`

---

## 🛠️ Technologies Used

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| **Python**       | Application logic         |
| **MySQL**        | Database management       |
| **PyMySQL**      | Python-MySQL connectivity |
| **SQL**          | Database queries          |
| **Git & GitHub** | Version control           |

---

## 🗄️ Database Structure

The project uses four main tables:

```text
┌──────────────────┐
│    candidates    │
├──────────────────┤
│ candidate_id PK  │
│ name             │
│ email            │
│ phone            │
│ skills           │
└────────┬─────────┘
         │
         │
         ▼
┌──────────────────┐
│   applications   │
├──────────────────┤
│ application_id PK│
│ candidate_id FK  │
│ job_id FK        │
│ application_date │
│ status           │
└────────┬─────────┘
         │
         │
         ▼
┌──────────────────┐
│       jobs       │
├──────────────────┤
│ job_id PK        │
│ company_id FK    │
│ job_title        │
│ job_type         │
│ salary           │
└────────┬─────────┘
         │
         │
         ▼
┌──────────────────┐
│     companies    │
├──────────────────┤
│ company_id PK    │
│ company_name     │
│ location         │
│ email            │
└──────────────────┘
```

The application module uses SQL `JOIN` operations to retrieve candidate, job, and application information together.

---

## 📂 Project Structure

```text
Online-Job-Application/
│
├── app.py
├── candidate.py
├── company.py
├── job.py
├── application.py
├── main.py
└── README.md
```

### File Description

| File             | Description                                     |
| ---------------- | ----------------------------------------------- |
| `app.py`         | Establishes the MySQL database connection       |
| `candidate.py`   | Handles candidate CRUD operations               |
| `company.py`     | Handles company CRUD operations                 |
| `job.py`         | Handles job CRUD operations                     |
| `application.py` | Handles job applications and application status |
| `main.py`        | Main menu and program execution                 |
| `README.md`      | Project documentation                           |

---

## ⚙️ Requirements

Before running the project, make sure you have:

* Python 3.x
* MySQL Server
* MySQL Workbench (optional)
* PyMySQL package
* VS Code or another Python IDE

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sruthi7989/Online-Job-Application.git
```

### 2. Navigate to the Project Directory

```bash
cd Online-Job-Application
```

### 3. Install PyMySQL

```bash
pip install pymysql
```

---

## 🗃️ Database Setup

Open MySQL and create the database:

```sql
CREATE DATABASE job_portal;
```

Select the database:

```sql
USE job_portal;
```

Create the required tables:

```sql
CREATE TABLE candidates (
    candidate_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    skills VARCHAR(255)
);

CREATE TABLE companies (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    company_name VARCHAR(100),
    location VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE jobs (
    job_id INT PRIMARY KEY AUTO_INCREMENT,
    company_id INT,
    job_title VARCHAR(100),
    job_type VARCHAR(50),
    salary VARCHAR(50),
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE applications (
    application_id INT PRIMARY KEY AUTO_INCREMENT,
    candidate_id INT,
    job_id INT,
    application_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);
```

---

## 🔐 Database Configuration

Update the database connection in `app.py` with your own MySQL credentials.

**Do not commit real passwords or credentials to GitHub.**

A better approach is to use environment variables:

```python
import os
from pymysql import connect

def get_connection():
    return connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "job_portal")
    )
```

Create a `.env` file locally and add it to `.gitignore`.

---

## ▶️ How to Run

After setting up MySQL and configuring the database connection:

```bash
python main.py
```

The application displays a menu similar to:

```text
======================================
 ONLINE JOB APPLICATION SYSTEM
======================================

1. Add Candidate
2. View Candidates
3. Update Candidate
4. Delete Candidate

5. Add Company
6. View Companies
7. Update Company
8. Delete Company

9. Add Job
10. View Jobs
11. Update Job
12. Delete Job

13. Apply for Job
14. View Applications
15. Update Application Status
16. Delete Application

17. Exit
```

Select the required option and provide the requested information.

---

## 🔄 Application Workflow

```text
Candidate
    │
    ▼
Register Candidate
    │
    ▼
View Available Jobs
    │
    ▼
Apply for Job
    │
    ▼
Application Created
    │
    ▼
Application Status
    │
    ├── Applied
    ├── Shortlisted
    ├── Rejected
    └── Selected
```

---

## 💡 SQL Concepts Demonstrated

This project demonstrates practical SQL concepts including:

* `CREATE DATABASE`
* `CREATE TABLE`
* Primary Keys
* Foreign Keys
* `INSERT`
* `SELECT`
* `UPDATE`
* `DELETE`
* `JOIN`
* Parameterized SQL queries
* Database relationships
* Transactions using `commit()`

---

## 🧠 Python Concepts Demonstrated

* Functions
* Modules
* Importing functions between Python files
* User input
* Conditional statements
* Loops
* Database connectivity
* Exception-aware database programming
* SQL execution through Python
* Modular program structure

---

## 📈 Future Enhancements

The project can be extended with:

* 🔐 User authentication and login
* 👨‍💼 Separate recruiter and candidate dashboards
* 🔎 Job search and filtering
* 📄 Resume upload
* 📧 Email notifications
* 🌐 Web interface using Flask or Django
* 🔒 Password hashing and improved security
* 📊 Admin dashboard
* ☁️ Cloud database integration
* 📱 Responsive frontend
* 📋 Advanced application tracking

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Python programming
* MySQL database management
* Python-MySQL connectivity
* CRUD operations
* Relational database design
* SQL JOIN operations
* Modular programming
* Building a database-driven application

---

## 👩‍💻 Author

**Sruthi Puchakayala**

B.Tech – Information Technology

---

## 🔗 Project Repository

[Online Job Application System](https://github.com/Sruthi7989/Online-Job-Application)

---

## ⭐ If you find this project useful

Feel free to ⭐ star the repository and explore the source code.
