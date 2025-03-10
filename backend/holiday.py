import requests
import os
# from dotenv import load_dotenv

# load_dotenv()

def get_holidays(country, year):
    # Base URL for the holidays endpoint
    url = "https://calendarific.com/api/v2/holidays"
    api_key = os.getenv("CALENDARIFIC_API_KEY")

    # Parameters for the API request
    params = {
        'api_key': api_key,  
        'country': country,  
        'year': year ,      
        'type': 'national' 
    }

    try:
        # Sending the GET request to the API
        response = requests.get(url, params=params)
        
        # If the request was successful, check the status code
        if response.status_code == 200:
            holidays = response.json().get('response', {}).get('holidays', [])
            
            if holidays:
      
                holiday_list = []
                
                for holiday in holidays:
                    holiday_list.append({
                        "name": holiday['name'],
                        "date": holiday['date']['iso']
                    })

                return holiday_list
            else:
                return [f"No holidays found for {country} in {year}."]
        else:
            # If there was an error, return the error code and message
            return f"Error: {response.status_code} - {response.text}"
    
    except Exception as e:
        print(f"An error occurred: {e}")


# if __name__ == "__main__":
#     country = "IN"  # ISO country code for the United States
#     year = 2024     # The year you want to check

#     holiday_list=get_holidays(country, year)
#     print(holiday_list)
