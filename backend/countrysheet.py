import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_address_format_by_country_name_sheet(country_name):
    ci_country = {}

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('data.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Country-wise-address-formats')
    sheet_instance = sheet.get_worksheet(0)
    records = sheet_instance.get_all_records()

    ci_country_l = find_country_record(records, country_name)
    if not ci_country_l:
        return 'Country name not found'

    populate_ci_country(ci_country, ci_country_l)

    insert_ci_country = generate_insert_query('CI_COUNTRY', ci_country)
    insert_ci_country_l = generate_insert_query('CI_COUNTRY_L', ci_country_l)

    return insert_ci_country, insert_ci_country_l

def find_country_record(records, country_name):
    for ci_country_l in records:
        if ci_country_l["DESCR"].lower() == country_name.lower():
            return ci_country_l
    return None

def populate_ci_country(ci_country, ci_country_l):
    for key, value in ci_country_l.items():
        if key == 'COUNTRY':
            ci_country['COUNTRY'] = value
        elif key == 'VERSION':
            ci_country['VERSION'] = value
        elif key in ['LANGUAGE_CD', 'DESCR']:
            continue
        elif value:
            ci_country[key[:-3] + 'AVAIL'] = 'Y'
            ci_country[key[:-3] + 'USG_FLG'] = 'OPT' if value.endswith('(Opt.)') else 'REQ'
        else:
            ci_country[key[:-3] + 'AVAIL'] = 'N'
            ci_country[key[:-3] + 'USG_FLG'] = 'NA'

def generate_insert_query(table_name, data):
    columns = ", ".join(data.keys())
    values = ", ".join(f"'{v}'" if isinstance(v, str) else str(v) for v in data.values())
    return f"INSERT INTO {table_name} ({columns}) VALUES ({values});"


# country_name = 'India'  # Replace with the desired country name
# address_format = get_address_format_by_country_name_sheet(country_name)
# print(address_format)