# Render Cron Job

A simple cron job service that makes GET requests to a specified URL. Designed to run on Render.com's cron job service.

## Setup

### Requirements
- Python 3.x
- `requests` library

### Environment Variables
- `CRON_URL`: The URL to send GET requests to

### Render Configuration

1. Create a new **Cron Job** service on Render
2. Configure the following settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python cron_job.py`
   - Add environment variable `CRON_URL` with your target URL

### Local Development

1. Clone this repository
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip3 install -r requirements.txt`
5. Set the CRON_URL environment variable:
   - Windows Command Prompt: `set CRON_URL=https://your-url.com`
   - Windows PowerShell: `$env:CRON_URL = "https://your-url.com"`
   - Unix/MacOS/Linux: `export CRON_URL=https://your-url.com`
6. Run the script: `python3 cron_job.py`

## Logging

The script includes basic logging that will show:
- When requests are made
- Successful responses with status codes
- Errors (including timeouts and request failures)

Logs can be viewed in the Render dashboard.

## Timeout

The script has a 10-second timeout for requests. If the target URL doesn't respond within this time, the request will be aborted and logged as an error. 