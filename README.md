# Club Membership Portal

A user-friendly Django web application that allows students to register, log in, and explore various sports clubs and activities. Users can view and update their profiles, register for clubs, and manage participation—all through a clean and responsive interface.

---

## Features

- User Authentication: Login and registration with CSV-based data storage.
- User Profile: View and update details such as full name, email, club, and role.
- Club Dashboard: Explore clubs like Football, Cricket, Badminton, and Athletics with descriptions and registration fees.
- Responsive and colorful UI with a modern design.
- Data persistence using CSV files for simplicity.

---

## Technology Stack

- Backend: Django (Python)
- Frontend: HTML, CSS (custom styling)
- Data Storage: CSV files
- Version Control: Git & GitHub

---

## Project Structure

club_project/
├── clubapps/
│ ├── templates/clubapps/
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── dashboard.html
│ │ └── profile.html
│ ├── static/css/
│ │ ├── style.css
│ │ └── images/
│ │ ├── bg.jpg
│ │ └── [club images]
│ ├── views.py
│ ├── urls.py
│ └── ...
├── users.csv
├── manage.py
└── .gitignore


---

## How to Run Locally

1. Clone the repository:
git clone https://github.com/nehasultann/django-club-system.git
cd django-club-system

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate


3. Install dependencies:
pip install -r requirements.txt


4. Run the Django development server:
python manage.py runserver


5. Open your browser and visit:
http://127.0.0.1:8000
