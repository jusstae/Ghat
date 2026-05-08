#!/usr/bin/env python3 

import subprocess
import sys
import os

# Git Commands  
COMMANDS = {
    "s": ["status"],
    "a": ["add", "."],
    "c": ["commit", "-m"],
    "p": ["push"],
    "init": ["init"],
    "pl": ["pull"],
    "co": ["checkout"],
    "cl": ["clone"],
    "b": ["branch"],
    "sw": ["switch"],   
    "d": ["diff"],
    "lg": ['logs'],
}
    
# Main Script
def run(cmd_parts):
    try:
        subprocess.run(["git"] + cmd_parts, check=True)
    except subprocess.CalledProcessError:
        print(f"Error: git {' '.join(cmd_parts) }")

def ghat():
    if len(sys.argv) < 2:
        print("Usage: ghat <command> [args]")
        return

    cmd = sys.argv[1]

    if cmd not in COMMANDS: # When we run and we dont get any arguments
        print(f"Unknown command: {cmd}")
        return
    
base = COMMANDS[cmd]

if cmd == "c":
    if len(sys.argv) < 3: # If argument is less then 3 we don't get a message to commit
        print("Commit message required")
        return
    message = ' '.join(sys.argv[2:])
    run(base + [message])
