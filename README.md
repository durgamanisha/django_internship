Django Internship Assignment

A production-ready Django project featuring:

- **DRF APIs**: public + JWT-secured endpoints  
- **Celery** with Redis for background tasks  
- **Telegram Bot** integration using `python-telegram-bot`  
- Environment-variable management  
- Modular structure & Git history best practices  

---

Project Structure:
this is the project structure
django_internship/
├── django_internship/
│   ├── __init__.py
│   ├── settings.py
│   ├── celery.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tasks.py
├── telegram_bot/
│   ├── bot.py
│   └── views.py
├── manage.py
├── requirements.txt
└── README.md


