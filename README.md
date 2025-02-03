🚀 1. System Requirements
Before you begin, ensure you have the following installed: ✅ Python 3.8+ (Download from python.org)
✅ Git (Download from git-scm.com)
✅ Pip (Automatically installed with Python)

📥 2. Installation Instructions
1️⃣ Clone the Repository
Open Command Prompt (Windows) / Terminal (Mac/Linux) and run:

git clone https://github.com/AlmonBot/AlmonBot.git
cd AlmonBot

Create a Virtual Environment (Optional but Recommended)
python -m venv venv

Activate it:

Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

3. Running the Application
1️⃣ Start the Flask Application
Run the following command:

python app.py

If everything is correct, you should see:

Running on http://127.0.0.1:5000/

Open your browser and go to:

http://127.0.0.1:5000/

⚙️ 4. How to Use the Control Panel
1️⃣ Fill in the Required Fields


Field Name	 / Description
API ID	- Get from my.telegram.org
API Hash	- Get from my.telegram.org
Phone Number	- Your Telegram phone number
Target Bot Username	 - The bot to send contract addresses to
Telegram Group ID	 - The group from which signals will be received

2️⃣ Click "Start Bot"
Once all fields are filled, press the Start Bot button. The bot will begin monitoring the specified Telegram group and send trade signals automatically.

❓ 5. FAQ & Troubleshooting
Q: Flask server is not starting, what should I do?
Ensure Python and Pip are installed correctly.
Run pip install -r requirements.txt to install dependencies.
Try python app.py again.
Q: "ModuleNotFoundError: No module named 'flask'"
Run:
pip install flask

Q: My bot isn't sending trade signals!
Double-check your API ID, API Hash, and Phone Number.
Ensure the Telegram Group ID is correct.
Try restarting the bot by stopping (Ctrl+C) and rerunning python app.py.

🔒 6. Security & Best Practices
⚠️ Do NOT share your API ID, API Hash, or phone number publicly.
⚠️ Use environment variables instead of hardcoding credentials in the script.
⚠️ Consider using a VPS to keep the bot running 24/7.

📜 7. License
This project is open-source under the MIT License.

💬 8. Support & Contribution
Have an issue? Open a GitHub issue at:
👉 GitHub Issues

Want to contribute? Fork the repo and submit a Pull Request.

![image](https://github.com/user-attachments/assets/77461cec-d2af-4250-9a64-19f5b7818ea0)




