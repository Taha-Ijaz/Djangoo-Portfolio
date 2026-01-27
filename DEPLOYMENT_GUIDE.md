# Deployment Guide - Running from ZIP File

## If You're Sharing the Project as ZIP

### ⚠️ Important: What to Include/Exclude

**✅ INCLUDE in ZIP:**
- All Python files (`.py`)
- `manage.py`
- `requirements.txt`
- `README.md`
- `SETUP_GUIDE.md`
- `templates/` folder
- `static/` folder
- `portfolio_project/` folder
- All app folders (`core/`, `bio/`, `education/`, etc.)
- `.gitignore` (if exists)

**❌ DO NOT INCLUDE (will be recreated):**
- `venv/` folder (virtual environment - too large, OS-specific)
- `.env` file (contains sensitive data - SECRET_KEY)
- `db.sqlite3` (database - will be empty anyway)
- `__pycache__/` folders
- `*.pyc` files
- `media/` folder (user uploads - will be empty)

---

## For the Person Receiving the ZIP

### What They Need to Have Installed

**Required:**
1. **Python 3.8 or higher**
   - Check: `python --version` or `python3 --version`
   - Download: https://www.python.org/downloads/

2. **pip** (comes with Python)
   - Check: `pip --version`

**That's it!** No other frameworks or databases needed.

---

## Step-by-Step Instructions for Recipient

### Step 1: Extract ZIP File
- Extract the ZIP to a folder (e.g., `C:\Projects\Django-Portfolio` or `~/Projects/Django-Portfolio`)

### Step 2: Open Terminal/Command Prompt
Navigate to the extracted folder:
```bash
cd path/to/Django-Portfolio
```

### Step 3: Create Virtual Environment
```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

### Step 4: Activate Virtual Environment
```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (CMD)
venv\Scripts\activate.bat

# macOS/Linux
source venv/bin/activate
```

**You should see `(venv)` in your prompt.**

### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- Django
- python-dotenv
- psycopg2-binary (optional)

### Step 6: Create .env File
Create a `.env` file in the project root (same folder as `manage.py`):

**Windows (PowerShell):**
```powershell
New-Item -Path .env -ItemType File
notepad .env
```

**macOS/Linux:**
```bash
touch .env
nano .env
```

**Add this content:**
```env
DJANGO_SECRET_KEY=generate-a-secret-key-here
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

**Generate secret key:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the generated key and paste it in `.env` file.

### Step 7: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

This creates the database file (`db.sqlite3`).

### Step 8: Create Admin User
```bash
python manage.py createsuperuser
```

Enter:
- Username
- Email (optional)
- Password (twice)

### Step 9: Run Server
```bash
python manage.py runserver
```

### Step 10: Access Application
- **Portfolio:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/

---

## Quick Setup Script (Optional)

Create a `setup.bat` (Windows) or `setup.sh` (macOS/Linux) file:

**setup.bat (Windows):**
```batch
@echo off
echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo Creating .env file...
if not exist .env (
    echo DJANGO_SECRET_KEY= > .env
    echo DJANGO_DEBUG=True >> .env
    echo DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1 >> .env
    echo .env file created. Please edit it and add your SECRET_KEY.
)

echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. Edit .env file and add SECRET_KEY
echo 2. Run: python manage.py makemigrations
echo 3. Run: python manage.py migrate
echo 4. Run: python manage.py createsuperuser
echo 5. Run: python manage.py runserver
pause
```

**setup.sh (macOS/Linux):**
```bash
#!/bin/bash
echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Creating .env file..."
if [ ! -f .env ]; then
    cat > .env << EOF
DJANGO_SECRET_KEY=
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
EOF
    echo ".env file created. Please edit it and add your SECRET_KEY."
fi

echo ""
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add SECRET_KEY"
echo "2. Run: python manage.py makemigrations"
echo "3. Run: python manage.py migrate"
echo "4. Run: python manage.py createsuperuser"
echo "5. Run: python manage.py runserver"
```

---

## What's Actually Required?

### Minimum Requirements:
1. **Python 3.8+** - The only thing that must be installed
2. **Internet connection** - To install packages via pip

### Automatically Created:
- `venv/` - Virtual environment (created by user)
- `.env` - Environment file (created by user)
- `db.sqlite3` - Database (created after migrations)
- `__pycache__/` - Python cache (auto-generated)
- `media/` - Upload folder (auto-created)

### No Installation Needed:
- ❌ No database server (uses SQLite)
- ❌ No web server (Django has built-in dev server)
- ❌ No additional frameworks
- ❌ No system dependencies

---

## Summary for Recipient

**What they need:**
- Python 3.8+ installed
- Extract ZIP file
- Follow 10 steps above

**What they DON'T need:**
- Database installation
- Web server
- Any other frameworks
- The .env or venv from your ZIP

**Time to setup:** ~5-10 minutes

---

## Troubleshooting for Recipient

**"python is not recognized"**
- Use `python3` instead
- Or install Python from python.org

**"pip is not recognized"**
- Use `python -m pip install -r requirements.txt`

**"ModuleNotFoundError"**
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt` again

**"Port 8000 already in use"**
- Use different port: `python manage.py runserver 8080`

---

## Best Practice: Create a README for Recipient

Include this in your ZIP:

```
QUICK START:
1. Extract this ZIP
2. Open terminal in extracted folder
3. Run: python -m venv venv
4. Activate: .\venv\Scripts\Activate.ps1 (Windows) or source venv/bin/activate (Mac/Linux)
5. Run: pip install -r requirements.txt
6. Create .env file (see SETUP_GUIDE.md)
7. Run: python manage.py migrate
8. Run: python manage.py createsuperuser
9. Run: python manage.py runserver
10. Open: http://127.0.0.1:8000/

See SETUP_GUIDE.md for detailed instructions.
```

