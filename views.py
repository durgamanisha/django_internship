from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from telegram import Update, Bot
from .bot import start
import json
from django.conf import settings

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

@csrf_exempt
def webhook(request):
    payload = json.loads(request.body)
    update = Update.de_json(payload, bot)
    import asyncio
    asyncio.run(start(update, None))
    return HttpResponse(status=200)
