# Django-Portfolio

A dynamic personal portfolio site built with Django (MVT) — all content is managed through Django Admin and stored in SQLite (or PostgreSQL).

This repository contains:
- Separate Django apps for: bio, education, skills, experience, projects, and core
- Professional portfolio template with dark theme and gold accents
- Templates using Django template variables (no hardcoded content)
- Static & media configuration
- Admin configured for CMS-style editing

## Quick Setup (Development)

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or copy the project**
   ```bash
   cd Django-Portfolio
   ```

2. **Create virtual environment**
   ```bash
   # Windows
   python -m venv venv
   
   # macOS/Linux
   python3 -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   
   # Windows (CMD)
   venv\Scripts\activate.bat
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create `.env` file** at project root:
   ```env
   DJANGO_SECRET_KEY=your-secret-key-here
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
   ```
   
   Generate secret key:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

6. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Portfolio: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Technology Stack

- **Backend:** Django 4.2+
- **Database:** SQLite (default, no setup needed) or PostgreSQL (optional)
- **Frontend:** HTML5, CSS3, JavaScript
- **Icons:** Font Awesome (CDN)

## Project Structure

```
Django-Portfolio/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── portfolio_project/     # Main project settings
├── core/                  # Core app (home page)
├── bio/                   # Bio app
├── education/             # Education app
├── experience/            # Experience app
├── skills/                # Skills app
├── projects/              # Projects app
├── static/                # Static files (CSS, JS, images)
└── templates/             # HTML templates
```

## Adding Content

1. Log in to Django Admin: http://127.0.0.1:8000/admin/
2. Add content through the admin interface:
   - **Bio:** Personal information, profile picture, contact details
   - **Education:** Degrees and certifications
   - **Experience:** Work experience
   - **Skills:** Technical skills
   - **Projects:** Portfolio projects with technologies
   - **Technologies:** Technology tags for projects

## Database

The project uses **SQLite by default** (no installation required). The database file `db.sqlite3` is created automatically after running migrations.

To use PostgreSQL instead, uncomment the PostgreSQL configuration in `portfolio_project/settings.py` and update your `.env` file with PostgreSQL credentials.

## For Detailed Setup Instructions

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for comprehensive setup instructions, troubleshooting, and production deployment notes.

## Notes

- Add Bio, Education, Skills, Experience, Technology, and Project entries via Admin.
- Upload profile image via Bio's profile_picture field (Media will be served in DEBUG mode).
- For production: DEBUG=False, configure allowed hosts, use collectstatic, configure webserver for static & media.
