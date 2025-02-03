from flask import Flask, render_template, request, jsonify
import subprocess
import threading
import os

app = Flask(__name__)

def start_bot(api_id, api_hash, phone_number, target_username, group_id):
    """Runs the Telegram bot script as a subprocess."""
    bot_script = f"""
import re
from telethon import TelegramClient, events
import asyncio

client = TelegramClient('session/session_name', {api_id}, '{api_hash}')
target_username = '{target_username}'
sent_contracts = set()
solana_contract_pattern = re.compile(r'\\b[1-9A-HJ-NP-Za-km-z]{{32,44}}\\b')

group_id = {group_id}

async def main():
    await client.start(phone='{phone_number}')
    print("✅ Bot is running...")

    @client.on(events.NewMessage(chats=group_id))
    async def handler(event):
        message = event.message.message or ""
        contracts = solana_contract_pattern.findall(message)
        if contracts:
            for contract in contracts:
                if contract not in sent_contracts:
                    formatted_message = f"/buy {contract} 0.05"
                    await client.send_message(target_username, formatted_message)
                    sent_contracts.add(contract)
                    await asyncio.sleep(2)

    await client.run_until_disconnected()
asyncio.run(main())
    """
    os.makedirs("bot", exist_ok=True)
    with open("bot/bot_script.py", "w") as f:
        f.write(bot_script)
    
    subprocess.Popen(["python", "bot/bot_script.py"])  # Run bot script

@app.route('/')
def index():
    return render_template('index.html')  # Now, it only renders the existing file!

@app.route('/start_bot', methods=['POST'])
def start_bot_api():
    data = request.json
    threading.Thread(target=start_bot, args=(
        data['api_id'], data['api_hash'], data['phone_number'],
        data['target_username'], data['group_id']
    )).start()
    return jsonify({"status": "Bot started successfully"})

if __name__ == '__main__':
    os.makedirs("templates", exist_ok=True)  # Ensure templates folder exists
    os.makedirs("static", exist_ok=True)  # Ensure static folder exists
    app.run(debug=True)
