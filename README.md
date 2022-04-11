# TNT bot

## About The Project

Telegram bot's are awsome like Ngrok is awsome and Ttyd is awsome too!
So I made this bot that can run bash script's on your local machine
It's hackable! and you can add awsome bash script's too
In my senario I made htop with ttyd as a web service(you can put bash terminal as a web service!)

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* inside terminal
  ```sh
  apt install tmux curl torsocks jq htop ttyd ngrok
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free Bot API Key at [https://telegram.org](https://telegram.org)
2. Clone the repo
   ```sh
   git clone https://github.com/arsalanses/ttyd-ngrok-telegram-bot.git
   ```
3. Install python packages
   ```sh
   pip install -r requirements.txt
   ```
4. Enter your API token in `main.py`
   ```py
   TOKEN = 'ENTER YOUR API'
   ```
