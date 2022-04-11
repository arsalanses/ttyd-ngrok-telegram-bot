#!/usr/bin/bash

tmux new -d -s ttyd './ttyd.x86_64 -p 8080 -m 1 -R htop' #TODO: download ttyd in this directory
tmux split-window -h -t ttyd
tmux send-keys -t ttyd "./ngrok-stable-linux-amd64/ngrok http 8080" C-m #TODO: download ngrok in this directory

sleep 3

. torsocks off
NGROK_URLS=$(curl -s http://127.0.0.1:4040/api/tunnels | jq -r '.tunnels[0].public_url')
. torsocks on

TELEGRAM_TOKEN="<YOUR-BOT-TOKEN>" #TODO: set your bot token here
TELEGRAM_ID="<YOUR-ID>" #TODO: set your channel or user telegram id here
torsocks curl -s --data chat_id="${TELEGRAM_ID}" --data-urlencode "text=${NGROK_URLS}" "https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage?parse_mode=HTML" > telegram.log &

exit 1
