# ISS Tracker with Email Notification

This Python script tracks the International Space Station (ISS) using its API and sends an email notification when the ISS is overhead during nighttime.

## Features

- **ISS Tracking:** Utilizes the Open Notify API to track the current position of the ISS.
- **Day/Night Detection:** Determines if it's nighttime at your location using sunrise-sunset.org API.
- **Email Notification:** Sends an email notification when the ISS is overhead during nighttime.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)

## Setup

1. Clone the repository or download the script.
2. Install the Requests library if you haven't already: `pip install requests`.
3. Configure the script:
   - Set your latitude (`MY_LAT`) and longitude (`MY_LNG`) in the script to reflect your location.
   - Replace `EMAIL`, `PASSWORD`, and `EMAIL2` with your Gmail credentials and recipient email.
4. Ensure less secure apps access is enabled for your Gmail account if you're using Gmail for sending emails.

## Usage

1. Run the script: `python iss_tracker.py`.
2. The script will continuously monitor the ISS position.
3. You will receive an email notification when the ISS is overhead during nighttime.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

---
