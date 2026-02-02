# 🤖 Telegram Stock BOT (Python)

## 📝 Description
This is a real-time **Stock Monitoring Bot** developed in Python. It leverages **Selenium WebDriver** for browser automation to check product availability on e-commerce websites dynamically. Once a change in stock status is detected, the bot instantly notifies the user via the **Telegram Bot API**.

The project is a practical example of combining web scraping, asynchronous programming with `asyncio`, and third-party API integration to solve real-world automation tasks.

---

## 🌟 Key Features
* **Automated Web Inspection:** Uses Selenium to navigate to product pages and verify stock status via XPath.
* **Instant Telegram Alerts:** Sends immediate notifications to your mobile device when a product becomes available.
* **Asynchronous Execution:** Built with `asyncio` for efficient, non-blocking operations and customizable check intervals.
* **Error Handling:** Includes basic exception handling to notify the user if page structures change or connection issues occur.

---

## 🏗️ Project Structure
* **`check_stock()`**: The core logic that navigates to the target URL and evaluates specific web elements to determine stock availability.
* **`send_message()`**: An asynchronous wrapper for the Telegram Bot API to send text alerts.
* **`main()`**: An infinite loop that coordinates the monitoring process at defined time intervals.

---

## 🛠️ Technologies Used
* **Language:** Python
* **Browser Automation:** Selenium WebDriver
* **Messaging API:** `python-telegram-bot`
* **Concurrency:** `asyncio`

## 🚀 How to Run

1. **Prerequisites:**
   * Install Python 3.x.
   * Install dependencies: `pip install selenium python-telegram-bot`.
   * Download the correct **ChromeDriver** that matches your Chrome browser version.

2. **Configuration:**
   * Open the script and replace `TOKEN` with your Telegram Bot token.
   * Replace `CHAT_ID` with your unique Telegram chat ID.
   * Update the `url` and `By.XPATH` variables to match the product and site you wish to monitor.

3. **Execution:**
   ```bash
   python stokBot.py
