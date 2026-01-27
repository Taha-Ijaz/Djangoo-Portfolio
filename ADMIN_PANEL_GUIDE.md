# Django Admin Panel Guide

## Available Sections in Admin Panel

After logging in at `http://127.0.0.1:8000/admin/`, you'll see the following sections:

### 📋 Core Sections

1. **Bio**
   - Manage personal information
   - Fields: Full Name, Job Title, Profile Picture, Description, Email, Phone, LinkedIn, GitHub, Languages, Interests

2. **Education**
   - Add education entries
   - Fields: Degree, Institution, Start Date, End Date, Duration, Description

3. **Experience**
   - Add work experience
   - Fields: Title, Organization, Start Date, End Date, Duration, Description

4. **Skills**
   - Manage technical skills
   - Fields: Name, Category, Level (Beginner/Intermediate/Advanced/Expert)

5. **Projects**
   - Add portfolio projects
   - Fields: Title, Description, Technologies (Many-to-Many), Project Link, Image

6. **Technologies**
   - Manage technology tags for projects
   - Fields: Name

### 🎓 Additional Sections

7. **Certifications** ✅
   - Add certifications
   - Fields: Name, Organization, Issue Date, Expiry Date, Certificate URL
   - Features: Search by name/organization, Filter by organization/date

8. **Technical Expertise** ✅
   - Add technical expertise categories
   - Fields: Category, Description, Order (for display sorting)
   - Features: Editable order in list view, Search by category/description

9. **Technical Achievements** ✅
   - Add technical achievements
   - Fields: Title, Description, Icon (Font Awesome class), Order (for display sorting)
   - Features: Editable order in list view, Search by title/description
   - Icon examples: `fas fa-code`, `fas fa-trophy`, `fas fa-certificate`

---

## How to Access Admin Panel

1. **Start the server:**
   ```bash
   python manage.py runserver
   ```

2. **Go to:** http://127.0.0.1:8000/admin/

3. **Login** with your superuser credentials

---

## Quick Guide: Adding Content

### Adding a Certification:
1. Click on **Certifications** → **Add Certification**
2. Fill in:
   - Name: e.g., "Introduction to Programming"
   - Organization: e.g., "Online Learning Platform"
   - Issue Date: Select date
   - Expiry Date: (optional)
   - Certificate URL: (optional) Link to certificate
3. Click **Save**

### Adding Technical Expertise:
1. Click on **Technical Expertise** → **Add Technical Expertise**
2. Fill in:
   - Category: e.g., "Frontend Development"
   - Description: e.g., "Building responsive and interactive user interfaces"
   - Order: Lower numbers appear first (e.g., 1, 2, 3)
3. Click **Save**

### Adding Technical Achievement:
1. Click on **Technical Achievements** → **Add Technical Achievement**
2. Fill in:
   - Title: e.g., "100+ GitHub Contributions"
   - Description: e.g., "Active coding practice and project development"
   - Icon: e.g., `fas fa-code` (Font Awesome icon class)
   - Order: Lower numbers appear first
3. Click **Save**

---

## Font Awesome Icons for Technical Achievements

Common icon classes you can use:
- `fas fa-code` - Code icon
- `fas fa-trophy` - Trophy icon
- `fas fa-certificate` - Certificate icon
- `fas fa-star` - Star icon
- `fas fa-medal` - Medal icon
- `fas fa-award` - Award icon
- `fas fa-fire` - Fire icon
- `fas fa-rocket` - Rocket icon

**Note:** Use Font Awesome 6 icon classes (the site uses Font Awesome 6.4.0)

---

## Display Order

Both **Technical Expertise** and **Technical Achievements** have an `order` field:
- Lower numbers appear first
- You can edit the order directly in the list view
- Useful for organizing content by importance

---

## All Admin Sections Summary

| Section | Model Name | Key Fields |
|---------|-----------|------------|
| Bio | Bio | Name, Job Title, Profile Picture, Contact Info |
| Education | Education | Degree, Institution, Dates |
| Experience | Experience | Title, Organization, Dates |
| Skills | Skill | Name, Category, Level |
| Projects | Project | Title, Description, Technologies |
| Technologies | Technology | Name |
| **Certifications** | **Certification** | **Name, Organization, Dates** |
| **Technical Expertise** | **TechnicalExpertise** | **Category, Description, Order** |
| **Technical Achievements** | **TechnicalAchievement** | **Title, Description, Icon, Order** |

---

## Troubleshooting

**If sections don't appear:**
1. Make sure migrations are run: `python manage.py migrate`
2. Check that apps are in `INSTALLED_APPS` in `settings.py`
3. Verify admin files exist in each app folder
4. Restart the development server

**If you can't see the models:**
- Make sure you're logged in as a superuser
- Check that the models are registered in `admin.py` files
- Verify the app is in `INSTALLED_APPS`

