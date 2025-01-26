import os
import requests
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    cron_url = os.getenv('CRON_URL')
    
    if not cron_url:
        logger.error("CRON_URL environment variable is not set")
        return
    
    try:
        logger.info(f"Making GET request to configured URL")
        response = requests.get(cron_url, timeout=10)
        response.raise_for_status()
        logger.info(f"Request successful - Status code: {response.status_code}")
        
    except requests.Timeout:
        logger.error("Request timed out after 10 seconds")
    except requests.RequestException as e:
        logger.error(f"Request failed: {str(e)}")

if __name__ == "__main__":
    main() 