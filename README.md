# Blood Donation Project

## Overview

The Blood Donation Project is a web application designed to facilitate blood donation and management processes. It connects donors, recipients, and blood banks, enabling easy requests and offers of blood. The application includes features for user management, blood request management, and an administrative dashboard.

## Features

- User registration and authentication
- User profile management
- Blood request creation and management
- Admin dashboard for managing users and blood requests
- Notification system for updates on blood requests
- Responsive design for accessibility on various devices

## Technologies Used

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Python**: The programming language used for backend development.
- **SQLite**: Default database for development; can be switched to PostgreSQL or MySQL in production.
- **HTML/CSS**: For frontend design and layout.
- **JavaScript**: For interactive elements (if applicable).
- **Pillow**: For image handling (if applicable).

## Installation

### Prerequisites

- Python 3.x
- pip
- Django

### Steps to Set Up

1. **Clone the repository:**

   ```
   git clone https://github.com/yourusername/blood-donation.git
   cd blood-donation
   ```

2. **Create a virtual environment:**

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```
   python manage.py migrate
   ```

5. **Run the development server:**

   ```
   python manage.py runserver
   ```

6. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **User Registration**: Navigate to the registration page and create an account.
- **User Login**: Log in to your account to access user features.
- **Create Blood Requests**: After logging in, you can create blood requests through your user dashboard.
- **Admin Access**: Admin users can manage users and blood requests from the admin dashboard.

To install the packages listed in the requirements.txt, you can run:
pip install -r requirements.txt


