import json
import os
from holiday import get_holidays

CONFIG_FILE = 'config_data.json'

def load_config():
    """Load the JSON config file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            return json.load(file)
    else:
        return {}

def save_config(config):
    """Save the JSON config file."""
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file, indent=4)

def get_or_update_work_cal(country, year, version="version_1"):
    """Retrieve or update the work calendar configuration for a country and year."""
    config = load_config()
    
    c2m_data = config.setdefault("C2M", {}).setdefault(version, {}).setdefault("work_cal", {})
    country_year_key = f"{country}_{year}"

    if country_year_key in c2m_data:
        print("Accessing in previously fetched data")
        return c2m_data[country_year_key]
    else:
        holidays = get_holidays(country, year)  
        print("Accessed API")

        c2m_data[country_year_key] = {
            "holidays": holidays
            # "weekends": ["Saturday", "Sunday"]  # Example weekends, could be dynamic
        }
        save_config(config)
        return c2m_data[country_year_key]

# config = get_or_update_work_cal("IN", 2022)
# print(config)
