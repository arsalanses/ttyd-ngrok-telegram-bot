#!/usr/bin/bash
tmux new -d -s telegram
tmux send-keys -t telegram "source ../venv/bin/activate" C-m
tmux send-keys -t telegram "torsocks python3 ../main.py" C-m

