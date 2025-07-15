# Django Monthly Challenges App

A simple Django web application that showcases monthly challenges, built as part of a Python and Django fundamentals learning journey. This project demonstrates core Django concepts including project and app structure, URL routing, views, template inheritance, static file management, and basic data handling.

## Table of Contents

1.  [Project Overview](#1-project-overview)
2.  [Features](#2-features)
3.  [Folder Structure](#3-folder-structure)
4.  [Setup and Installation](#4-setup-and-installation)
    * [Prerequisites](#prerequisites)
    * [Cloning the Repository](#cloning-the-repository)
    * [Virtual Environment Setup](#virtual-environment-setup)
    * [Database Migrations](#database-migrations)
    * [Running the Development Server](#running-the-development-server)
5.  [Usage](#5-usage)
    * [Navigating the App](#navigating-the-app)
    * [Accessing Challenges](#accessing-challenges)
6.  [Project Configuration Details](#6-project-configuration-details)
    * [Django Settings (`settings.py`)](#django-settings-settingspy)
    * [Project URLs (`blogger/urls.py`)](#project-urls-bloggerurlspy)
    * [App URLs (`challenges/urls.py`)](#app-urls-challengesurlspy)
    * [Views (`challenges/views.py`)](#views-challengesviewspy)
    * [Templates](#templates)
    * [Static Files](#static-files)
    * [Custom Error Pages](#custom-error-pages)
7.  [Data Structure](#7-data-structure)
8.  [Deployment Notes](#8-deployment-notes)
9.  [Contributing](#9-contributing)
10. [License](#10-license)
11. [Contact](#11-contact)



## 1. Project Overview

This project is a small web application that presents a list of monthly challenges. Users can browse all available months and click on a specific month to see its details, including the challenge name, description, duration, benefits, and how-to steps. The application is built using the Django web framework.

## 2. Features

* **Monthly Challenge Listing:** A home page displaying all months with available challenges.
* **Dynamic Challenge Details:** Each month has a dedicated page showing its specific challenge.
* **Flexible URL Routing:** Challenges can be accessed by month name (e.g., `/challenges/january/`) or by month number (e.g., `/challenges/1/`), with number-based URLs redirecting to name-based ones for better SEO.
* **Template Inheritance:** Utilizes `base.html` for consistent site-wide layout.
* **Static File Management:** Proper handling of CSS for styling.
* **Custom 404 Pages:** User-friendly error pages for missing content (both app-specific and global).
* **Modular Data Storage:** Challenge data stored in a separate Python file.

## 3. Folder Structure

The project follows a standard Django project structure, with a dedicated app for challenges and clear separation of templates and static files.

blogger/                  \# Project Root
├── .gitignore            \# Specifies intentionally untracked files
├── manage.py             \# Django's command-line utility
├── blogger/              \# Main Project Configuration
│   ├── **init**.py
│   ├── settings.py       \# Project settings
│   ├── urls.py           \# Main URL routing
│   └── wsgi.py           \# WSGI config for deployment
│
├── challenges/           \# 'challenges' Django App
│   ├── migrations/
│   ├── **init**.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py         \# (Currently empty, no database models needed for static data)
│   ├── tests.py
│   ├── urls.py           \# App-specific URL routing
│   ├── views.py          \# App logic and template rendering
│   └── templates/        \# App's template directory
│       └── challenges/   \# Nested directory to prevent template name collisions
│           ├── index.html                  \# Lists all months
│           ├── challenge\_detail.html       \# Displays single challenge
│           └── challenge\_not\_found.html    \# Specific error for missing challenges
│
├── data/                 \# Custom Python package for application data
│   ├── **init**.py       \# Makes 'data' a Python package
│   └── challenge\_list.py \# Contains the monthly\_challenges dictionary
│
├── static/               \# Project-wide static assets (CSS, JS, images)
│   └── css/
│       └── base\_styles.css \# Common CSS for the entire site
│
└── templates/            \# Project-wide templates (for base layout and global errors)
├── base.html         \# Base template for site layout
├── 404.html          \# Global Not Found page (for DEBUG=False)
└── 500.html          \# Global Server Error page (for DEBUG=False)


## 4. Setup and Installation

These instructions assume you are working within a WSL (Windows Subsystem for Linux) environment.

### Prerequisites

* Python 3.8+
* pip (Python package installer)
* Git
* WSL (Windows Subsystem for Linux) with a Linux distribution (e.g., Ubuntu) installed.
* Windows Firewall rule configured for WSL, if accessing from Windows browser outside of `127.0.0.1`. (e.g., `netsh advfirewall firewall add rule name="Django Port 8000" dir=in action=allow protocol=TCP localport=8000`)

### Cloning the Repository

First, open your WSL terminal (e.g., Ubuntu).

# Navigate to where you want to store your project
cd ~ # Or your preferred development directory

# Clone the repository
git clone [https://github.com/your-username/blogger.git](https://github.com/your-username/blogger.git) # Replace with your repo URL
cd blogger

### Virtual Environment Setup

It's highly recommended to use a Python virtual environment to manage dependencies.

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install Django and other dependencies
pip install Django
# If you have a requirements.txt file, use: pip install -r requirements.txt
```

### Database Migrations

Even though this project primarily uses static data, Django requires database setup for its built-in features (like the Admin panel).

```bash
python manage.py migrate
```

### Running the Development Server

Before running, ensure your `blogger/blogger/settings.py` `ALLOWED_HOSTS` includes your WSL IP address if you plan to access it from Windows using that IP. E.g., `ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.1.4']`

```bash
python manage.py runserver 0.0.0.0:8000
```

This will start the Django development server. You can access the application in your web browser at:

  * **`http://127.0.0.1:8000/`** (This will redirect to `/challenges/`)
  * **`http://127.0.0.1:8000/challenges/`** (The main challenges index page)
  * **`http://YOUR_WSL_IP_ADDRESS:8000/challenges/`** (If accessing from Windows using WSL's IP)

## 5\. Usage

### Navigating the App

  * **Home Page (`/challenges/`):** Displays a grid of all 12 months. Each month is a clickable link.
  * **Month Challenge Page (`/challenges/<month_name>/`):** Clicking a month (e.g., "January") or directly navigating to `challenges/january/` will show the specific challenge details for that month.

### Accessing Challenges

You can access challenge details in two primary ways:

1.  **By Month Name (Recommended):**
    `http://127.0.0.1:8000/challenges/january/`
    `http://127.0.0.1:8000/challenges/february/`
    ...and so on for all 12 months.

2.  **By Month Number (Redirects to Name):**
    `http://127.0.0.1:8000/challenges/1/` (Redirects to `/challenges/january/`)
    `http://127.0.0.1:8000/challenges/2/` (Redirects to `/challenges/february/`)
    ...and so on.

## 6\. Project Configuration Details

This section outlines the key configurations and code structure.

### Django Settings (`settings.py`)

  * `INSTALLED_APPS`: `'challenges'` is registered.
  * `TEMPLATES`: Configured to find templates in `blogger/templates/` (for `base.html`, `404.html`, `500.html`) and within each app's `templates/` directory (for `challenges/templates/challenges/`).
    ```python
    # blogger/blogger/settings.py
    import os
    # ...
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')], # Project-wide templates
            'APP_DIRS': True, # App-specific templates
            # ...
        },
    ]
    ```
  * `STATIC_URL` and `STATICFILES_DIRS`: Configured to serve static assets like `base_styles.css` from the `blogger/static/` directory.

### Project URLs (`blogger/urls.py`)

  * Includes the `challenges` app's URLs under the `/challenges/` path.

  * Crucially, it assigns a `namespace='challenges'` to these URLs, enabling reverse URL lookups like `{% url 'challenges:index' %}` in templates.

  * The root path (`/`) is redirected to `/challenges/`.

    ```python
    # blogger/blogger/urls.py
    from django.contrib import admin
    from django.urls import path, include
    from django.views.generic.base import RedirectView # Import this for redirection

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('challenges/', include('challenges.urls', namespace='challenges')),
        path('', RedirectView.as_view(url='/challenges/', permanent=True)),
    ]
    ```

### App URLs (`challenges/urls.py`)

  * Defines the URL patterns specific to the `challenges` app.

  * `app_name = 'challenges'` is set at the top, which is mandatory when including this module with a namespace in the project's `urls.py`.

  * Includes routes for the index page, month by number, and month by name.

    ```python
    # blogger/challenges/urls.py
    from django.urls import path
    from . import views

    app_name = 'challenges' # REQUIRED for namespace to work

    urlpatterns = [
        path('', views.index, name='index'),
        path('<int:month_number>/', views.month_number_challenge, name='month_number_challenge'),
        path('<str:month_name>/', views.month_name_challenge, name='month_name_challenge'),
    ]
    ```

### Views (`challenges/views.py`)

  * **`index(request)`:** Fetches all month names from `monthly_challenges` and renders `challenges/index.html`.
  * **`month_name_challenge(request, month_name)`:**
      * Capitalizes the `month_name` to match dictionary keys.
      * Retrieves challenge data. If not found, renders `challenges/challenge_not_found.html` with a 404 status.
      * Renders `challenges/challenge_detail.html` with the specific challenge data.
  * **`month_number_challenge(request, month_number)`:**
      * Converts `month_number` to a `month_name` using a helper function.
      * If the number is invalid, renders `challenges/challenge_not_found.html` with a 404 status.
      * **Redirects** to the canonical `month_name_challenge` URL (e.g., `/challenges/1/` redirects to `/challenges/january/`). This is good for SEO and URL consistency.
  * **Helper `get_month_name_from_number(month_number)`:** A utility function to safely convert month integers to full month names.

### Templates

  * **`base.html` (`blogger/templates/base.html`):** The main structural template, defining header, navigation, main content block (`{% block content %}`), and footer. All other templates `{% extends "base.html" %}`.
  * **`index.html` (`challenges/templates/challenges/index.html`):** Loops through the `months` context variable to create clickable links to individual challenge pages.
  * **`challenge_detail.html` (`challenges/templates/challenges/challenge_detail.html`):** Displays the details of a single challenge using data passed in the `challenge` context variable.
  * **`challenge_not_found.html` (`challenges/templates/challenges/challenge_not_found.html`):** Custom template rendered by app views when a specific challenge is not found.

### Static Files

  * `base_styles.css` (`blogger/static/css/base_styles.css`): Contains global CSS rules for the project.
  * Templates use `{% load static %}` and `{% static 'path/to/file.css' %}` to correctly link to static assets.

### Custom Error Pages

  * `404.html` (`blogger/templates/404.html`): Used by Django when `DEBUG=False` and a non-existent URL is accessed (e.g., `http://127.0.0.1:8000/nonexistent`).
  * `500.html` (`blogger/templates/500.html`): Used by Django when `DEBUG=False` and an unhandled server error occurs.
  * **To test these global error pages:**
    1.  Set `DEBUG = False` in `settings.py`.
    2.  Add `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')` to `settings.py`.
    3.  Run `python manage.py collectstatic` (Django will copy all static files into the `staticfiles` directory).
    4.  Restart your Django server (`python manage.py runserver`).
    5.  Access a non-existent URL (e.g., `http://127.0.0.1:8000/blah/`) to see `404.html`.
    6.  To test `500.html`, you would intentionally raise an error in a view.

## 7\. Data Structure

The monthly challenge data is stored in a Python dictionary located at `data/challenge_list.py`:

```python
# data/challenge_list.py
monthly_challenges = {
    "January": {
        "challenge_name": "Read a Book a Week",
        "description": "Dedicate time each week to read a full book.",
        "duration": "4 weeks",
        "benefits": "Expands knowledge, improves focus, reduces stress.",
        "how_to": [
            "Choose 4 books you want to read.",
            "Set aside dedicated reading time each day (e.g., 30-60 minutes).",
            "Minimize distractions (turn off notifications).",
            "Join a book club or discuss with friends for accountability."
        ]
    },
    # ... (other months continue in the same format)
    "December": {
        "challenge_name": "Mindful Holiday Season",
        "description": "Practice mindfulness and gratitude daily amidst holiday busyness.",
        "duration": "4 weeks",
        "benefits": "Reduces stress, increases joy, improves presence.",
        "how_to": [
            "Dedicate 10 minutes daily for meditation or quiet reflection.",
            "Practice mindful eating during meals and snacks.",
            "Express gratitude to at least one person each day.",
            "Take short breaks throughout the day to focus on your breath."
        ]
    }
}
```

## 8\. Deployment Notes

For production deployment, remember to:

  * Set `DEBUG = False` in `settings.py`.
  * Configure `ALLOWED_HOSTS` with your production domain(s).
  * Run `python manage.py collectstatic` to gather static files.
  * Use a production-ready WSGI server (e.g., Gunicorn, uWSGI) and a web server (e.g., Nginx, Apache) to serve your application and static files.
  * Implement proper security practices (e.g., strong `SECRET_KEY`, environment variables for sensitive info).

## 9\. Contributing

Feel free to fork this repository, create pull requests, or open issues if you have suggestions or find bugs.

## 10\. License

This project is licensed under the MIT License - see the `LICENSE` file (if you add one) for details.

## 11\. Contact

For any questions or feedback, please reach out:

  * **Your Name:** Raje Abhilash Mohite
  * **GitHub:** [github.com/rajeabhilash](https://github.com/rajeabhilash)
  * **Email:** [rajeabhilash\vashishthaenterprisecare@gmail.com](mailto:vashishthaenterprisecare@gmail.com) 
