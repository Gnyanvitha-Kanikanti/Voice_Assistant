🎙️ Personal Voice Assistant
A Python-based voice assistant that provides weather updates, tells jokes, fetches news headlines, plays YouTube videos, and retrieves information from Wikipedia — all powered by voice commands!

🚀 Features

🔊 Text-to-Speech voice interaction

🎤 Speech Recognition input

🌦️ Real-time Weather Report

📰 Latest News Headlines

📹 Play YouTube Videos via voice

🌐 Wikipedia-based Information Search

😂 Random Jokes (via Joke API)

🧠 Technologies Used

Python 3.x

speech_recognition

pyttsx3

requests

selenium

webdriver-manager

newsapi-python

📁 Project Structure

├── main.py              # Main voice assistant script

├── weather.py           # Weather report using OpenWeather API

├── news.py              # News headlines from NewsAPI

├── jokes.py             # Joke fetching from Joke API

├── seleniumweb.py       # Wikipedia search via Selenium

├── ut_script.py         # YouTube video playback via Selenium


🎤 Sample Voice Commands
“What's the weather like?”

“Tell me a joke.”

“Give me the latest news.”

“Play video [your topic]”

“Give me information about [your topic]”

📌 Notes

Ensure a working microphone for voice input.

Google Chrome and ChromeDriver are required for Selenium-based features.

The assistant uses Wikipedia and YouTube through browser automation.

