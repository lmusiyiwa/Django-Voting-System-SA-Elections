# Copilot Instructions for Voting System

## Project Overview
**Voting System** is a Django-based South African political elections platform with three main features:
1. **Leader voting system** - Vote for and view political leaders
2. **News page** - Display political news and leaders
3. **Multilingual chatbot** - Support-oriented chatbot in 11 SA languages (English, Afrikaans, isiZulu, isiXhosa, Sesotho, Setswana, Sepedi, Xitsonga, Tshivenda, isiNdebele, SiSwati)

## Architecture

### Core Components

**Django Project Structure:**
- `voting_system/` - Main Django project (settings, URLs, WSGI)
- `vote/` - Primary app handling voting, leaders, and chatbot
- `models.py` (root) - Election/Position/Candidate/Voter/Vote models
- `vote/models.py` - Leader model for SA political leaders

**URL Routing:**
- `/` - Home page (redirects to news)
- `/news/` - Leaders and political news page
- `/chatbot/` - Multilingual support chatbot
- `/admin/` - Django admin for managing leaders

**Database:**
- SQLite (`db.sqlite3`) with models interconnected via ForeignKey relationships
- Key relationship: `Vote.voter` → `Voter` → `User` (Django auth)

### View Patterns

**Session-based State (Chatbot):**
- `request.session["language"]` - Tracks selected language (set on first user input)
- `request.session["conversation"]` - List of dicts with `{"sender": "bot"|"you", "text": "...", "new": bool}`
- `request.session["awaiting_yes_no"]` - Boolean flag for two-factor responses
- The `"new": True` flag triggers typing animations in templates

**Keyword Matching for Context:**
- Multilingual keyword lists map user input to resource types (food, shelter, safety, etc.)
- Affirmations and resources hardcoded in `vote/views.py` for mental health support
- Case-insensitive matching with language aliasing (e.g., "zulu" → "isiZulu")

## Critical Patterns

### Multilingual Implementation
- All response strings stored in `translations` dict organized by feature and language
- Keyword-based intent detection supports synonyms across 11 languages
- Language selection happens once per session; `language_aliases` handle user variations

### Django Admin Integration
- `Leader` model registered with `LeaderAdmin` showing name, party, website
- Leader photos uploaded to `/media/leaders/` (ImageField)
- No votes field currently—focus is on displaying leader profiles

### Media Handling
- `MEDIA_URL = "/media/"` and `MEDIA_ROOT` point to `media/` directory
- Leader photos stored as `leaders/` subdirectory
- Development: Media served via `static()` helper in `voting_system/urls.py`

## Developer Workflows

### Running the Server
```bash
python manage.py runserver
```

### Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating an Admin User
```bash
python manage.py createsuperuser
```

### Media/Static Files in Development
- Static files auto-served from `/static/` (CSS, JS, images)
- Media files auto-served from `/media/` (uploaded leader photos)
- No collectstatic needed for development

## Important Notes

### Chatbot Conversation Flow
1. **Initial**: Bot sends intro in English; user selects language
2. **Language Selected**: Bot shows menu of help categories (food, shelter, safety, etc.)
3. **User Request**: Bot detects keywords and returns relevant resource links
4. **Follow-up**: Bot asks "anything else?" → if yes, restart from step 2; if no, goodbye
5. **Recovery**: Unknown input repeats the current menu

### Common Pitfalls
- **Session State**: Always mark bot messages with `"new": False` before adding new ones (prevents re-animation)
- **Language Aliases**: User input is lowercased; ensure keyword lists match lowercase versions
- **Resource Links**: HTML in `translations["resources"]` includes Bootstrap button classes—preserve on edits
- **Duplicate Code**: `vote/views.py` has duplicated resource handling logic; consider refactoring to helper function

### Configuration
- Environment variables via `python-decouple` (e.g., `NEWS_API_KEY`)
- `.env` file loaded but `NEWS_API_KEY` currently unused in code
- `DEBUG = True` (development only—change for production)

## File References
- **Models**: `/vote/models.py` (Leader), `/models.py` (Election/Vote/Voter)
- **Views**: `/vote/views.py` (all three main views—news, chatbot, home)
- **Templates**: `/vote/templates/` (chatbot.html, sa_politics_news.html)
- **Admin**: `/vote/admin.py` (Leader registration)
- **Settings**: `/voting_system/settings.py` (DEBUG, MEDIA, STATIC, INSTALLED_APPS)

---

**Last Updated:** December 2, 2025 | **Branch:** loreen-work
