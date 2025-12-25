# Career Application Tracker
Project Overview
The Career Application Tracker is a web application that allows users to manage and track their job applications efficiently. Users can add applications, update their status (Applied, Interview, Offer, Rejected), and monitor important dates such as when they applied and interview schedules. The dashboard provides filtering and search functionality for better user experience, and the interface is fully mobile-responsive.
This project combines backend and frontend development to provide a modern, interactive web experience. Users can perform all actions dynamically without page reloads, thanks to JavaScript-powered features like status updates and AJAX deletion of applications.

# Distinctiveness and Complexity
This project satisfies the distinctiveness and complexity requirements of the CS50W Capstone:
Distinctiveness:
Unlike other CS50W projects, this application is neither a social network nor an e-commerce platform.
Its focus is on personal productivity and career tracking, which sets it apart from standard course projects.
Complexity:
Backend: Built with Django, using relational models for user-linked applications and secure user authentication (login, logout, registration).
Frontend: Includes dynamic JavaScript interactions to update status without reloading pages, delete applications asynchronously, and filter/search the data.
Responsive Design: The dashboard and controls adapt to mobile and desktop screens using modern CSS techniques, including gradients, hover effects, badges, and flexible table layouts.
UX/UI Design: Color-coded status badges, Google Fonts integration, and card-style layout enhance usability and visual appeal.

This combination of authentication, relational data handling, frontend interactivity, mobile responsiveness, and thoughtful design demonstrates significant full-stack development effort, making the project sufficiently complex and unique.
# File Structure 
capstone/
├── tracker/
│   ├── models.py           # Defines the Application model
│   ├── views.py            # Handles dashboard, add/edit/delete, login/register
│   ├── urls.py             # Maps URL patterns to views
│   ├── templates/tracker/
│   │   ├── layout.html     # Base template with navbar/header
│   │   ├── dashboard.html  # Dashboard page showing applications
│   │   ├── login.html      # Login page
│   │   └── register.html   # Registration page
│   └── static/tracker/
│       ├── styles.css      # Global and page-specific styling
│       └── main.js         # JavaScript for status updates and deletion
├── manage.py               # Django management script
└── requirements.txt        # Required Python packages


# How to Run
1. Clone the repository:
  git clone https://github.com/YOUR_USERNAME/capstone.git
  cd capstone

2. Set up a virtual environment and install dependencies:
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt

3. Run Django migrations:
  python manage.py makemigrations
  python manage.py migrate

4. Create a superuser (optional):
  python manage.py createsuperuser

5. Run the development server:
   python manage.py runserver
  Open your browser at http://127.0.0.1:8000/ to use the dashboard


# Features
User Authentication: Secure login, logout, and registration.
CRUD Operations: Add, update, and delete job applications.
Dynamic Status Updates: Change application status using a dropdown without reloading the page.
Filtering & Search: Quickly find applications by status, company, or position.
Mobile-Responsive: Works seamlessly on desktops, tablets, and smartphones.
Modern Design: Gradient backgrounds, card-style containers, hover effects, color-coded badges, and Google Fonts.

# Additional Notes
JavaScript & AJAX: Enables smooth, real-time updates for status and deletion.
Security: Each user only sees their applications; CSRF protection is implemented.
Distinctive Purpose: Designed for career management, which is unique among CS50W projects.
Deployment Ready: Can be easily deployed to platforms like Heroku or PythonAnywhere.



   
