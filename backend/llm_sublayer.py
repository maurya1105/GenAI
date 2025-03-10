
import logging, json
import object_categories
from datetime import datetime

OBJECT_CONTEXT= object_categories.OBJECT_CONTEXTS

def classify_query_object_category(model, query):
    object_list = '\n    - '.join(OBJECT_CONTEXT.keys())
    prompt = f"""Your task is to classify the below query into one of the objects it is trying to configure. Focus solely on what object is being asked to configure not its specification.
    
    ###Example###
    if asked "configure work calendar for the country india"
    Answer: WORK_CALENDAR
    Answer wont be COUNTRY even though it is mentioned. Understand english grammar and always provide output as the object name which is asked to configure by user.
    ######
    
    
    Output should only be the category name.
 
    Query: {query}
 
    Objects:
    - {object_list}
    
    """
    print(prompt)
    try:
        object_name = model.invoke(prompt)
        object_name = object_name.strip()  # Remove extra whitespace
        if object_name in OBJECT_CONTEXT:
            logging.debug(f"Object detected: {object_name}")
            return object_name, OBJECT_CONTEXT[object_name]  # Return both the category and its context
        else:
            logging.error(f"Invalid object category returned: {object_name}")
            return None, None
    except Exception as e:
        logging.error(f"Error classifying the query into an object: {e}")
        return None, None

def work_cal_country_extract(model, query):

    # Define the prompt with Python code to handle the current year logic
    prompt = f"""
    Classify the following query into its respective country and year. If the country is mentioned, return its ISO 3166-1 alpha-2 country code (e.g., "US" for the United States, "IN" for India). If the country is not mentioned, return "null" for the country. For the year, if it is explicitly mentioned, extract the year as a four-digit number. If the year is not mentioned, return "null" for the year. Return the result as a JSON object with the following format:

    ```json
    {{
    "country": "<ISO_country_code_or_null>",
    "year": "<year_or_null>"
    }}
    Note that the year should always be in string and not int.
    
    Query to be classified: {query}
    """
    response = model.invoke(prompt)
    # print(response)
    
    # Strip any extraneous whitespace or characters
    response = response.strip()

    # Try to find and extract the JSON portion
    try:
        json_start = response.find("{")
        json_end = response.rfind("}") + 1
        if json_start != -1 and json_end != -1:
            json_str = response[json_start:json_end]
            # print("Extracted JSON string:", json_str)
            logging.info(f"Extracted json string from subquery LLM response: {json_str}")

            response_json = json.loads(json_str)

            # Extract country and year from the JSON
            country = response_json.get("country", "").strip()
            year = response_json.get("year", "").strip()

            # If no country is mentioned, return "null"
            if not country or country =="null":
                return None

            # If no year is mentioned, use the current year
            if not year or year =="null":
                year = str(datetime.now().year)

            return country, year

        else:
            raise ValueError("No JSON object found in the response")

    except (json.JSONDecodeError, ValueError, AttributeError) as e:
        print("Error decoding JSON response:", e)
        return None, None
    
def extract_country_from_query(model, query):
    prompt = f"""Your task is to extract and return the **full name** of the country mentioned in the query below in a structured JSON format. 
1. Only return the **full name** of the country if it is given as an abbreviation, short form, or alias. For example:
   - 'UAE' → 'United Arab Emirates'
   - 'USA' → 'United States' 
   - 'UK' → 'United Kingdom'
2. If the country name is already written in its commonly recognized full name (e.g., 'India', 'France', 'Germany'), return it as-is, without converting it to its legal or official title.
3. If no country is mentioned or the country name is ambiguous, return the following JSON:
```json
{{
  "country": null
}}
```
4. Do not include any additional information, explanations, or extra text. Only return the JSON.

The JSON format must be:
```json
{{
  "country": "<full_country_name>"
}}
```

Query: {query}
    """
    response = model.invoke(prompt)
    response = response.strip()
    try:
        json_start = response.find("{")
        json_end = response.rfind("}") + 1
        if json_start != -1 and json_end != -1:
            json_str = response[json_start:json_end]
            # print("Extracted JSON string:", json_str)
            logging.info(f"Extracted json string from subquery LLM response: {json_str}")

            response_json = json.loads(json_str)

            # Extract country and year from the JSON
            country_name = response_json.get("country", "").strip()
            if not country_name or country_name =="null":
                return None
            
            logging.debug(f"Country detected by LLM: {country_name}")
            return country_name.strip() 
        else:
            raise ValueError("No JSON object found in the response")
    except Exception as e:
        logging.error(f"Error detecting country: {e}")
        return None