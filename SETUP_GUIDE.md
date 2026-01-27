# Django Portfolio - Setup Guide for New System

## Prerequisites Required

### 1. Python
- **Version:** Python 3.8 or higher (Python 3.12 recommended)
- **Check if installed:** `python --version` or `python3 --version`
- **Download:** https://www.python.org/downloads/

### 2. pip (Python Package Manager)
- Usually comes with Python
- **Check if installed:** `pip --version` or `pip3 --version`
- **Update if needed:** `python -m pip install --upgrade pip`

### 3. Git (Optional - if cloning from repository)
- **Check if installed:** `git --version`
- **Download:** https://git-scm.com/downloads

---

## Step-by-Step Setup Instructions

### Step 1: Get the Project Files

**Option A: If you have the project folder**
- Copy the entire project folder to the new system

*

### Step 2: Navigate to Project Directory

Open terminal/command prompt and navigate to the project folder:



### Step 3: Create Virtual Environment

**Windows:**
```powershell
python -m venv venv
```



### Step 4: Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```



**Note:** You should see `(venv)` at the beginning of your command prompt when activated.

---

### Step 5: Install Dependencies

With virtual environment activated, run:

```bash
pip install -r requirements.txt
```

**This will install:**
- Django (>=4.2)
- psycopg2-binary (for PostgreSQL - optional)
- python-dotenv (for environment variables)

---

### Step 6: Create .env File

Create a `.env` file in the project root directory (same level as `manage.py`):

**Windows (PowerShell):**
```powershell
New-Item -Path .env -ItemType File
notepad .env
```


**Add this content to .env:**
```env
DJANGO_SECRET_KEY=your-secret-key-here-change-this-in-production
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# Database (SQLite - no setup needed)
# The project uses SQLite by default, so no database setup required!




**Generate a secret key (optional):**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

### Step 7: Run Database Migrations

With virtual environment activated:

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates the database tables.

---

### Step 8: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

**Follow the prompts:**
- Username: (enter your username)
- Email: (enter your email - optional)
- Password: (enter password - it won't show as you type)
- Password confirmation: (enter again)

---



### Step 10: Run the Development Server

```bash
python manage.py runserver
```

**You should see:**
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---

### Step 11: Access the Application

1. **Portfolio Site:** Open browser and go to: `http://127.0.0.1:8000/`
2. **Admin Panel:** Go to: `http://127.0.0.1:8000/admin/`
   - Login with the superuser credentials you created

---

## Quick Command Reference

### Daily Usage Commands

**Activate virtual environment:**
- Windows: `.\venv\Scripts\Activate.ps1`
- macOS/Linux: `source venv/bin/activate`

**Run server:**
```bash
python manage.py runserver
```

**Stop server:**
- Press `Ctrl + C` in the terminal

**Create new migrations (after model changes):**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Deactivate virtual environment:**
```bash
deactivate
```

---

## Framework & Technology Stack

### Backend Framework
- **Django 4.2+** - Python web framework

### Database
- **SQLite** (default) - No installation needed, file-based database


### Frontend
- **HTML5/CSS3** - Static files in `static/` folder
- **JavaScript** - For animations (optional)
- **Font Awesome** - Icons (loaded from CDN)

### Python Packages
- Django - Web framework
- python-dotenv - Environment variable management
- psycopg2-binary - PostgreSQL adapter (optional)

---

## Troubleshooting

### Issue: "python is not recognized"
**Solution:** Use `python3` instead of `python` on macOS/Linux



## File Structure Overview

```
Django-Portfolio/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (create this)
├── db.sqlite3               # SQLite database (created after migrate)
├── portfolio_project/       # Main project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL configuration
│   └── wsgi.py              # WSGI config
├── core/                    # Core app (home page)
├── bio/                     # Bio app
├── education/               # Education app
├── experience/              # Experience app
├── skills/                  # Skills app
├── projects/                # Projects app
├── static/                  # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/               # Base templates
└── media/                   # User uploads (created automatically)
```

---

## Production Deployment Notes

For production deployment, you'll need to:

1. Set `DEBUG=False` in `.env`
2. Set proper `ALLOWED_HOSTS` in `.env`
3. Use a production database (PostgreSQL recommended)
4. Set up a web server (Nginx/Apache)
5. Use a WSGI server (Gunicorn/uWSGI)
6. Set up static file serving
7. Configure media file serving
8. Use environment variables for sensitive data

---

## Summary Checklist

- [ ] Python 3.8+ installed
- [ ] Project files copied/cloned
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with configuration
- [ ] Migrations run (`python manage.py migrate`)
- [ ] Superuser created (`python manage.py createsuperuser`)
- [ ] Server running (`python manage.py runserver`)
- [ ] Site accessible at http://127.0.0.1:8000/
- [ ] Admin panel accessible at http://127.0.0.1:8000/admin/

---

## Need Help?

If you encounter any issues:
1. Check that virtual environment is activated
2. Verify all dependencies are installed
3. Ensure `.env` file exists and has correct values
4. Check that migrations have been run
5. Review error messages in the terminal

