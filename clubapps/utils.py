import csv
import os
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password

CSV_PATH = os.path.join(settings.BASE_DIR, 'clubapps', 'user_data.csv')

def load_user_data(username):
    csv_path = os.path.join(settings.BASE_DIR, 'clubapps', 'user_data.csv')
    with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                return row
    return {}


def authenticate_csv(username, password):
    """
    Checks if the username and password match an entry in the CSV.
    Returns True if valid, else False.
    """
    if not os.path.exists(CSV_PATH):
        return False

    with open(CSV_PATH, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and check_password(password, row['password']):
                return True
    return False

def add_user_to_csv(username, password, full_name='', email=''):
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['username', 'password', 'full_name', 'email'])
            writer.writeheader()

    with open(CSV_PATH, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                return False  # User already exists

    with open(CSV_PATH, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['username', 'password', 'full_name', 'email'])
        writer.writerow({
            'username': username,
            'password': make_password(password),
            'full_name': full_name,
            'email': email
        })
    return True

def update_user_data_in_csv(username, full_name, email, club, role):
    # Read all data
    if not os.path.exists(CSV_PATH):
        return False

    rows = []
    updated = False
    with open(CSV_PATH, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                row['full_name'] = full_name
                row['email'] = email
                row['club'] = club
                row['role'] = role
                updated = True
            rows.append(row)

    if updated:
        with open(CSV_PATH, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['username', 'password', 'full_name', 'email', 'club', 'role']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        return True
    return False

