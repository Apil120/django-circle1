# 🎨 Django Circle1 — Premium Grid Blog

A modern, full-stack blogging application built using **Django** and styled with a premium, responsive **glassmorphic dark-mode interface**. This project displays a dynamic grid of blog posts fetched from an SQLite database, tracks article view counts in real-time, and integrates seamlessly with Django's administrative panel.

---

## ⚡ Key Features

*   **Premium Glassmorphic Design:** A modern dark-theme user interface designed with the **Plus Jakarta Sans** font, CSS custom properties (variables), vibrant radial gradients, layout transitions, backdrop blurs, and hover micro-animations.
*   **Dynamic Database Integration:** Pulls blog details, categories, and author metadata directly from the SQLite database.
*   **Automatic View Tracker:** Logs engagement by auto-incrementing post views every time a visitor reads the full article detail page.
*   **Smart Template Fallbacks:** If the database contains no posts yet, the site gracefully falls back to displaying structured, styled static mock articles to ensure a clean first-time user experience.
*   **Django Admin Ready:** Fully configured with Django's standard administration system, enabling quick CRUD operations on blogs.

---

## 📂 Project Structure

```bash
blog_project/
│
├── manage.py            # Django command-line utility
├── db.sqlite3           # SQLite database file
├── .gitignore           # Git ignore configuration
│
├── blogsite/            # Project configuration directory
│   ├── __init__.py
│   ├── settings.py      # Core settings and database configs
│   ├── urls.py          # Main URL routing (points to blogapp)
│   ├── wsgi.py          # WSGI configuration for deployment
│   └── asgi.py          # ASGI configuration
│
├── blogapp/             # Core blog application
│   ├── migrations/      # Database migrations
│   ├── admin.py         # Admin panel registrations
│   ├── apps.py          # Application configuration
│   ├── models.py        # Database models (Blog model)
│   ├── urls.py          # Blogapp specific URL routing
│   ├── views.py         # Request-response controller logic (Home & Read views)
│   └── tests.py         # Unit tests
│
└── templates/           # Frontend presentation layer
    ├── index.html       # Home page featuring grid of blog cards
    └── blog.html        # Detailed view for reading individual articles
```

---

## 🛠️ Database Schema

The core structure of the blog is defined by the following fields inside `blogapp/models.py`:

```python
class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    body = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField()
```

---

## 🚀 Setup & Installation

Follow these steps to run the project locally on your machine:

### 1. Prerequisite Checks
Ensure you have **Python 3.x** and **pip** installed.

### 2. Activate Virtual Environment
Navigate to the project root directory and activate the virtual environment:

**On Windows (PowerShell/CMD):**
```powershell
.venv\Scripts\activate
```

**On Unix or macOS:**
```bash
source .venv/bin/activate
```

*(If `.venv` is not configured yet, you can create it via `python -m venv .venv` and install django using `pip install django`)*

### 3. Run Migrations
Generate the SQLite database schema by running:
```bash
python manage.py migrate
```

### 4. Create an Administrative Superuser
Create a user account to log in to the administrative portal and write blog posts:
```bash
python manage.py createsuperuser
```
*Follow the terminal prompts to set your username, email, and password.*

### 5. Start the Development Server
Launch the built-in Django server:
```bash
python manage.py runserver
```

### 6. View the App
Open your browser and navigate to:
*   **Main Application:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
*   **Django Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 💻 Tech Stack

*   **Backend:** Python 3.x, Django 6.x
*   **Database:** SQLite3
*   **Frontend:** Semantic HTML5, Vanilla CSS3 (Custom Grid system, Glassmorphism, CSS variables, SVG icons)
