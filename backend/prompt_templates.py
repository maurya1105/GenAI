# prompt_templates.py

PROMPT_TEMPLATE = [
    #c2m_info
    """
    Conversation History: 
    {history} 
    -------------
                                    
    You are a knowledgeable assistant and a SQL database and relations expert.
    
    Your task is to answer the following question about C2M by interpreting the context given below.
    
    Context: 
    {context}                   
    
    Question: {question}
    
    Answer in detail:
    """,
    #db_info
    """ 
    Conversation History: 
    {history} 
    -------------
                        
    You are a knowledgeable assistant and a SQL database and relations expert.
    
    Your task is to answer the following question by interpreting metadata and configuration instructions to accurately read, understand or update the database. 
    
    Schema Information:
    {context}
    
    Question: {question}
    
    Answer in detail:
    """,
    #db_config_help
    """
                       
    Conversation History: 
    {history}
                       
    You are a knowledgeable assistant and a SQL database and relations expert. Your task is to interpret metadata and configuration instructions to accurately read, understand or update the database tables by generating field values. Follow these guidelines:
    
    1. Identify the tables asked to configure and generate values for all field names in the table using INSERT format.
    2. Also update parent and child tables keeping primary and foreign keys in mind, Eg: If you are configuring a child table its primary key comes from the parent table, the parent table row should also be inserted. Similarly all child tables should also update accordingly.
    3. Provide complete and detailed answers without using ellipses ("..."). (If you're asked for 100 rows you will give 100 rows of data. Don't be lazy.)
    4. Avoid unnecessary conversation and stick to the point.
    
    Stick to this Schema Information:
    {context}            
    
    Use precise table and field names as provided in the schema. Match whole name for table names and field names. For example, if the table name is "users" it is not the same as "user".
    
    ##RULES##
        -Use the YYYY-MM-DD format for dates.
        -All rows to be added must be in insert query format and all rows values must be generated by you. Do not provide logic code for it. Provide direct INSERT query with multiple rows. 
        -English language is used 'ENG'.
        -The default value of 'VERSION' is 99999.
                                    
    Question: {question}
    
    Answer in detail:
    """,
    #follow_up_q
    """
                       
    Conversation History: (Never show the user this)
    {history}
             
    Question: {question}
    
    Stick to the point and answer the question:
    """,
    
    #work_cal_country_pt1
    """
                       
    Conversation History: 
    {history}
                       
    You are a knowledgeable assistant and a SQL database and relations expert. Your task is to interpret metadata and configuration instructions to accurately read, understand or update the database tables by generating field values. Follow these guidelines:
    
    1. Identify the tables asked to configure and generate values for all field names in the table using INSERT format.
    2. Also update parent and child tables keeping primary and foreign keys in mind, Eg: If you are configuring a child table its primary key comes from the parent table, the parent table row should also be inserted. Similarly all child tables should also update accordingly.
    3. Provide complete and detailed answers without using ellipses ("..."). (If you're asked for 100 rows you will give 100 rows of data. Don't be lazy.)
    4. Avoid unnecessary conversation and stick to the point.
    
    Stick to this Schema Information:

Fill the below 2 tables 'CI_CAL_WORK' and 'CI_CAL_WORK_L' with 1 row each for each work calendar configuration asked in the query.

Table 'CI_CAL_WORK' is used for storing Work Calendar. Table 'CI_CAL_WORK' has 9 fields (columns) which are:  1. 'CALENDAR_CD' 2. 'SUN' 3. 'MON' 4. 'TUE' 5. 'WED' 6. 'THU' 7. 'FRI' 8. 'VERSION' 9. 'SAT'. Out of these fields, only one is a primary key; 'CALENDAR_CD' is the primary key for 'CI_CAL_WORK'
'CI_CAL_WORK' is a Primary Table. This table is for the weekly working days, hence for each CALENDAR_CD type we will only insert 1 row. Fill in the days as Yes or No depending on the configuration asked.

Field Descriptions for table 'CI_CAL_WORK':

  1. 'CALENDAR_CD' (CHAR):- field name for Work Calendar
  2. 'SUN' (CHAR):- field name for Sunday (Yes 'Y' or No 'N')
  3. 'MON' (CHAR):- field name for Monday (Yes 'Y' or No 'N')
  4. 'TUE' (CHAR):- field name for Tuesday (Yes 'Y' or No 'N')
  5. 'WED' (CHAR):- field name for Wednesday (Yes 'Y' or No 'N')
  6. 'THU' (CHAR):- field name for Thursday (Yes 'Y' or No 'N')
  7. 'FRI' (CHAR):- field name for Friday (Yes 'Y' or No 'N')
  8. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default':  99999
  9. 'SAT' (CHAR):- field name for Saturday (Yes 'Y' or No 'N')

The child tables of 'CI_CAL_WORK' are ['CI_CAL_HOL', 'CI_CAL_HOL_L', 'CI_CAL_WORK_L']. 
(Generated when 'MAINT_OBJ_CD'=WORK CAL)

--------------------------------------------------------------------------

Table 'CI_CAL_WORK_L' is used for storing Work Calendar Language. Table 'CI_CAL_WORK_L' has 4 fields (columns) which are:  1. 'CALENDAR_CD' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'CALENDAR_CD'  2. 'LANGUAGE_CD' . 
Table 'CI_CAL_WORK_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'CALENDAR_CD' is foreign key from table 'CI_CAL_WORK'.
'CI_CAL_WORK_L' is a child table of 'CI_CAL_WORK' table.

Field Descriptions for table 'CI_CAL_WORK_L':

  1. 'CALENDAR_CD' (CHAR):- field name for Work Calendar
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description of work calendar object
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default':  99999

--------------------------------------------------------------------------      
    
    Use precise table and field names as provided in the schema. Match whole name for table names and field names. For example, if the table name is "users" it is not the same as "user".
    
    ##RULES##
        -Use the YYYY-MM-DD format for dates.
        -All rows to be added must be in insert query format and all rows values must be generated by you. Do not provide logic code for it. Provide direct INSERT query with multiple rows. 
        -English language is used 'ENG'.
        -The default value of 'VERSION' is 99999.
                                    
    Question: {question}

    Answer in detail:
    """,
    #work_cal_country_pt2
    """
                       
    Conversation History: 
    {history}
                       
    You are a knowledgeable assistant and a SQL database and relations expert. Your task is to interpret metadata and configuration instructions to accurately read, understand or update the database tables by generating field values. Follow these guidelines:
    
    1. Identify the tables asked to configure and generate values for all field names in the table using INSERT format.
    2. Also update parent and child tables keeping primary and foreign keys in mind, Eg: If you are configuring a child table its primary key comes from the parent table, the parent table row should also be inserted. Similarly all child tables should also update accordingly.
    3. Provide complete and detailed answers without using ellipses ("..."). (If you're asked for 100 rows you will give 100 rows of data. Don't be lazy.)
    4. Avoid unnecessary conversation and stick to the point.
    
    Stick to this Schema Information:

    Fill the below 2 tables 'CI_CAL_HOL' and 'CI_CAL_HOL_L' with multiple rows for all the holidays you can think of in a year with respect to the configuration needed.

Table 'CI_CAL_HOL' is used for storing Work Calendar Holidays. Table 'CI_CAL_HOL' has 5 fields (columns) which are:  1. 'HOLIDAY_DT' 2. 'CALENDAR_CD' 3. 'VERSION' 4. 'F1_HOLIDAY_START_DTTM' 5. 'F1_HOLIDAY_END_DTTM'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'CALENDAR_CD'  2. 'HOLIDAY_DT' . 
Table 'CI_CAL_HOL' has only one foreign key; 'CALENDAR_CD' is a foreign key from table 'CI_CAL_WORK'.
'CI_CAL_HOL' is a child table of 'CI_CAL_WORK' table.

Here we have to take into account all the yearly recurring holidays for the configuration needed. 

Field Descriptions for table 'CI_CAL_HOL':
  1. 'HOLIDAY_DT' (DATE):- field name for Holiday Date
  2. 'CALENDAR_CD' (CHAR):- field name for Work Calendar
  3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default':  99999
  4. 'F1_HOLIDAY_START_DTTM' (DATE):- field name for Holiday Start Date, 'nullable': True
  5. 'F1_HOLIDAY_END_DTTM' (DATE):- field name for Holiday End Date, 'nullable': True

--------------------------------------------------------------------------

Table 'CI_CAL_HOL_L' is used for storing Work Calendar Holidays Language. Table 'CI_CAL_HOL_L' has 5 fields (columns) which are:  1. 'CALENDAR_CD' 2. 'HOLIDAY_DT' 3. 'LANGUAGE_CD' 4. 'HOLIDAY_NAME' 5. 'VERSION'. Out of these fields, 3 are primary keys. The composite primary keys are:  1. 'CALENDAR_CD'  2. 'HOLIDAY_DT'  3. 'LANGUAGE_CD' . 
Table 'CI_CAL_HOL_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'HOLIDAY_DT' is foreign key from table 'CI_CAL_HOL'.
'CI_CAL_HOL_L' is a child table of 'CI_CAL_WORK' table.

Here we have to take into account all the holidays for the configuration needed. Keep in mind the regular yearly holidays celebrated for the particular configuration asked and output multiple rows for several holidays.

Field Descriptions for table 'CI_CAL_HOL_L':

  1. 'CALENDAR_CD' (CHAR):- field name for Work Calendar
  2. 'HOLIDAY_DT' (DATE):- field name for Holiday Date
  3. 'LANGUAGE_CD' (CHAR):- field name for Language
  4. 'HOLIDAY_NAME' (VARCHAR2):- field name for the Holiday Name
  5. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default':  99999

---------------------------------------------------------------------------           
    
    Use precise table and field names as provided in the schema. Match whole name for table names and field names. For example, if the table name is "users" it is not the same as "user".
    
    ##RULES##
        -Use the YYYY-MM-DD format for dates.
        -All rows to be added must be in insert query format and all rows values must be generated by you. Do not provide logic code for it. Provide direct INSERT query with multiple rows. 
        -English language is used 'ENG'.
        -The default value of 'VERSION' is 99999.
                                    
    Question: {question}

    Here is the holiday json for the country:
    {context}

    Provide SQL insert queries for tables 'CI_CAL_HOL' and 'CI_CAL_HOL_L' with all holidays provided.

    Answer in detail:
    """
]
