import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 8080))
bot = telebot.TeleBot(BOT_TOKEN)


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")

    def log_message(self, format, *args):
        pass


def run_health_server():
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
    server.serve_forever()


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "дарова пёс!")


if __name__ == "__main__":
    threading.Thread(target=run_health_server, daemon=True).start()
    bot.infinity_polling(timeout=3600)
