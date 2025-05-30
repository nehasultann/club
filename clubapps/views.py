from django.shortcuts import render, redirect
from .utils import authenticate_csv, add_user_to_csv, load_user_data, update_user_data_in_csv

# LOGIN VIEW
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if authenticate_csv(username, password):
            request.session['username'] = username  # Store username in session
            return redirect('dashboard')
        else:
            return render(request, 'clubapps/login.html', {'error': 'Invalid credentials'})
    return render(request, 'clubapps/login.html')

# SIGNUP VIEW
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        full_name = request.POST.get('full_name', '')
        email = request.POST.get('email', '')

        if add_user_to_csv(username, password, full_name, email):
            return redirect('login')
        else:
            return render(request, 'clubapps/signup.html', {'error': 'Username already exists'})
    return render(request, 'clubapps/signup.html')


# DASHBOARD VIEW
def dashboard(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    return render(request, 'clubapps/dashboard.html', {'username': username})


def profile(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')

    data = load_user_data(username)
    return render(request, 'clubapps/profile.html', {'user_data': data})

# LOGOUT VIEW
def logout_view(request):
    request.session.flush()  # Clear session
    return redirect('login')

# Update Profile View
def update_profile_view(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')

    user_data = load_user_data(username)

    if request.method == 'POST':
        # Extract updated fields from POST
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        club = request.POST.get('club')
        role = request.POST.get('role')

        # Update the CSV file
        update_user_data_in_csv(username, full_name, email, club, role)

        # Redirect back to profile page
        return redirect('profile')

    return render(request, 'clubapps/update_profile.html', {'user_data': user_data})
