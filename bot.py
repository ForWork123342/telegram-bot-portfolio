#!/usr/bin/env python3

"""
Telegram Bot for Educational Purposes
Copyright (c) 2025 ForWork123342

This code is provided for educational purposes only.
You are free to use, modify and distribute it for learning purposes.
No commercial use allowed without explicit permission.

THE SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND.
"""



from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

async def main():
    # Get bot token from user input
    token = input("Please enter your Telegram bot token: ").strip()
    
    if not token:
        print("Error: Token cannot be empty!")
        return
    
    # Initialize bot and dispatcher
    bot = Bot(token=token)
    dp = Dispatcher()
    
    @dp.message(Command(commands=['start', 'help']))
    async def send_welcome(message: Message):
        """Send welcome message and a joke"""
        await message.answer(
            "👋 Привет! Я бот, который знает программистские шутки.\n\n"
            "Вот одна из них:\n"
            "🤖 Почему программисты путают Хэллоуин и Рождество?\n"
            "🎃 Потому что Oct 31 == Dec 25! 🎄"
        )
    
    @dp.message(Command(commands=['joke']))
    async def send_joke(message: Message):
        """Send a random programming joke"""
        jokes = [
            "🤓 Как называют программиста, который не любит кофе? Decaf developer.",
            "💘 Почему программисты такие хорошие любовники? Потому что они знают, как обрабатывать исключения!",
            "💡 Сколько программистов нужно, чтобы поменять лампочку? Ни одного, это hardware проблема!",
            "🐍 Почему Python не смог завести себе девушку? Потому что у него не было классов!",
            "🧠 Чем отличается хороший программист от плохого? Хороший думает, что знает 5% всего. Плохой - 95%."
        ]
        import random
        await message.answer(random.choice(jokes))
    
    print("🤖 Bot is running... Press Ctrl+C to stop")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())