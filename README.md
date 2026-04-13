# Vidya Mandir — SSC & ICSE Coaching Institute Website

A professional Django-based website for a coaching institute specialising in SSC & ICSE education.

## Tech Stack
- **Backend:** Django 5.x (Python)
- **Database:** SQLite (default) — easily swappable with PostgreSQL
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Fonts:** Cormorant Garamond + Montserrat (Google Fonts)

## Project Structure
```
coaching_institute/
├── coaching_institute/       # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                     # Main Django app
│   ├── models.py             # StudentResult, Testimonial, ContactSubmission
│   ├── views.py              # All page views
│   ├── admin.py              # Admin panel config
│   └── urls.py               # URL routing
├── templates/core/           # HTML templates
│   ├── base.html             # Shared layout, navbar, footer
│   ├── home.html             # Homepage with hero, counters, toppers
│   ├── results.html          # Dynamic results with filter + pagination
│   ├── testimonials.html     # Student testimonials
│   ├── subjects.html         # Subjects taught
│   ├── about.html            # Teacher profile + timeline
│   └── contact.html          # Contact form
├── static/
│   ├── css/style.css         # Full design system
│   └── js/main.js            # Animations, counters, filters
└── db.sqlite3                # SQLite database (seeded with sample data)
```

## Quick Start

### 1. Install dependencies
```bash
pip install django
```

### 2. Run migrations
```bash
python manage.py migrate
```

### 3. Create admin user
```bash
python manage.py createsuperuser
```

### 4. Run the server
```bash
python manage.py runserver
```

### 5. Visit
- **Website:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/
  - Username: `admin` | Password: `admin123` *(change this!)*

## Pages
| URL | Description |
|-----|-------------|
| `/` | Homepage — hero, counters, toppers, testimonials |
| `/results/` | Student results with board/year filter + search |
| `/testimonials/` | All student testimonials |
| `/subjects/` | Subjects: Maths, Science, English |
| `/about/` | Teacher profile, timeline, philosophy |
| `/contact/` | Contact form (saves to DB) |
| `/admin/` | Django Admin — manage all data |

## Admin Panel — Managing Data

### Adding Student Results
1. Go to `/admin/` → **Student Results** → **Add**
2. Fill in: Name, Board (SSC/ICSE), Score (%), Year
3. Check **Is Topper** to feature on homepage
4. Set **Rank** (1/2/3) for medal display

### Adding Testimonials
1. Go to `/admin/` → **Testimonials** → **Add**
2. Check **Is Featured** to show on homepage

### Viewing Contact Submissions
1. Go to `/admin/` → **Contact Submissions**
2. Mark as **Is Read** after following up

## Switching to PostgreSQL
In `settings.py`, replace the DATABASES block:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vidyamandir_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Then run: `pip install psycopg2-binary && python manage.py migrate`

## Design System
- **Primary:** Deep Navy `#0a1628`
- **Accent:** Gold `#c9a84c`
- **Typography:** Cormorant Garamond (headings) + Montserrat (body/labels)
- **Fully responsive** — mobile, tablet, desktop

## Deployment (Production)
```bash
pip install gunicorn whitenoise
# Add 'whitenoise.middleware.WhiteNoiseMiddleware' to MIDDLEWARE in settings.py
# Set DEBUG = False and ALLOWED_HOSTS = ['yourdomain.com']
gunicorn coaching_institute.wsgi:application
```
