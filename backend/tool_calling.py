from langchain_community.llms.ollama import Ollama
from countrysheet import get_address_format_by_country_name_sheet
from apistate import get_states_by_country_name_api

llm = Ollama(model = "llama3:instruct")

from langchain_core.tools import tool

@tool
def config_table(input : int) -> str:
    """configure any object type apart from country"""
    return f"Configuring table with input: {input}"

@tool
def country_config(country : str) -> str:
    """Configures the country specified."""
    insert_ci_country, insert_ci_country_l = get_address_format_by_country_name_sheet(country)
    response=f"""
Response:  Here are the two SQL INSERT queries for country {country}:

**CI_COUNTRY_L**

sql
{insert_ci_country_l}


CI_COUNTRY_L contains labels for address fields.

**CI_COUNTRY**

sql
{insert_ci_country}


CI_COUNTRY contains usage flags (required, not allowed, optional) and availability values (yes, no) for address fields. If a field's usage is REQ or OPT, _AVAIL should be Y. If NA, _AVAIL should be N.

"""         
    states_country = get_states_by_country_name_api(country)
    response+=f"Here are the two SQL INSERT queries for the states in country {country}:\n\n**CI_STATE**\nsql\n{states_country[0]}\n\n**CI_STATE_L**\nsql\n{states_country[1]}\n\nNumber of states in country {country}: {states_country[2]}"
    return response

from langchain.tools.render import render_text_description
rendered = render_text_description([config_table, country_config])
print(rendered)

from langchain_core.prompts import ChatPromptTemplate

System = f"""You are an assistant that has access to the following tools. Here are the name and description of the tool:

{rendered}

Given the user input, return the name and input of the tool to use. Return your response as a JSON blob with 'name' and 'arguments' keys. Also make sure to return arguments value as dictionary. Do not return any other text data."""


prompt = ChatPromptTemplate.from_messages([("system", System), ("user", "{input}")])

print("prompt:", prompt)

from langchain_core.output_parsers import JsonOutputParser

def selector(response):
    print("response: ", response)
    if response["name"]=="country_config":
        return globals()[response["name"]](response["arguments"])
    else:
        return globals()[response["name"]](input)

chain = prompt | llm | JsonOutputParser() | selector

# print(chain.invoke({"input" : "what is 3 multiplied by 4."}))

print(chain.invoke({"input" : "configure country india"}))

print(chain.invoke({"input" : "configure table premise"}))
