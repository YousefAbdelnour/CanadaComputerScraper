# Canada Computers Inventory Checker

A Python script to check the stock availability of select products on Canada Computers and send an SMS notification when they are available. The script uses web scraping, a progress bar, and SMS alerts.

## Reason for creation

I made this script because I am trying to buy the Nvidia RTX 5080, but scalper bots keep buying the online stock, so I made this scraper so I know if a graphics card is in store, so I can go quick to purchase it. 

I will not make a scalper bot, as it goes against my beliefs of fair purchase between customers and distaste of resellers.

## Features

- **Web Scraping**: Fetches product availability using `requests` and `BeautifulSoup`.
- **Stylized CLI**: Uses `rich` for a fancy progress bar, logging, and styled messages.
- **SMS Alerts**: Sends a text message to your phone when an item is in stock.
- **Error Handling**: Handles request errors and logs issues properly.

## Requirements

Ensure you have the following before running the script:

1. **Python 3.7+** installed on your system.
2. **A Twilio account** to send SMS notifications.
3. **A Twilio phone number** to send messages from.
4. **Your personal phone number** registered with Twilio for receiving messages.

## Installation

First, install the required Python packages using `pip`:

```bash
pip install requests beautifulsoup4 twilio rich
```

## Setup

### Twilio Configuration
1. **Create a Twilio account** at [Twilio](https://www.twilio.com/).
2. **Get your Account SID and Auth Token** from the Twilio dashboard.
3. **Purchase a Twilio phone number** (must support SMS).
4. **Update the script** with your Twilio credentials and phone numbers:

```python
TWILIO_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"
YOUR_PHONE_NUMBER = "your_personal_phone_number"
```

## Running the Script

After configuring your Twilio details, run the script:

```bash
python inventory_checker.py
```

## How It Works

1. The script scrapes the Canada Computers website for product availability.
2. A progress bar visually indicates the scanning process.
3. If any product is in stock, the script:
   - Prints a notification in the console.
   - Sends an SMS alert to your phone.
4. If no products are in stock, it simply logs the results.

## Example Output

```
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 🔍 Inventory Checker 🔍 ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Canada Computers Inventory Checker                                                                                                                                                                                                                                         │
│  Check product availability in real time!                                                                                                                                                                                                                                  │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── Starting Inventory Check ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[21:18:57] OUT OF STOCK → https://www.canadacomputers.com/en/powered-by-nvidia/269470/asus-rog-astral-geforce-rtx-5080-16gb-gddr7-quad-fan-force-rog-astral-rtx5080-16g-gaming.html                                                                              scraper.py:84
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── Inventory Check Complete ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── ❌ Out of Stock ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ No stock available.                                                                                                                                                                                                                                                        │
|                                                                                                                                                                                                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Notes

- Twilio may require you to verify your personal number before sending texts.
- Free Twilio accounts have limited usage and may append a promotional message to SMS.
- This script is intended for personal use and is not affiliated with Canada Computers.

## License

This project is licensed under the MIT License.

---

Goodluck! 🚀

