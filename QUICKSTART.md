# Quick Start - Voting System

## 🚀 Get Running in 3 Steps

```bash
# 1. Migrate database
python manage.py migrate

# 2. Create admin user
python manage.py createsuperuser

# 3. Run server
python manage.py runserver
```

Then visit: **http://localhost:8000**

---

## 📍 Application Routes

| Route | Purpose | Auth Required |
|-------|---------|---|
| `/` | Home (redirects) | ❌ |
| `/login/` | User login | ❌ |
| `/logout/` | Logout confirmation | ✅ |
| `/news/` | Leaders & chatbot | ✅ |
| `/chatbot/` | Multilingual support | ✅ |
| `/results/` | Vote results | ✅ |
| `/admin/` | Django admin panel | ✅ Admin |

---

## 👥 Default Test Credentials

Create with: `python manage.py createsuperuser`

Example:
- Username: `admin`
- Password: `yourpassword`

---

## 🎮 User Experience Flow

```
Visitor
  ↓
Visit http://localhost:8000
  ↓
Redirected to /login/ (unauthenticated)
  ↓
Enter username/password
  ↓
Logged in → /news/ (leaders page)
  ↓
Can access: News, Chatbot, Results, Logout
```

---

## ⚙️ Key Settings

**Authentication:**
```python
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'news'
LOGOUT_REDIRECT_URL = 'login'
```

**Database:** SQLite (`db.sqlite3`)

**Static Files:** `/vote/static/`

**Media (Leader photos):** `/media/leaders/`

---

## 📝 Common Tasks

### Create Test Candidate

```bash
python manage.py shell

from vote.models import Election, Candidate
from datetime import datetime, timedelta

election = Election.objects.create(
    title="Test Election",
    start_date=datetime.now(),
    end_date=datetime.now() + timedelta(days=30)
)

Candidate.objects.create(
    name="Test Candidate",
    party="Test Party",
    election=election
)
```

### View Vote Count

```bash
python manage.py shell

from vote.models import Vote
print(f"Total votes: {Vote.objects.count()}")
```

### Add Leader via Admin

1. Go to: `http://localhost:8000/admin/`
2. Login with superuser credentials
3. Click "Leaders"
4. Click "Add Leader"
5. Fill in details and upload photo

---

## 🆘 Need Help?

See: `SETUP_GUIDE.md` for detailed troubleshooting
