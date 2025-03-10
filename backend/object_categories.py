OBJECT_CONTEXTS={
    "BILL_CYCLE": """
Table 'CI_BILL_CYC' is used for storing Bill Cycle - CCB. Table 'CI_BILL_CYC' has 3 fields (columns) which are:  1. 'BILL_CYC_CD' 2. 'VERSION' 3. 'CIS_DIVISION'. Out of these fields, only one is a primary key; 'BILL_CYC_CD' is the primary key for 'CI_BILL_CYC'. 
Table 'CI_BILL_CYC' has only one foreign key; 'CIS_DIVISION' is a foreign key from table 'CI_CIS_DIVISION'.
'CI_BILL_CYC' is a Primary Table.

Field Descriptions for table 'CI_BILL_CYC':

  1. 'BILL_CYC_CD' (CHAR):- field name for Bill Cycle
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, default: 99999
  3. 'CIS_DIVISION' (CHAR):- field name for CIS Division, default: '-'

The child tables of 'CI_BILL_CYC' are ['CI_BILL_CYC_L', 'CI_BILL_CYC_SCH']. 
(Generated when 'MAINT_OBJ_CD'=BILL CYCLE)

--------------------------------------------------------------------------

Table 'CI_BILL_CYC_L' is used for storing Bill Cycle Language - CCB. Table 'CI_BILL_CYC_L' has 4 fields (columns) which are:  1. 'BILL_CYC_CD' 2. 'LANGUAGE_CD' 3. 'VERSION' 4. 'DESCR'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'BILL_CYC_CD'  2. 'LANGUAGE_CD' . 
Table 'CI_BILL_CYC_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'BILL_CYC_CD' is foreign key from table 'CI_BILL_CYC'.
'CI_BILL_CYC_L' is a child table of 'CI_BILL_CYC' table.

Field Descriptions for table 'CI_BILL_CYC_L':

  1. 'BILL_CYC_CD' (CHAR):- field name for Bill Cycle
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, default: 99999
  4. 'DESCR' (VARCHAR2):- field name for Description

--------------------------------------------------------------------------

Table 'CI_BILL_CYC_SCH' is used for storing Bill Cycle Schedule - CCB. Table 'CI_BILL_CYC_SCH' has 7 fields (columns) which are:  1. 'FREEZE_COMPLETE_SW' 2. 'VERSION' 3. 'BILL_CYC_CD' 4. 'WIN_START_DT' 5. 'WIN_END_DT' 6. 'ACCOUNTING_DT' 7. 'EST_DT'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'BILL_CYC_CD'  2. 'WIN_START_DT' . 
Table 'CI_BILL_CYC_SCH' has only one foreign key; 'BILL_CYC_CD' is a foreign key from table 'CI_BILL_CYC'.
'CI_BILL_CYC_SCH' is a child table of 'CI_BILL_CYC' table.

Field Descriptions for table 'CI_BILL_CYC_SCH':

  1. 'FREEZE_COMPLETE_SW' (CHAR):- field name for Freeze and Complete, default: ‘Y’
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, default: 99999
  3. 'BILL_CYC_CD' (CHAR):- field name for Bill Cycle, default: ‘XX'
  4. 'WIN_START_DT' (DATE):- field name for Window Start Date
  5. 'WIN_END_DT' (DATE):- field name for Window End Date
  6. 'ACCOUNTING_DT' (DATE):- field name for Accounting Date,  'precision': None, 'nullable': True, default: (same value as 'WIN_START_DT')
  7. 'EST_DT' (DATE):- field name for Estimate Date,  'precision': None, 'nullable': True, default: (same value as 'WIN_END_DT')

  
IMP Note:- Only 1 row needs to be added in CI_BILL_CYC and CI_BILL_CYC_L since only one primary key BILL_CYC_CD='XX'.
-Give the exact number of bill cycles asked, dont be afraid to do the work. It is illegal to skip rows, generate all values.
-Multiple rows (bill cycles) need to be added in CI_BILL_CYC_SCH, but only 1 row needs to be added in CI_BILL_CYC and CI_BILL_CYC_L since only one primary key BILL_CYC_CD='XX'
-Bill cyles must be continous ie the next bill cycle should start with the last one's end date. (First bill cycle is always the start date given)
---------------------------------------------------------------------------
""",

    "MAINTENANCE_OBJECT": """
Table 'CI_MD_MO' is used for storing Maintenance Object. Table 'CI_MD_MO' has 7 fields (columns) which are:  1. 'MAINT_OBJ_CD' 2. 'VERSION' 3. 'PROG_COM_ID' 4. 'OWNER_FLG' 5. 'PM_PROG_COM_ID' 6. 'UI_PROG_COM_ID' 7. 'SVC_NAME'. Out of these fields, only one is a primary key; 'MAINT_OBJ_CD' is the primary key for 'CI_MD_MO'. 
Table 'CI_MD_MO' has 3 foreign keys as listed:  'UI_PROG_COM_ID' is foreign key from table 'CI_MD_PRG_COM', 'PROG_COM_ID' is foreign key from table 'CI_MD_PRG_COM', and 'PM_PROG_COM_ID' is foreign key from table 'CI_MD_PRG_COM'.
'CI_MD_MO' is a Primary Table.

Field Descriptions for table 'CI_MD_MO':

  1. 'MAINT_OBJ_CD' (CHAR):- field name for Maintenance Object
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  3. 'PROG_COM_ID' (CHAR):- field name for Program Com ID
  4. 'OWNER_FLG' (CHAR):- field name for Owner
  5. 'PM_PROG_COM_ID' (CHAR):- field name for Page
  6. 'UI_PROG_COM_ID' (CHAR):- field name for UI Page
  7. 'SVC_NAME' (CHAR):- field name for Service Name

The child tables of 'CI_MD_MO' are ['CI_MD_MO_L', 'CI_MD_MO_OPT', 'CI_MD_MO_TBL', 'CI_MD_MO_ALG']. 
(Generated when 'MAINT_OBJ_CD'=MAIN OBJ)

--------------------------------------------------------------------------

Table 'CI_MD_MO_L' is used for storing Maintenance Object Language. Table 'CI_MD_MO_L' has 5 fields (columns) which are:  1. 'MAINT_OBJ_CD' 2. 'LANGUAGE_CD' 3. 'VERSION' 4. 'DESCR' 5. 'OWNER_FLG'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'MAINT_OBJ_CD'  2. 'LANGUAGE_CD' . 
Table 'CI_MD_MO_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'MAINT_OBJ_CD' is foreign key from table 'CI_MD_MO'.
'CI_MD_MO_L' is a child table of 'CI_MD_MO' table.

Field Descriptions for table 'CI_MD_MO_L':

  1. 'MAINT_OBJ_CD' (CHAR):- field name for Maintenance Object
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  4. 'DESCR' (VARCHAR2):- field name for Description
  5. 'OWNER_FLG' (CHAR):- field name for Owner

--------------------------------------------------------------------------

Table 'CI_MD_MO_OPT' is used for storing Maintenance Object Option. Table 'CI_MD_MO_OPT' has 6 fields (columns) which are:  1. 'MAINT_OBJ_CD' 2. 'MAINT_OBJ_OPT_FLG' 3. 'SEQ_NUM' 4. 'MAINT_OBJ_OPT_VAL' 5. 'VERSION' 6. 'OWNER_FLG'. Out of these fields, 4 are primary keys. The composite primary keys are:  1. 'MAINT_OBJ_CD'  2. 'MAINT_OBJ_OPT_FLG'  3. 'SEQ_NUM'  4. 'MAINT_OBJ_OPT_VAL' . 
Table 'CI_MD_MO_OPT' has only one foreign key; 'MAINT_OBJ_CD' is a foreign key from table 'CI_MD_MO'.
'CI_MD_MO_OPT' is a child table of 'CI_MD_MO' table.

Field Descriptions for table 'CI_MD_MO_OPT':

  1. 'MAINT_OBJ_CD' (CHAR):- field name for Maintenance Object
  2. 'MAINT_OBJ_OPT_FLG' (CHAR):- field name for Maintenance Object Option Type
  3. 'SEQ_NUM' (NUMBER):- field name for Sequence,  'precision': 3
  4. 'MAINT_OBJ_OPT_VAL' (VARCHAR2):- field name for Maintenance Object Option Value
  5. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  6. 'OWNER_FLG' (CHAR):- field name for Owner

--------------------------------------------------------------------------

Table 'CI_MD_MO_TBL' is used for storing Maintenance Object Table. Table 'CI_MD_MO_TBL' has 9 fields (columns) which are:  1. 'MAINT_OBJ_CD' 2. 'TBL_NAME' 3. 'PRNT_CONST_ID' 4. 'OWNER_FLG' 5. 'TBL_ROLE_FLG' 6. 'COMPARE_TYP_FLG' 7. 'VERSION' 8. 'LIST_PROG_COM_ID' 9. 'PRNT_OWNER_FLG'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'MAINT_OBJ_CD'  2. 'TBL_NAME' . 
Table 'CI_MD_MO_TBL' has 4 foreign keys as listed:  'PRNT_CONST_ID' is foreign key from table 'CI_MD_CONST', 'LIST_PROG_COM_ID' is foreign key from table 'CI_MD_PRG_COM', 'TBL_NAME' is foreign key from table 'CI_MD_TBL', and 'MAINT_OBJ_CD' is foreign key from table 'CI_MD_MO'.
'CI_MD_MO_TBL' is a child table of 'CI_MD_MO' table.

Field Descriptions for table 'CI_MD_MO_TBL':

  1. 'MAINT_OBJ_CD' (CHAR):- field name for Maintenance Object
  2. 'TBL_NAME' (CHAR):- field name for Table
  3. 'PRNT_CONST_ID' (CHAR):- field name for Parent Constraint ID
  4. 'OWNER_FLG' (CHAR):- field name for Owner
  5. 'TBL_ROLE_FLG' (CHAR):- field name for Table Role
  6. 'COMPARE_TYP_FLG' (CHAR):- field name for Compare Method
  7. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  8. 'LIST_PROG_COM_ID' (CHAR):- field name for Program Com ID
  9. 'PRNT_OWNER_FLG' (CHAR):- field name for Constraint Owner

--------------------------------------------------------------------------

Table 'CI_MD_MO_ALG' is used for storing Maintenance Object Algorithm. Table 'CI_MD_MO_ALG' has 6 fields (columns) which are:  1. 'MAINT_OBJ_CD' 2. 'MAINT_OBJ_SEVT_FLG' 3. 'SEQ_NUM' 4. 'ALG_CD' 5. 'VERSION' 6. 'OWNER_FLG'. Out of these fields, 4 are primary keys. The composite primary keys are:  1. 'ALG_CD'  2. 'SEQ_NUM'  3. 'MAINT_OBJ_CD'  4. 'MAINT_OBJ_SEVT_FLG' . 
Table 'CI_MD_MO_ALG' has 2 foreign keys as listed:  'ALG_CD' is foreign key from table 'CI_ALG', and 'MAINT_OBJ_CD' is foreign key from table 'CI_MD_MO'.
'CI_MD_MO_ALG' is a child table of 'CI_MD_MO' table.

Field Descriptions for table 'CI_MD_MO_ALG':

  1. 'MAINT_OBJ_CD' (CHAR):- field name for Maintenance Object
  2. 'MAINT_OBJ_SEVT_FLG' (CHAR):- field name for Maintenance Object System Event
  3. 'SEQ_NUM' (NUMBER):- field name for Sequence,  'precision': 3
  4. 'ALG_CD' (CHAR):- field name for Algorithm
  5. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  6. 'OWNER_FLG' (CHAR):- field name for Owner
---------------------------------------------------------------------------

""",
    "PREMISE_TYPE": """
Table 'CI_PREM_TYPE' is used for storing Premise Type. Table 'CI_PREM_TYPE' has 3 fields (columns) which are:  1. 'PREM_TYPE_CD' 2. 'VERSION' 3. 'ALLOW_CIS_DIV_FLG'. Out of these fields, only one is a primary key; 'PREM_TYPE_CD' is the primary key for 'CI_PREM_TYPE'
'CI_PREM_TYPE' is a Primary Table.

Field Descriptions for table 'CI_PREM_TYPE':

  1. 'PREM_TYPE_CD' (CHAR):- field name for Premise Type, usually a short form
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, default: 99999
  3. 'ALLOW_CIS_DIV_FLG' (CHAR):- field name for Allow CIS Division

The child tables of 'CI_PREM_TYPE' are ['CI_PREM_TYPE_L']. 
(Generated when 'MAINT_OBJ_CD'=PREM TYPE)

--------------------------------------------------------------------------

Table 'CI_PREM_TYPE_L' is used for storing Premise Type Language. Table 'CI_PREM_TYPE_L' has 4 fields (columns) which are:  1. 'PREM_TYPE_CD' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'PREM_TYPE_CD'  2. 'LANGUAGE_CD' . 
Table 'CI_PREM_TYPE_L' has 2 foreign keys as listed:  'PREM_TYPE_CD' is foreign key from table 'CI_PREM_TYPE', and 'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE'.
'CI_PREM_TYPE_L' is a child table of 'CI_PREM_TYPE' table.

Field Descriptions for table 'CI_PREM_TYPE_L':

  1. 'PREM_TYPE_CD' (CHAR):- field name for Premise Type
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, default: 99999

---------------------------------------------------------------------------
""",
    "PHONE_TYPE": """
Table 'CI_PHONE_TYPE' is used for storing Phone Type. Table 'CI_PHONE_TYPE' has 4 fields (columns) which are:  1. 'PHONE_TYPE_CD' 2. 'PHONE_FMT_ALG_CD' 3. 'VERSION' 4. 'PHONE_TYPE_FLG'. Out of these fields, only one is a primary key; 'PHONE_TYPE_CD' is the primary key for 'CI_PHONE_TYPE'. 
Table 'CI_PHONE_TYPE' has only one foreign key; 'PHONE_FMT_ALG_CD' is a foreign key from table 'CI_ALG'.
'CI_PHONE_TYPE' is a Primary Table.

Field Descriptions for table 'CI_PHONE_TYPE':

  1. 'PHONE_TYPE_CD' (CHAR):- field name for Phone Type
  2. 'PHONE_FMT_ALG_CD' (CHAR):- field name for Phone Number Format Algorithm
  3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, default: 99999
  4. 'PHONE_TYPE_FLG' (CHAR):- field name for Phone Type Flag

The child tables of 'CI_PHONE_TYPE' are ['CI_PHONE_TYPE_L']. 
(Generated when 'MAINT_OBJ_CD'=PHONE TYPE)

--------------------------------------------------------------------------

Table 'CI_PHONE_TYPE_L' is used for storing Phone Type Language. Table 'CI_PHONE_TYPE_L' has 4 fields (columns) which are:  1. 'PHONE_TYPE_CD' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'LANGUAGE_CD'  2. 'PHONE_TYPE_CD' . 
Table 'CI_PHONE_TYPE_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'PHONE_TYPE_CD' is foreign key from table 'CI_PHONE_TYPE'.
'CI_PHONE_TYPE_L' is a child table of 'CI_PHONE_TYPE' table.

Field Descriptions for table 'CI_PHONE_TYPE_L':

  1. 'PHONE_TYPE_CD' (CHAR):- field name for Phone Type
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

---------------------------------------------------------------------------
""",
    "CURRENCY": """
Table 'CI_CURRENCY_CD' is used for storing Currency Code. Table 'CI_CURRENCY_CD' has 6 fields (columns) which are:  1. 'CURRENCY_CD' 2. 'CUR_SYMBOL' 3. 'DECIMAL_POSITIONS' 4. 'SCALE_POSITIONS' 5. 'VERSION' 6. 'CUR_POS_FLG'. Out of these fields, only one is a primary key; 'CURRENCY_CD' is the primary key for 'CI_CURRENCY_CD'
'CI_CURRENCY_CD' is a Primary Table.

Field Descriptions for table 'CI_CURRENCY_CD':

  1. 'CURRENCY_CD' (CHAR):- field name for Currency Code of the country
  2. 'CUR_SYMBOL' (CHAR):- field name for Symbol of currency ($,₹.. etc)
  3. 'DECIMAL_POSITIONS' (NUMBER):- field name for Decimal Positions,  'precision': 1
  4. 'SCALE_POSITIONS' (NUMBER):- field name for Scale Positions,  'precision': 3
  5. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, default: 99999
  6. 'CUR_POS_FLG' (CHAR):- field name for Currency Symbol Position (Prefix 'PR' or Suffix 'SF')

The child tables of 'CI_CURRENCY_CD' are ['CI_CURRENCY_CD_L']. 
(Generated when 'MAINT_OBJ_CD'=CURR CODE)

--------------------------------------------------------------------------

Table 'CI_CURRENCY_CD_L' is used for storing Currency Code Language. Table 'CI_CURRENCY_CD_L' has 4 fields (columns) which are:  1. 'CURRENCY_CD' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'CURRENCY_CD'  2. 'LANGUAGE_CD' . 
Table 'CI_CURRENCY_CD_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'CURRENCY_CD' is foreign key from table 'CI_CURRENCY_CD'.
'CI_CURRENCY_CD_L' is a child table of 'CI_CURRENCY_CD' table.

Field Descriptions for table 'CI_CURRENCY_CD_L':

  1. 'CURRENCY_CD' (CHAR):- field name for Currency Code
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description (Country and currency name)
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

---------------------------------------------------------------------------
""",
    "CUSTOMER_CONTACT_TYPE": """
Table 'CI_CC_TYPE' is used for storing Customer Contact Type. Table 'CI_CC_TYPE' has 11 fields (columns) which are:  1. 'CC_CL_CD' 2. 'CC_TYPE_CD' 3. 'CC_ACTION_FLG' 4. 'LTR_TMPL_CD' 5. 'VERSION' 6. 'CIS_DIVISION' 7. 'CC_PER_FLG' 8. 'CC_ACCT_FLG' 9. 'CC_PREM_FLG' 10. 'ENTITY_REL_FLG' 11. 'CUSTOM_ARCH_ELIG_CRIT_FLG'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'CC_TYPE_CD'  2. 'CC_CL_CD' . 
Table 'CI_CC_TYPE' has 3 foreign keys as listed:  'LTR_TMPL_CD' is foreign key from table 'CI_LETTER_TMPL', 'CC_CL_CD' is foreign key from table 'CI_CC_CL', and 'CIS_DIVISION' is foreign key from table 'CI_CIS_DIVISION'.
'CI_CC_TYPE' is a Primary Table.

Field Descriptions for table 'CI_CC_TYPE':

  1. 'CC_CL_CD' (CHAR):- field name for Contact Class
  2. 'CC_TYPE_CD' (CHAR):- field name for Contact Type
  3. 'CC_ACTION_FLG' (CHAR):- field name for Contact Action, default: 'LT'
  4. 'LTR_TMPL_CD' (CHAR):- field name for Letter Template
  5. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, default: 99999
  6. 'CIS_DIVISION' (CHAR):- field name for CIS Division, default: '-'
  7. 'CC_PER_FLG' (CHAR):- field name for Person Usage, default: 'OPTL'
  8. 'CC_ACCT_FLG' (CHAR):- field name for Account Usage, default: 'OPTL'
  9. 'CC_PREM_FLG' (CHAR):- field name for Premise Usage, default: 'OPTL'
  10. 'ENTITY_REL_FLG' (CHAR):- field name for Entity Relationship, default: 'NONE'
  11. 'CUSTOM_ARCH_ELIG_CRIT_FLG' (CHAR):- field name for Custom Archive Eligibility Criteria, default: 'NAPP'

The child tables of 'CI_CC_TYPE' are ['CI_CHTY_CCTY', 'CI_CC_TYPE_L']. 
(Generated when 'MAINT_OBJ_CD'=CUST CNT TYP)

--------------------------------------------------------------------------

Table 'CI_CHTY_CCTY' is used for storing Customer Contact Type Template Characteristics. Table 'CI_CHTY_CCTY' has 14 fields (columns) which are:  1. 'CC_CL_CD' 2. 'CC_TYPE_CD' 3. 'CHAR_TYPE_CD' 4. 'REQUIRED_SW' 5. 'DEFAULT_SW' 6. 'SORT_SEQ' 7. 'CHAR_VAL' 8. 'ADHOC_CHAR_VAL' 9. 'CHAR_VAL_FK1' 10. 'CHAR_VAL_FK2' 11. 'CHAR_VAL_FK3' 12. 'CHAR_VAL_FK4' 13. 'CHAR_VAL_FK5' 14. 'VERSION'. Out of these fields, 3 are primary keys. The composite primary keys are:  1. 'CC_TYPE_CD'  2. 'CHAR_TYPE_CD'  3. 'CC_CL_CD' . 
Table 'CI_CHTY_CCTY' has 2 foreign keys as listed:  'CHAR_TYPE_CD' is foreign key from table 'CI_CHAR_TYPE', and 'CC_TYPE_CD' is foreign key from table 'CI_CC_TYPE'.
'CI_CHTY_CCTY' is a child table of 'CI_CC_TYPE' table.

Field Descriptions for table 'CI_CHTY_CCTY':

  1. 'CC_CL_CD' (CHAR):- field name for Contact Class
  2. 'CC_TYPE_CD' (CHAR):- field name for Contact Type
  3. 'CHAR_TYPE_CD' (CHAR):- field name for Characteristic Type
  4. 'REQUIRED_SW' (CHAR):- field name for Required, default: 'N'
  5. 'DEFAULT_SW' (CHAR):- field name for Default, default: 'N'
  6. 'SORT_SEQ' (NUMBER):- field name for Sequence,  'precision': 2
  7. 'CHAR_VAL' (CHAR):- field name for Characteristic Value
  8. 'ADHOC_CHAR_VAL' (VARCHAR2):- field name for Adhoc Characteristic Value, default: '-'
  9. 'CHAR_VAL_FK1' (VARCHAR2):- field name for Characteristic Value FK 1, default: '-'
  10. 'CHAR_VAL_FK2' (VARCHAR2):- field name for Characteristic Value FK 2, default: '-'
  11. 'CHAR_VAL_FK3' (VARCHAR2):- field name for Characteristic Value FK 3, default: '-'
  12. 'CHAR_VAL_FK4' (VARCHAR2):- field name for Characteristic Value FK 4, default: '-'
  13. 'CHAR_VAL_FK5' (VARCHAR2):- field name for Characteristic Value FK 5, default: '-'
  14. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, default: 99999

--------------------------------------------------------------------------

Table 'CI_CC_TYPE_L' is used for storing Customer Contact Type Language. Table 'CI_CC_TYPE_L' has 6 fields (columns) which are:  1. 'CC_CL_CD' 2. 'CC_TYPE_CD' 3. 'LANGUAGE_CD' 4. 'DESCR' 5. 'VERSION' 6. 'CC_SHORT_NOTE'. Out of these fields, 3 are primary keys. The composite primary keys are:  1. 'LANGUAGE_CD'  2. 'CC_CL_CD'  3. 'CC_TYPE_CD' . 
Table 'CI_CC_TYPE_L' has 2 foreign keys as listed:  'CC_CL_CD' is foreign key from table 'CI_CC_TYPE', and 'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE'.
'CI_CC_TYPE_L' is a child table of 'CI_CC_TYPE' table.

Field Descriptions for table 'CI_CC_TYPE_L':

  1. 'CC_CL_CD' (CHAR):- field name for Contact Class
  2. 'CC_TYPE_CD' (CHAR):- field name for Contact Type
  3. 'LANGUAGE_CD' (CHAR):- field name for Language
  4. 'DESCR' (VARCHAR2):- field name for Description
  5. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, default: 99999
  6. 'CC_SHORT_NOTE' (VARCHAR2):- field name for Contact Type Shorthand, default: '-'

""",
    "COUNTRY": """

Table 'CI_COUNTRY' is used for storing Country format usage flags and availability values. Table 'CI_COUNTRY' has 28 fields (columns) which are:  1. 'CITY_AVAIL' 2. 'VERSION' 3. 'NUM1_AVAIL' 4. 'NUM2_AVAIL' 5. 'HOUSE_TYPE_AVAIL' 6. 'COUNTY_AVAIL' 7. 'STATE_AVAIL' 8. 'POSTAL_AVAIL' 9. 'IN_CITY_LIM_AVAIL' 10. 'GEO_CODE_AVAIL' 11. 'ADDR1_USG_FLG' 12. 'ADDR2_USG_FLG' 13. 'ADDR3_USG_FLG' 14. 'ADDR4_USG_FLG' 15. 'CITY_USG_FLG' 16. 'COUNTY_USG_FLG' 17. 'GEO_CODE_USG_FLG' 18. 'HOUSE_TYPE_USG_FLG' 19. 'IN_CITY_LIM_USG_FLG' 20. 'NUM1_USG_FLG' 21. 'NUM2_USG_FLG' 22. 'POSTAL_USG_FLG' 23. 'STATE_USG_FLG' 24. 'COUNTRY' 25. 'ADDR1_AVAIL' 26. 'ADDR2_AVAIL' 27. 'ADDR3_AVAIL' 28. 'ADDR4_AVAIL'. Out of these fields, only one is a primary key; 'COUNTRY' is the primary key for 'CI_COUNTRY'
'CI_COUNTRY' is a Primary Table.

Field Descriptions for table 'CI_COUNTRY':

  1. 'COUNTRY' (CHAR):- field name for Country
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, default: 99999
  3. 'NUM1_AVAIL' (CHAR):- field name for Number 1
  4. 'NUM2_AVAIL' (CHAR):- field name for Number 2
  5. 'HOUSE_TYPE_AVAIL' (CHAR):- field name for House Type
  6. 'COUNTY_AVAIL' (CHAR):- field name for County
  7. 'CITY_AVAIL' (CHAR):- field name for City
  8. 'STATE_AVAIL' (CHAR):- field name for State
  9. 'POSTAL_AVAIL' (CHAR):- field name for Postal
  10. 'IN_CITY_LIM_AVAIL' (CHAR):- field name for In City Limit
  11. 'ADDR1_AVAIL' (CHAR):- field name for Address 1
  12. 'ADDR2_AVAIL' (CHAR):- field name for Address 2
  13. 'ADDR3_AVAIL' (CHAR):- field name for Address 3
  14. 'ADDR4_AVAIL' (CHAR):- field name for Address 4
  15. 'GEO_CODE_AVAIL' (CHAR):- field name for Geographic Code
  16. 'ADDR1_USG_FLG' (CHAR):- field name for Address 1 Usage
  17. 'ADDR2_USG_FLG' (CHAR):- field name for Address 2 Usage
  18. 'ADDR3_USG_FLG' (CHAR):- field name for Address 3 Usage
  19. 'ADDR4_USG_FLG' (CHAR):- field name for Address 4 Usage
  20. 'CITY_USG_FLG' (CHAR):- field name for City Usage
  21. 'COUNTY_USG_FLG' (CHAR):- field name for County Usage
  22. 'GEO_CODE_USG_FLG' (CHAR):- field name for Geographic Code Usage
  23. 'HOUSE_TYPE_USG_FLG' (CHAR):- field name for House Type Usage
  24. 'IN_CITY_LIM_USG_FLG' (CHAR):- field name for In City Limit Usage
  25. 'NUM1_USG_FLG' (CHAR):- field name for Number 1 Usage
  26. 'NUM2_USG_FLG' (CHAR):- field name for Number 2 Usage
  27. 'POSTAL_USG_FLG' (CHAR):- field name for Postal Usage
  28. 'STATE_USG_FLG' (CHAR):- field name for State Usage


The child tables of 'CI_COUNTRY' are ['CI_STATE_L', 'CI_STATE', 'CI_COUNTRY_L']. 
(Generated when 'MAINT_OBJ_CD'=COUNTRY)

--------------------------------------------------------------------------

Table 'CI_COUNTRY_L' is used for storing Country address format labels. Table 'CI_COUNTRY_L' has 17 fields (columns) which are:  1. 'COUNTRY' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'ADDR1_LBL' 5. 'ADDR2_LBL' 6. 'ADDR3_LBL' 7. 'ADDR4_LBL' 8. 'CITY_LBL' 9. 'NUM1_LBL' 10. 'NUM2_LBL' 11. 'HOUSE_TYPE_LBL' 12. 'COUNTY_LBL' 13. 'STATE_LBL' 14. 'POSTAL_LBL' 15. 'IN_CITY_LIM_LBL' 16. 'GEO_CODE_LBL' 17. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'LANGUAGE_CD'  2. 'COUNTRY' . 
Table 'CI_COUNTRY_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'COUNTRY' is foreign key from table 'CI_COUNTRY'.
'CI_COUNTRY_L' is a child table of 'CI_COUNTRY' table.

Field Descriptions for table 'CI_COUNTRY_L':

  1. 'COUNTRY' (CHAR):- field name for Country
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description
  4. 'ADDR1_LBL' (VARCHAR2):- field name for Address 1
  5. 'ADDR2_LBL' (VARCHAR2):- field name for Address 2
  6. 'ADDR3_LBL' (VARCHAR2):- field name for Address 3
  7. 'ADDR4_LBL' (VARCHAR2):- field name for Address 4
  8. 'CITY_LBL' (VARCHAR2):- field name for City
  9. 'NUM1_LBL' (VARCHAR2):- field name for Number 1
  10. 'NUM2_LBL' (VARCHAR2):- field name for Number 2
  11. 'HOUSE_TYPE_LBL' (VARCHAR2):- field name for House Type
  12. 'COUNTY_LBL' (VARCHAR2):- field name for County
  13. 'STATE_LBL' (VARCHAR2):- field name for State
  14. 'POSTAL_LBL' (VARCHAR2):- field name for Postal or PIN code
  15. 'IN_CITY_LIM_LBL' (VARCHAR2):- field name for In City Limit
  16. 'GEO_CODE_LBL' (VARCHAR2):- field name for Geographic Code
  17. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, default: 99999

IMP NOTE:- Keep in mind standard postal address format for the country asked to configure.  Every country won't use all the address fields. The fields that aren't used must be reflected in CI_COUNTRY table.
-'CI_COUNTRY' contains usage flags of whether those fields are required for the particular country or not, whereas, 'CI_COUNTRY_L' contains labels for the fields.
-CI_COUNTRY table should be populated with all 28 fields containing _USG_FLG and _AVAIL values for all address fields.
-The field names ending with '_USG_FLG' have 3 usage values 'REQ'-Required, 'NA'-Not Allowed, 'OPT'-Optional.
-The field names ending with '_AVAIL' have 2 values 'Y'-Yes and 'N'-No.
-If a field's usage is 'REQ', its corresponding `_AVAIL` value should be 'Y'. If a field's usage is 'OPT', its corresponding `_AVAIL` value should be 'Y'. If a field's usage is 'NA', its corresponding `_AVAIL` value should be 'N'. 
-CI_COUNTRY_L table should be populated with 17 fields containing address labels for the fields.
-If a particular field's usage is NA, just insert its label as ('').
-Using ellipses(...) is illegal. Generate all values and don't be lazy.
-Output should have insert queries to all 4 tables.

--------------------------------------------------------------------------

Table 'CI_STATE_L' is used for storing State Language. Table 'CI_STATE_L' has 5 fields (columns) which are:  1. 'STATE' 2. 'COUNTRY' 3. 'LANGUAGE_CD' 4. 'DESCR' 5. 'VERSION'. Out of these fields, 3 are primary keys. The composite primary keys are:  1. 'COUNTRY'  2. 'STATE'  3. 'LANGUAGE_CD' . 
Table 'CI_STATE_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'STATE' is foreign key from table 'CI_STATE'.
'CI_STATE_L' is a child table of 'CI_COUNTRY' table.

Field Descriptions for table 'CI_STATE_L':

  1. 'STATE' (CHAR):- field name for State (2-letter Short code)
  2. 'COUNTRY' (CHAR):- field name for Country (3-letter Short code)
  3. 'LANGUAGE_CD' (CHAR):- field name for Language
  4. 'DESCR' (VARCHAR2):- field name for full name of the State
  5. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, default: 99999

--------------------------------------------------------------------------

Table 'CI_STATE' is used for storing State. Table 'CI_STATE' has 3 fields (columns) which are:  1. 'STATE' 2. 'COUNTRY' 3. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'STATE'  2. 'COUNTRY' . 
Table 'CI_STATE' has only one foreign key; 'COUNTRY' is a foreign key from table 'CI_COUNTRY'.
'CI_STATE' is a child table of 'CI_COUNTRY' table.

Field Descriptions for table 'CI_STATE':

  1. 'STATE' (CHAR):- field name for State (2-letter Short code)
  2. 'COUNTRY' (CHAR):- field name for Country (3-letter Short code)
  3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, default: 99999

---------------------------------------------------------------------------

""",
    "CHARACTERISTIC_TYPE": """
Use the below steps when asked to create a characteristic type value:

Steps for configuration of char type:
1. Configure table CI_CHAR_TYPE and generate values for all 9 fields:
   a) CHAR_TYPE_CD: the primary key 
   b) Determine whether the characteristic is of adhoc value (ADV), predefined value (DFV) or of foreign key value (FKV), this value goes into CHAR_TYPE_FLG
   c) ADHOC_VAL_ALG_CD: If adhoc; fill an algorithm name as its value, else; leave the field blank. 
   d) SEARCH_FLG: has values of ALWD and NALW.
   e) CUSTOM_SW: has values of Y and N.
   f) FK_REF_CD: fill in only when it is of foreign key value type
   g) FLD_NAME: fill in only when field name specified
   h) VERSION: 99999 (default)
   i) OWNER_FLG: Usually the first two letters of CHAR_TYPE_CD (eg: CI, CM, D1 etc)
   (Insert query should have 9 columns)
2. Fill in CI_CHAR_TYPE_L with same CHAR_TYPE_CD since that is the primary key. CI_CHAR_TYPE_L has 5 columns:- CHAR_TYPE_CD, LANGUAGE_CD, DESCR, VERSION, OWNER_FLG.
3. If characteristic is of predefined value type; fill in the 2 tables; CI_CHAR_VAL and CI_CHAR_VAL_L with multiple rows of predefined values. Else if characteristic is of adhoc or foreign key type; dont generate query.
   CI_CHAR_VAL has 4 columns:- CHAR_TYPE_CD, CHAR_VAL, VERSION and OWNER_FLG
   CI_CHAR_VAL_L has 6 columns:- CHAR_TYPE_CD, CHAR_VAL, DESCR, VERSION, OWNER_FLG and LANGUAGE_CD
4. Generate sql insert query for table CI_CHAR_ENTITY.

Always answer in format: INSERT INTO table_name (col1,col2..) VALUES (val1, val2..). Never stray away from the table definition given in schema or else the sql queries wont work.
""",
    "PERSON_RELATION_TYPE": """

These tables store relationship between people.

Table 'CI_PER_REL_TYPE' is used for storing Person Relationship Type. Table 'CI_PER_REL_TYPE' has 2 fields (columns) which are:  1. 'PER_REL_TYPE_CD' 2. 'VERSION'. Out of these fields, only one is a primary key; 'PER_REL_TYPE_CD' is the primary key for 'CI_PER_REL_TYPE'
'CI_PER_REL_TYPE' is a Primary Table.

Field Descriptions for table 'CI_PER_REL_TYPE':

  1. 'PER_REL_TYPE_CD' (CHAR):- field name for Relationship Type
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999

The child tables of 'CI_PER_REL_TYPE' are ['CI_PER_REL_TYPE_L']. 
(Generated when 'MAINT_OBJ_CD'=PER REL TYPE)

--------------------------------------------------------------------------

Table 'CI_PER_REL_TYPE_L' is used for storing Person Relationship Type Language. Table 'CI_PER_REL_TYPE_L' has 5 fields (columns) which are:  1. 'PER_REL_TYPE_CD' 2. 'LANGUAGE_CD' 3. 'DESCR12' 4. 'DESCR21' 5. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'PER_REL_TYPE_CD'  2. 'LANGUAGE_CD' . 
Table 'CI_PER_REL_TYPE_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'PER_REL_TYPE_CD' is foreign key from table 'CI_PER_REL_TYPE'.
'CI_PER_REL_TYPE_L' is a child table of 'CI_PER_REL_TYPE' table.

Field Descriptions for table 'CI_PER_REL_TYPE_L':

  1. 'PER_REL_TYPE_CD' (CHAR):- field name for Relationship Type
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR12' (VARCHAR2):- field name for Description (Person 1=>Person 2)
  4. 'DESCR21' (VARCHAR2):- field name for Description (Person 2=>Person 1)
  5. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999

---------------------------------------------------------------------------
""",
    "IDENTIFIER_TYPE": """
To configure an identifier type:

Identifier types are used for identification of a person via documents like SSN, PAN, Aadhar etc. 

Table 'CI_ID_TYPE' is used for storing Identifier Type. Table 'CI_ID_TYPE' has 10 fields (columns) which are:  1. 'ID_TYPE_CD' 2. 'VERSION' 3. 'ID_FMT_ALG_CD' 4. 'VAL_ID_TYPE_FOR_DUPS_FLG' 5. 'BUS_OBJ_CD' 6. 'ID_PREFIX_FLG' 7. 'FIELD_NAME' 8. 'DELIMITER' 9. 'ALLOW_PRIMARY_FLG' 10. 'BO_DATA_AREA'. Out of these fields, only one is a primary key; 'ID_TYPE_CD' is the primary key for 'CI_ID_TYPE'. 
Table 'CI_ID_TYPE' has 3 foreign keys as listed:  'ID_FMT_ALG_CD' is foreign key from table 'CI_ALG', 'BUS_OBJ_CD' is foreign key from table 'F1_BUS_OBJ', and 'FIELD_NAME' is foreign key from table 'CI_LOOKUP_FIELD'.
'CI_ID_TYPE' is a Primary Table.

Field Descriptions for table 'CI_ID_TYPE':

  1. 'ID_TYPE_CD' (CHAR):- field name for ID Type
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999
  3. 'ID_FMT_ALG_CD' (CHAR):- field name for Identifier Format
  4. 'VAL_ID_TYPE_FOR_DUPS_FLG' (CHAR):- field name for Validate for Duplicates
  5. 'BUS_OBJ_CD' (CHAR):- field name for Business Object
  6. 'ID_PREFIX_FLG' (CHAR):- field name for Identifier Prefix, 'nullable': True
  7. 'FIELD_NAME' (CHAR):- field name for Field Name, 'nullable': True
  8. 'DELIMITER' (CHAR):- field name for Delimiter, 'nullable': True
  9. 'ALLOW_PRIMARY_FLG' (CHAR):- field name for Allow as Primary
  10. 'BO_DATA_AREA' (CLOB):- field name for Business Object Data Area, 'nullable': True

The child tables of 'CI_ID_TYPE' are ['CI_ID_TYPE_L']. 
(Generated when 'MAINT_OBJ_CD'=ID TYPE)

--------------------------------------------------------------------------

Table 'CI_ID_TYPE_L' is used for storing Identifier Type Language. Table 'CI_ID_TYPE_L' has 4 fields (columns) which are:  1. 'ID_TYPE_CD' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'ID_TYPE_CD'  2. 'LANGUAGE_CD' . 
Table 'CI_ID_TYPE_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'ID_TYPE_CD' is foreign key from table 'CI_ID_TYPE'.
'CI_ID_TYPE_L' is a child table of 'CI_ID_TYPE' table.

Field Descriptions for table 'CI_ID_TYPE_L':

  1. 'ID_TYPE_CD' (CHAR):- field name for ID Type
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999

---------------------------------------------------------------------------
""",
    "ACCOUNT_RELATION_TYPE": """

These tables store relationship of accounts.

Table 'CI_ACCT_REL_TYP' is used for storing Account Relationship Type. Table 'CI_ACCT_REL_TYP' has 2 fields (columns) which are:  1. 'ACCT_REL_TYPE_CD' 2. 'VERSION'. Out of these fields, only one is a primary key; 'ACCT_REL_TYPE_CD' is the primary key for 'CI_ACCT_REL_TYP'
'CI_ACCT_REL_TYP' is a Primary Table.

Field Descriptions for table 'CI_ACCT_REL_TYP':

  1. 'ACCT_REL_TYPE_CD' (CHAR):- field name for Account Relationship Type
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999

The child tables of 'CI_ACCT_REL_TYP' are ['CI_ACCT_REL_TYP_L']. 
(Generated when 'MAINT_OBJ_CD'=ACCT REL TYP)

--------------------------------------------------------------------------

Table 'CI_ACCT_REL_TYP_L' is used for storing Account Relationship Type Language. Table 'CI_ACCT_REL_TYP_L' has 4 fields (columns) which are:  1. 'ACCT_REL_TYPE_CD' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'LANGUAGE_CD'  2. 'ACCT_REL_TYPE_CD' . 
Table 'CI_ACCT_REL_TYP_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'ACCT_REL_TYPE_CD' is foreign key from table 'CI_ACCT_REL_TYP'.
'CI_ACCT_REL_TYP_L' is a child table of 'CI_ACCT_REL_TYP' table.

Field Descriptions for table 'CI_ACCT_REL_TYP_L':

  1. 'ACCT_REL_TYPE_CD' (CHAR):- field name for Account Relationship Type
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999

---------------------------------------------------------------------------
""",
    "TIME_ZONE": """
Table 'CI_TIME_ZONE' is used for storing Time Zone. Table 'CI_TIME_ZONE' has 5 fields (columns) which are:  1. 'TIME_ZONE_CD' 2. 'VERSION' 3. 'SEASON_TM_SHIFT_CD' 4. 'MINUTE_FR_BASE_TZ' 5. 'F1_TIMEZONE_NAME'. Out of these fields, only one is a primary key; 'TIME_ZONE_CD' is the primary key for 'CI_TIME_ZONE'. 
Table 'CI_TIME_ZONE' has only one foreign key; 'SEASON_TM_SHIFT_CD' is a foreign key from table 'CI_SEAS_TM_SHIFT'.
'CI_TIME_ZONE' is a Primary Table.

Field Descriptions for table 'CI_TIME_ZONE':

  1. 'TIME_ZONE_CD' (CHAR):- field name for Time Zone
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999
  3. 'SEASON_TM_SHIFT_CD' (CHAR):- field name for Seasonal Time Shift
  4. 'MINUTE_FR_BASE_TZ' (NUMBER):- field name for Shift In Minutes,  'precision': 7
  5. 'F1_TIMEZONE_NAME' (VARCHAR2):- field name for Time Zone Name in format ({Country_name}/{Time_zone_name})

The child tables of 'CI_TIME_ZONE' are ['CI_TIME_ZONE_L']. 
(Generated when 'MAINT_OBJ_CD'=TIME ZONE)

--------------------------------------------------------------------------

Table 'CI_TIME_ZONE_L' is used for storing Time Zone Language. Table 'CI_TIME_ZONE_L' has 6 fields (columns) which are:  1. 'TIME_ZONE_CD' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'VERSION' 5. 'DFLT_TIME_ZONE_LABEL' 6. 'SHIFT_TIME_ZONE_LABEL'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'TIME_ZONE_CD'  2. 'LANGUAGE_CD' . 
Table 'CI_TIME_ZONE_L' has 2 foreign keys as listed:  'TIME_ZONE_CD' is foreign key from table 'CI_TIME_ZONE', and 'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE'.
'CI_TIME_ZONE_L' is a child table of 'CI_TIME_ZONE' table.

Field Descriptions for table 'CI_TIME_ZONE_L':

  1. 'TIME_ZONE_CD' (CHAR):- field name for Time Zone
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description
  4. 'VERSION' (NUMBER):- field name for Version, 'precision': 5, 'default': 99999
  5. 'DFLT_TIME_ZONE_LABEL' (VARCHAR2):- field name for Time Zone code
  6. 'SHIFT_TIME_ZONE_LABEL' (VARCHAR2):- field name for Shifted Time Zone Label

Only provide labels for English 'ENG' when not specified.

---------------------------------------------------------------------------
""",
    "LANGUAGE": """
Table 'CI_LANGUAGE' is used for storing Language Code. Table 'CI_LANGUAGE' has 8 fields (columns) which are:  1. 'LANGUAGE_CD' 2. 'DESCR' 3. 'VERSION' 4. 'SUPPORT_SW' 5. 'LOCALE' 6. 'COLLATOR_STRENGTH' 7. 'OWNER_FLG' 8. 'DISP_ORD_FLG'. Out of these fields, only one is a primary key; 'LANGUAGE_CD' is the primary key for 'CI_LANGUAGE'
'CI_LANGUAGE' is a Primary Table.

Field Descriptions for table 'CI_LANGUAGE':

  1. 'LANGUAGE_CD' (CHAR):- field name for Language
  2. 'DESCR' (VARCHAR2):- field name for Description
  3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999
  4. 'SUPPORT_SW' (CHAR):- field name for Language Enable, 'values': 'Y', 'N'
  5. 'LOCALE' (VARCHAR2):- field name for Locale
  6. 'COLLATOR_STRENGTH' (VARCHAR2):- field name for Collator Strength, 'values': 'PRIMARY', 'SECONDARY', 'TERTIARY', 'IDENTICAL'
  7. 'OWNER_FLG' (CHAR):- field name for Owner, 'default': 'F1'
  8. 'DISP_ORD_FLG' (CHAR):- field name for Display Order, 'values': 'LTR' (LeftToRight), 'RTL' (RightToLeft)

(Generated when 'MAINT_OBJ_CD'=LANGUAGE)

---------------------------------------------------------------------------
""",
    "UNIT_OF_MEASUREMENT": """
Table 'CI_UOM' is used for storing Unit Of Measure - CCB. Table 'CI_UOM' has 6 fields (columns) which are:  1. 'UOM_CD' 2. 'SVC_TYPE_CD' 3. 'ALLOWED_ON_REG_SW' 4. 'MSR_PEAK_QTY_SW' 5. 'DECIMAL_POSITIONS' 6. 'VERSION'. Out of these fields, only one is a primary key; 'UOM_CD' is the primary key for 'CI_UOM'. 
Table 'CI_UOM' has only one foreign key; 'SVC_TYPE_CD' is a foreign key from table 'CI_SVC_TYPE'.
'CI_UOM' is a Primary Table.

Field Descriptions for table 'CI_UOM':

  1. 'UOM_CD' (VARCHAR2):- field name for Unit of Measure
  2. 'SVC_TYPE_CD' (VARCHAR2):- field name for Service Type, 'values': 'O', 'E'
  3. 'ALLOWED_ON_REG_SW' (CHAR):- field name for Allowed on Register, 'values': 'Y', 'N'
  4. 'MSR_PEAK_QTY_SW' (CHAR):- field name for Measures Peak Qty, 'values': 'Y', 'N'
  5. 'DECIMAL_POSITIONS' (NUMBER):- field name for Decimal Positions,  'precision': 1
  6. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999

The child tables of 'CI_UOM' are ['CI_UOM_L']. 
(Generated when 'MAINT_OBJ_CD'=UOM)

--------------------------------------------------------------------------

Table 'CI_UOM_L' is used for storing Unit of Measure (UOM) Language - CCB. Table 'CI_UOM_L' has 4 fields (columns) which are:  1. 'UOM_CD' 2. 'LANGUAGE_CD' 3. 'VERSION' 4. 'DESCR'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'UOM_CD'  2. 'LANGUAGE_CD' . 
Table 'CI_UOM_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'UOM_CD' is foreign key from table 'CI_UOM'.
'CI_UOM_L' is a child table of 'CI_UOM' table.

Field Descriptions for table 'CI_UOM_L':

  1. 'UOM_CD' (VARCHAR2):- field name for Unit of Measure
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999
  4. 'DESCR' (VARCHAR2):- field name for Description

---------------------------------------------------------------------------
""",
    "SERVICE_QUANTITY_IDENTIFIER": """
Table 'CI_SQI' is used for storing Service Quantity Identifier (SQI)- CCB. Table 'CI_SQI' has 3 fields (columns) which are:  1. 'SQI_CD' 2. 'VERSION' 3. 'DECIMAL_POSITIONS'. Out of these fields, only one is a primary key; 'SQI_CD' is the primary key for 'CI_SQI'
'CI_SQI' is a Primary Table.

Field Descriptions for table 'CI_SQI':

  1. 'SQI_CD' (VARCHAR2):- field name for SQI
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999
  3. 'DECIMAL_POSITIONS' (NUMBER):- field name for Decimal Positions,  'precision': 1

The child tables of 'CI_SQI' are ['CI_SQI_L']. 
(Generated when 'MAINT_OBJ_CD'=SQI)

--------------------------------------------------------------------------

Table 'CI_SQI_L' is used for storing Service Quantity Identifier (SQI) Language - CCB. Table 'CI_SQI_L' has 4 fields (columns) which are:  1. 'SQI_CD' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'SQI_CD'  2. 'LANGUAGE_CD' . 
Table 'CI_SQI_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'SQI_CD' is foreign key from table 'CI_SQI'.
'CI_SQI_L' is a child table of 'CI_SQI' table.

Field Descriptions for table 'CI_SQI_L':

  1. 'SQI_CD' (VARCHAR2):- field name for SQI
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999

---------------------------------------------------------------------------
""",
    "GEO_TYPE": """

Table 'CI_GEO_TYPE' is used for storing Geographic Type. Table 'CI_GEO_TYPE' has 3 fields (columns) which are:  1. 'GEO_TYPE_CD' 2. 'VERSION' 3. 'GEO_VAL_FMT_ALG_CD'. Out of these fields, only one is a primary key; 'GEO_TYPE_CD' is the primary key for 'CI_GEO_TYPE'. 
Table 'CI_GEO_TYPE' has only one foreign key; 'GEO_VAL_FMT_ALG_CD' is a foreign key from table 'CI_ALG'.
'CI_GEO_TYPE' is a Primary Table.

Field Descriptions for table 'CI_GEO_TYPE':

  1. 'GEO_TYPE_CD' (CHAR):- field name for Geographic Type
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999
  3. 'GEO_VAL_FMT_ALG_CD' (CHAR):- field name for Validation Format Algorithm

The child tables of 'CI_GEO_TYPE' are ['CI_GEO_TYPE_L']. 
(Generated when 'MAINT_OBJ_CD'=GEO TYPE)

--------------------------------------------------------------------------

Table 'CI_GEO_TYPE_L' is used for storing Geographic Type Language. Table 'CI_GEO_TYPE_L' has 4 fields (columns) which are:  1. 'LANGUAGE_CD' 2. 'GEO_TYPE_CD' 3. 'DESCR' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'LANGUAGE_CD'  2. 'GEO_TYPE_CD' . 
Table 'CI_GEO_TYPE_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'GEO_TYPE_CD' is foreign key from table 'CI_GEO_TYPE'.
'CI_GEO_TYPE_L' is a child table of 'CI_GEO_TYPE' table.

Field Descriptions for table 'CI_GEO_TYPE_L':

  1. 'LANGUAGE_CD' (CHAR):- field name for Language
  2. 'GEO_TYPE_CD' (CHAR):- field name for Geographic Type
  3. 'DESCR' (VARCHAR2):- field name for Description
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999

---------------------------------------------------------------------------
""",
    "WORK_CALENDAR": """
Steps to configure a Work Calendar:

Step 1: Fill the below 2 tables 'CI_CAL_WORK' and 'CI_CAL_WORK_L' with 1 row each for each work calendar configuration asked in the query.

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
Step 2: Fill the below 2 tables 'CI_CAL_HOL' and 'CI_CAL_HOL_L' with multiple rows for all the holidays you can think of in a year with respect to the configuration needed.

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

IMP: This is a Work Calendar. Use the above tables when the query is asking to configure a work calendar.
---------------------------------------------------------------------------
""",
    "ACCOUNTING_CALENDAR": """
Following are steps to configure Accounting Calendar:

Step 1: Fill the below GL tables with insert queries that include all the field names provided.
- `CI_CAL_GL`: Its the primary storage for Accounting Calendars. It consists of 3 fields: `CALENDAR_ID` (PK)(CHAR), `NUMBER_OF_PERIODS`, and `VERSION`. The `NUMBER_OF_PERIODS` field, of type NUMBER, represents the number of periods in a year with a precision of 2.
- `CI_CAL_GL_L`: It consists of 4 fields: `CALENDAR_ID`, `DESCR`, `LANGUAGE_CD`, and `VERSION`. The primary key is a composite of `CALENDAR_ID` and `LANGUAGE_CD`. 
- `CI_CAL_PERIOD`: It is made up of 8 fields: `CALENDAR_ID`, `FISCAL_YEAR`, `ACCOUNTING_PERIOD`, `BEGIN_DT`, `END_DT`, `OPEN_FROM_DT`, `OPEN_TO_DT`, and `VERSION`. The composite primary key consists of `FISCAL_YEAR`, `ACCOUNTING_PERIOD`, and `CALENDAR_ID`.
- `CI_CAL_PERIOD_L`: It includes 6 fields: `CALENDAR_ID`, `LANGUAGE_CD`, `FISCAL_YEAR`, `PERIOD_DESCR`, `ACCOUNTING_PERIOD`, and `VERSION`. The primary key for this table is a composite of four fields: `LANGUAGE_CD`, `ACCOUNTING_PERIOD`, `FISCAL_YEAR`, and `CALENDAR_ID`. 

Step 2: Similarly fill the below set of W1 tables.
- `W1_CALENDAR`: Its another primary table used for storing Accounting Calendar data. It comprises 5 fields: `W1_CALENDAR_CD` (PK)(CHAR), `NUM_PERIODS`, `BUS_OBJ_CD`, `BO_DATA_AREA`, and `VERSION`. 
- `W1_CALENDAR_L`: It has 4 fields: `W1_CALENDAR_CD`, `LANGUAGE_CD`, `DESCR100`, and `VERSION`. The primary key is a composite of `W1_CALENDAR_CD` and `LANGUAGE_CD`. 
- `W1_CALENDAR_PERIOD`: It has 8 fields: `W1_CALENDAR_CD`, `W1_FISCAL_YEAR`, `ACCTG_PERIOD`, `W1_START_DT`, `W1_END_DT`, `W1_OPEN_FROM_DT`, `W1_OPEN_TO_DT`, and `VERSION`. The primary key for this table is a composite of `W1_FISCAL_YEAR`, `ACCTG_PERIOD`, and `W1_CALENDAR_CD`.
- `W1_CALENDAR_PERIOD_L`: It contains 6 fields: `W1_CALENDAR_CD`, `W1_FISCAL_YEAR`, `ACCTG_PERIOD`, `LANGUAGE_CD`, `DESCR100`, and `VERSION`. The composite primary key consists of `W1_FISCAL_YEAR`, `ACCTG_PERIOD`, `W1_CALENDAR_CD`, and `LANGUAGE_CD`. 
- `W1_CALENDAR_CHAR`: It stores characteristics of Accounting Calendars. It consists of 12 fields: `W1_CALENDAR_CD`, `CHAR_TYPE_CD`, `SEQ_NUM`, `CHAR_VAL`, `ADHOC_CHAR_VAL`, `CHAR_VAL_FK1`, `CHAR_VAL_FK2`, `CHAR_VAL_FK3`, `CHAR_VAL_FK4`, `CHAR_VAL_FK5`, `SEARCH_CHAR_VAL`, and `VERSION`. The primary key is a composite of `CHAR_TYPE_CD`, `SEQ_NUM`, and `W1_CALENDAR_CD`. 

Only output queries for the above exact 9 tables with the exact field names mentioned. It is illegal to change any table/ field names. It is against the rules to use ellipses('...'), output all rows asked for, don't be lazy.

IMP Note: The above 2 steps are seperated because they are different tables (GL and W1) and their field names are not related. Use the tables only when asked for configuring accounting calendar.

""",
    "LOOKUP_FIELD": """

Fill up the below tables when asked to create lookup fields:

Table 'CI_LOOKUP_FIELD' is used for storing Lookup Field. Table 'CI_LOOKUP_FIELD' has 5 fields (columns) which are:  1. 'FIELD_NAME' 2. 'VERSION' 3. 'CUSTOM_SW' 4. 'OWNER_FLG' 5. 'OBJ_PROPERTY_NAME'. Out of these fields, only one is a primary key; 'FIELD_NAME' is the primary key for 'CI_LOOKUP_FIELD'
'CI_LOOKUP_FIELD' is a Primary Table.

Field Descriptions for table 'CI_LOOKUP_FIELD':

  1. 'FIELD_NAME' (CHAR):- field name for Field Name, usually used for storing field name of flags
  2. 'VERSION' (NUMBER):- field name for Version, 'precision': 5, 'default': 99999
  3. 'CUSTOM_SW' (CHAR):- field name for Custom (Yes 'Y' or No 'N')
  4. 'OWNER_FLG' (CHAR):- field name for Owner
  5. 'OBJ_PROPERTY_NAME' (VARCHAR2):- field name for Java Field Name

The child tables of 'CI_LOOKUP_FIELD' are ['CI_LOOKUP_VAL_L', 'CI_LOOKUP_VAL']. 
When one FIELD_NAME is added to the lookup field table, multiple rows of field values will be added to CI_LOOKUP_VAL and CI_LOOKUP_VAL_L for different types of the FIELD_NAME.

--------------------------------------------------------------------------
The below tables stores the field values of the lookup field. It could be interpreted as different types of values that a lookup field can have.

Table 'CI_LOOKUP_VAL_L' is used for storing Lookup Field Value Language. Table 'CI_LOOKUP_VAL_L' has 8 fields (columns) which are:  1. 'FIELD_NAME' 2. 'FIELD_VALUE' 3. 'LANGUAGE_CD' 4. 'VERSION' 5. 'DESCR' 6. 'OWNER_FLG' 7. 'DESCR_OVRD' 8. 'DESCRLONG'. Out of these fields, 6 are primary keys. The composite primary keys are:  1. 'FIELD_NAME'  2. 'FIELD_VALUE'  3. 'LANGUAGE_CD'  4. 'FIELD_VALUE'  5. 'FIELD_NAME'  6. 'LANGUAGE_CD' . 
Table 'CI_LOOKUP_VAL_L' has 2 foreign keys as listed:  'FIELD_VALUE' is foreign key from table 'CI_LOOKUP_VAL', and 'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE'.
'CI_LOOKUP_VAL_L' is a child table of 'CI_LOOKUP_FIELD' table.

Field Descriptions for table 'CI_LOOKUP_VAL_L':

  1. 'FIELD_NAME' (CHAR):- field name for Field Name
  2. 'FIELD_VALUE' (CHAR):- field name for Field Value
  3. 'LANGUAGE_CD' (CHAR):- field name for Language
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999
  5. 'DESCR' (VARCHAR2):- field name for Description
  6. 'OWNER_FLG' (CHAR):- field name for Owner
  7. 'DESCR_OVRD' (VARCHAR2):- field name for Override Description, 'default': ' '
  8. 'DESCRLONG' (VARCHAR2):- field name for Detailed Description

--------------------------------------------------------------------------

Table 'CI_LOOKUP_VAL' is used for storing Lookup Field Value for storing the different values ('FIELD_VALUE's) of the 'FIELD_NAME'. Table 'CI_LOOKUP_VAL' has 6 fields (columns) which are:  1. 'FIELD_NAME' 2. 'FIELD_VALUE' 3. 'EFF_STATUS' 4. 'VERSION' 5. 'OWNER_FLG' 6. 'VALUE_NAME'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'FIELD_NAME'  2. 'FIELD_VALUE' . 
Table 'CI_LOOKUP_VAL' has only one foreign key; 'FIELD_NAME' is a foreign key from table 'CI_LOOKUP_FIELD'.
'CI_LOOKUP_VAL' is a child table of 'CI_LOOKUP_FIELD' table.

Field Descriptions for table 'CI_LOOKUP_VAL':

  1. 'FIELD_NAME' (CHAR):- field name for Field Name
  2. 'FIELD_VALUE' (CHAR):- field name for Field Value
  3. 'EFF_STATUS' (CHAR):- field name for Status, 'default': 'A'
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999
  5. 'OWNER_FLG' (CHAR):- field name for Owner
  6. 'VALUE_NAME' (VARCHAR2):- field name for Java Value Name

Fill all the tables for configuring a lookup field. only use this when asked for lookup field.
---------------------------------------------------------------------------
""",
    "CIS_DIVISION": """

Tables and Field Reference for CIS Division Configuration:

  1. 'CI_CIS_DIVISION' (Primary Table):
      -Fields: CIS_DIVISION, CALENDAR_CD, VERSION, BUS_OBJ_CD, CUST_CL_CD_BUS, CUST_CL_CD_PER, START_CASH_ONL_PTS, START_CR_RAT_PTS, CASH_ONLY_PTS_THRS, CR_RAT_THRS, OVRD_CRRT_CASH_SW, CIS_DIV_DATA_AREA, CIS_DIV_RESTRICT_FLG.
      -Primary Key: CIS_DIVISION
      -Foreign Keys: CALENDAR_CD, BUS_OBJ_CD, CUST_CL_CD_BUS, CUST_CL_CD_PER

  2. 'CI_CIS_DIVISION_L':
      -Fields: CIS_DIVISION, LANGUAGE_CD, VERSION, DESCR
      -Composite Primary Key: CIS_DIVISION, LANGUAGE_CD
      -Foreign Key: LANGUAGE_CD

  3. 'C1_CIS_DIV_RTYP':
      -Fill all 14 Fields: CIS_DIVISION, BILL_RTE_TYPE_CD, QTE_RTE_TYPE_CD, OVRD_BATCH_CD, RT_TYPE_ALG_ENT_FLG, OVRD_EXTRACT_ALG_CD, VERSION, OVRD_CO_ID, ENCR_OVRD_CO_ID, OVRD_CO_NAME, OVRD_CO_ENTITY_DESCR, OVRD_TNDR_SOURCE_CD, APAY_RTE_TYPE_CD, OVRD_WEB_DEBIT_ACCT_VAL_ALG_CD
      -Composite Primary Key: CIS_DIVISION, BILL_RTE_TYPE_CD, QTE_RTE_TYPE_CD, APAY_RTE_TYPE_CD

  4. 'CI_DIV_TD_ROLE':
      -Fields: TD_TYPE_CD, CIS_DIVISION, ROLE_ID, VERSION
      -Composite Primary Key: CIS_DIVISION, TD_TYPE_CD

  5. 'CI_CIS_DIV_CHAR':
      -Fields: CIS_DIVISION, CHAR_TYPE_CD, EFFDT, CHAR_VAL, VERSION, ADHOC_CHAR_VAL, CHAR_VAL_FK1, CHAR_VAL_FK2, CHAR_VAL_FK3, CHAR_VAL_FK4, CHAR_VAL_FK5
      -Composite Primary Key: CIS_DIVISION, CHAR_TYPE_CD, EFFDT

  6. 'C1_CIS_DIV_SEQ_CHAR':
      Fields: CIS_DIVISION, CHAR_TYPE_CD, SEQ_NUM, CHAR_VAL, ADHOC_CHAR_VAL, CHAR_VAL_FK1, CHAR_VAL_FK2, CHAR_VAL_FK3, CHAR_VAL_FK4, CHAR_VAL_FK5, VERSION, SRCH_CHAR_VAL
      Composite Primary Key: CIS_DIVISION, CHAR_TYPE_CD, SEQ_NUM

Instructions:
  -Insert CIS Division in 'CI_CIS_DIVISION'.
  -Insert language details in 'CI_CIS_DIVISION_L'.
  -Insert route types in 'C1_CIS_DIV_RTYP'.
  -Insert roles in 'CI_DIV_TD_ROLE'.
  -Insert effective-dated characteristics in 'CI_CIS_DIV_CHAR'.
  -Insert sequential characteristics in 'C1_CIS_DIV_SEQ_CHAR'.

The above tables will be used specifically for configuration of CIS Division. A CIS (Customer Information System) division is associated with a jurisdiction. The definition of a jurisdiction is a geographic-oriented entity with unique business rules.

---------------------------------------------------------------------------
""",
    "GENERAL_LEDGER_DIVISION": """

Table 'CI_GL_DIVISION' is used for storing General Ledger (GL) Division. Table 'CI_GL_DIVISION' has 4 fields (columns) which are:  1. 'CURRENCY_CD' 2. 'GL_DIVISION' 3. 'CALENDAR_ID' 4. 'VERSION'. Out of these fields, only one is a primary key; 'GL_DIVISION' is the primary key for 'CI_GL_DIVISION'. 
Table 'CI_GL_DIVISION' has 2 foreign keys as listed:  'CALENDAR_ID' is foreign key from table 'CI_CAL_GL', and 'CURRENCY_CD' is foreign key from table 'CI_CURRENCY_CD'.
'CI_GL_DIVISION' is a Primary Table.

Field Descriptions for table 'CI_GL_DIVISION':

  1. 'GL_DIVISION' (CHAR):- field name for GL Division
  2. 'CURRENCY_CD' (CHAR):- field name for Currency Code used for the ledger
  3. 'CALENDAR_ID' (CHAR):- field name for Calendar ID
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999

The child tables of 'CI_GL_DIVISION' are ['CI_GL_DIVISION_L']. 
(Generated when 'MAINT_OBJ_CD'=GL DIVISION)

--------------------------------------------------------------------------

Table 'CI_GL_DIVISION_L' is used for storing GL Division Language. Table 'CI_GL_DIVISION_L' has 4 fields (columns) which are:  1. 'GL_DIVISION' 2. 'LANGUAGE_CD' 3. 'VERSION' 4. 'DESCR'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'GL_DIVISION'  2. 'LANGUAGE_CD' . 
Table 'CI_GL_DIVISION_L' has 2 foreign keys as listed:  'GL_DIVISION' is foreign key from table 'CI_GL_DIVISION', and 'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE'.
'CI_GL_DIVISION_L' is a child table of 'CI_GL_DIVISION' table.

Field Descriptions for table 'CI_GL_DIVISION_L':

  1. 'GL_DIVISION' (CHAR):- field name for GL Division
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5, 'default': 99999
  4. 'DESCR' (VARCHAR2):- field name for Description

---------------------------------------------------------------------------
""",
    "DEBT_CLASS": """

Table 'CI_DEBT_CL' is used for storing Debt Class. Table 'CI_DEBT_CL' has 3 fields (columns) which are:  1. 'DEBT_CL_CD' 2. 'ELIG_FOR_COLL_SW' 3. 'VERSION'. Out of these fields, only one is a primary key; 'DEBT_CL_CD' is the primary key for 'CI_DEBT_CL'
'CI_DEBT_CL' is a Primary Table.

Field Descriptions for table 'CI_DEBT_CL':

  1. 'DEBT_CL_CD' (CHAR):- field name for Debt Class
  2. 'ELIG_FOR_COLL_SW' (CHAR):- field name for Eligible for Collection (Yes 'Y' or No 'N')
  3. 'VERSION' (NUMBER):- field name for Version, 'precision': 5, 'default': 99999

The child tables of 'CI_DEBT_CL' are ['CI_DC_ALG', 'CI_DEBT_CL_L']. 
(Generated when 'MAINT_OBJ_CD'=DEBT CLASS)

--------------------------------------------------------------------------

Table 'CI_DEBT_CL_L' is used for storing Debt Class Language. Table 'CI_DEBT_CL_L' has 4 fields (columns) which are:  1. 'DESCR' 2. 'LANGUAGE_CD' 3. 'DEBT_CL_CD' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'DEBT_CL_CD'  2. 'LANGUAGE_CD' . 
Table 'CI_DEBT_CL_L' has 2 foreign keys as listed:  'DEBT_CL_CD' is foreign key from table 'CI_DEBT_CL', and 'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE'.
'CI_DEBT_CL_L' is a child table of 'CI_DEBT_CL' table.

Field Descriptions for table 'CI_DEBT_CL_L':

  1. 'DESCR' (VARCHAR2):- field name for Description
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DEBT_CL_CD' (CHAR):- field name for Debt Class
  4. 'VERSION' (NUMBER):- field name for Version, 'precision': 5, 'default':  99999

--------------------------------------------------------------------------

Table 'CI_DC_ALG' is used for storing Debt Class Algorithm. Table 'CI_DC_ALG' has 5 fields (columns) which are:  1. 'DEBT_CL_CD' 2. 'DC_ALG_ENTITY_FLG' 3. 'SEQ_NUM' 4. 'ALG_CD' 5. 'VERSION'. Out of these fields, 3 are primary keys. The composite primary keys are:  1. 'SEQ_NUM'  2. 'DC_ALG_ENTITY_FLG'  3. 'DEBT_CL_CD' . 
Table 'CI_DC_ALG' has 2 foreign keys as listed:  'DEBT_CL_CD' is foreign key from table 'CI_DEBT_CL', and 'ALG_CD' is foreign key from table 'CI_ALG'.
'CI_DC_ALG' is a child table of 'CI_DEBT_CL' table.

Field Descriptions for table 'CI_DC_ALG':

  1. 'DEBT_CL_CD' (CHAR):- field name for Debt Class
  2. 'DC_ALG_ENTITY_FLG' (CHAR):- field name for Debt Class Algorithm Entity, a short acronym for algorithm name
  3. 'SEQ_NUM' (NUMBER):- field name for Sequence, 'precision': 3
  4. 'ALG_CD' (CHAR):- field name for Algorithm
  5. 'VERSION' (NUMBER):- field name for Version, 'precision': 5, 'default': 99999

Configuration:
-Provide insert queries for tables 'CI_DEBT_CL' and 'CI_DEBT_CL_L'.
-If any row has 'ELIG_FOR_COLL_SW' field set to 'Y', i.e. it is elligible for collection; then and only then fill table 'CI_DC_ALG' for that 'DEBT_CL_CD'. If not, then skip filling for 'CI_DC_ALG'.

---------------------------------------------------------------------------
""",
    "BILL_FACTOR": """

Table 'CI_BF' is used for storing Bill Factor. Table 'CI_BF' has 15 fields (columns) which are:  1. 'BF_CD' 2. 'CHAR_TYPE_CD' 3. 'VAL_TYPE_FLG' 4. 'ALLOW_PRO_SW' 5. 'ERR_IF_NO_VAL_SW' 6. 'VAL_IN_CONT_SW' 7. 'APPL_IN_CONT_SW' 8. 'EXEMPT_IN_CONT_SW' 9. 'CURRENCY_CD' 10. 'CHAR_SRC_FLG' 11. 'VERSION' 12. 'USE_SUB_SA_CT_SW' 13. 'BF_TYPE_FLG' 14. 'TOS_USAGE_FLG' 15. 'RATE_SEL_DT_ALG_CD'. Out of these fields, only one is a primary key; 'BF_CD' is the primary key for 'CI_BF'. 
Table 'CI_BF' has 3 foreign keys as listed:  'RATE_SEL_DT_ALG_CD' is foreign key from table 'CI_ALG', 'CURRENCY_CD' is foreign key from table 'CI_CURRENCY_CD', and 'CHAR_TYPE_CD' is foreign key from table 'CI_CHAR_TYPE'.
'CI_BF' is a Primary Table.

Field Descriptions for table 'CI_BF':

  1. 'BF_CD' (CHAR):- field name for Bill Factor
  2. 'CHAR_TYPE_CD' (CHAR):- field name for Characteristic Type
  3. 'VAL_TYPE_FLG' (CHAR):- field name for Value Type, 'values': 'C', 'P', 'U'
  4. 'ALLOW_PRO_SW' (CHAR):- field name for Allow RV Proration (Yes 'Y' or No 'N')
  5. 'ERR_IF_NO_VAL_SW' (CHAR):- field name for Error If No Value (Yes 'Y' or No 'N')
  6. 'VAL_IN_CONT_SW' (CHAR):- field name for Value In Contract Term (Yes 'Y' or No 'N')
  7. 'APPL_IN_CONT_SW' (CHAR):- field name for Contract Rider Applicability (Yes 'Y' or No 'N')
  8. 'EXEMPT_IN_CONT_SW' (CHAR):- field name for Tax Exemption In Contract Term (Yes 'Y' or No 'N')
  9. 'CURRENCY_CD' (CHAR):- field name for Currency Code
  10. 'CHAR_SRC_FLG' (CHAR):- field name for Characteristic Source, 'values': 'NA', 'PR', 'SA', 'SP'
  11. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  12. 'USE_SUB_SA_CT_SW' (CHAR):- field name for Use Sub SA Contract
  13. 'BF_TYPE_FLG' (CHAR):- field name for Bill Factor Type, 'values': 'I', 'R'
  14. 'TOS_USAGE_FLG' (CHAR):- field name for Terms of Service Usage
  15. 'RATE_SEL_DT_ALG_CD' (CHAR):- field name for Rate Selection Date Algorithm

The child tables of 'CI_BF' are ['CI_BF_L', 'CI_BF_CHAR']. 
(Generated when 'MAINT_OBJ_CD'=BILL FACTOR)

--------------------------------------------------------------------------

Table 'CI_BF_L' is used for storing Bill Factor Language. Table 'CI_BF_L' has 4 fields (columns) which are:  1. 'BF_CD' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'BF_CD'  2. 'LANGUAGE_CD' . 
Table 'CI_BF_L' has 2 foreign keys as listed:  'BF_CD' is foreign key from table 'CI_BF', and 'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE'.
'CI_BF_L' is a child table of 'CI_BF' table.

Field Descriptions for table 'CI_BF_L':

  1. 'BF_CD' (CHAR):- field name for Bill Factor
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

--------------------------------------------------------------------------

Table 'CI_BF_CHAR' is used for storing Bill Factor Characteristic. Table 'CI_BF_CHAR' has 7 fields (columns) which are:  1. 'CHAR_TYPE_CD' 2. 'BF_CD' 3. 'CHAR_VAL' 4. 'VERSION' 5. 'INTV_PF_EXT_ID' 6. 'INTV_MINUTE' 7. 'SEASON_TM_SHIFT_CD'. Out of these fields, 3 are primary keys. The composite primary keys are:  1. 'CHAR_VAL'  2. 'BF_CD'  3. 'CHAR_TYPE_CD' . 
Table 'CI_BF_CHAR' has 3 foreign keys as listed:  'BF_CD' is foreign key from table 'CI_BF', 'CHAR_TYPE_CD' is foreign key from table 'CI_CHAR_VAL', and 'SEASON_TM_SHIFT_CD' is foreign key from table 'CI_SEAS_TM_SHIFT'.
'CI_BF_CHAR' is a child table of 'CI_BF' table.

Field Descriptions for table 'CI_BF_CHAR':

  1. 'CHAR_TYPE_CD' (CHAR):- field name for Characteristic Type
  2. 'BF_CD' (CHAR):- field name for Bill Factor
  3. 'CHAR_VAL' (CHAR):- field name for Characteristic Value
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  5. 'INTV_PF_EXT_ID' (VARCHAR2):- field name for External ID
  6. 'INTV_MINUTE' (NUMBER):- field name for Minutes Per Interval,  'precision': 6
  7. 'SEASON_TM_SHIFT_CD' (CHAR):- field name for Seasonal Time Shift
---------------------------------------------------------------------------
""",
    "TO_DO_ROLE": """

Note: Could be asked to create a role with multiple types... the same ROLE_ID will have more than one types which will be having different TD_TYPE_CD.

Table 'CI_ROLE' is used for storing Role. Table 'CI_ROLE' has 2 fields (columns) which are:  1. 'ROLE_ID' 2. 'VERSION'. Out of these fields, only one is a primary key; 'ROLE_ID' is the primary key for 'CI_ROLE'
'CI_ROLE' is a Primary Table.

Field Descriptions for table 'CI_ROLE':

  1. 'ROLE_ID' (CHAR):- field name for To Do Role
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

The child tables of 'CI_ROLE' are ['CI_TD_VAL_ROLE', 'CI_ROLE_USER', 'CI_ROLE_L']. 
(Generated when 'MAINT_OBJ_CD'=TO DO ROLE)

--------------------------------------------------------------------------

Table 'CI_TD_VAL_ROLE' is used for storing To Do Type Role. Table 'CI_TD_VAL_ROLE' has 4 fields (columns) which are:  1. 'VERSION' 2. 'DEFAULT_SW' 3. 'TD_TYPE_CD' 4. 'ROLE_ID'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'ROLE_ID'  2. 'TD_TYPE_CD' . 
Table 'CI_TD_VAL_ROLE' has 2 foreign keys as listed:  'TD_TYPE_CD' is foreign key from table 'CI_TD_TYPE', and 'ROLE_ID' is foreign key from table 'CI_ROLE'.
'CI_TD_VAL_ROLE' is a child table of 'CI_ROLE' table.

Field Descriptions for table 'CI_TD_VAL_ROLE':

  1. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  2. 'DEFAULT_SW' (CHAR):- field name for Default
  3. 'TD_TYPE_CD' (CHAR):- field name for To Do Type
  4. 'ROLE_ID' (CHAR):- field name for To Do Role

--------------------------------------------------------------------------

Table 'CI_ROLE_USER' is used for storing Role User. Table 'CI_ROLE_USER' has 3 fields (columns) which are:  1. 'ROLE_ID' 2. 'USER_ID' 3. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'ROLE_ID'  2. 'USER_ID' . 
Table 'CI_ROLE_USER' has 2 foreign keys as listed:  'USER_ID' is foreign key from table 'SC_USER', and 'ROLE_ID' is foreign key from table 'CI_ROLE'.
'CI_ROLE_USER' is a child table of 'CI_ROLE' table.

Field Descriptions for table 'CI_ROLE_USER':

  1. 'ROLE_ID' (CHAR):- field name for To Do Role
  2. 'USER_ID' (CHAR):- field name for User
  3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

--------------------------------------------------------------------------

Table 'CI_ROLE_L' is used for storing Role Language. Table 'CI_ROLE_L' has 4 fields (columns) which are:  1. 'ROLE_ID' 2. 'LANGUAGE_CD' 3. 'VERSION' 4. 'DESCR'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'LANGUAGE_CD'  2. 'ROLE_ID' . 
Table 'CI_ROLE_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'ROLE_ID' is foreign key from table 'CI_ROLE'.
'CI_ROLE_L' is a child table of 'CI_ROLE' table.

Field Descriptions for table 'CI_ROLE_L':

  1. 'ROLE_ID' (CHAR):- field name for To Do Role
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  4. 'DESCR' (VARCHAR2):- field name for Description
---------------------------------------------------------------------------

""",
#     "TO_DO_TYPE": """

# Table 'CI_TD_TYPE' is used for storing To Do Type. Table 'CI_TD_TYPE' has 10 fields (columns) which are:  1. 'TD_TYPE_CD' 2. 'CRE_BATCH_CD' 3. 'MESSAGE_CAT_NBR' 4. 'MESSAGE_NBR' 5. 'RTE_BATCH_CD' 6. 'VERSION' 7. 'OWNER_FLG' 8. 'TD_USAGE_TYPE_FLG' 9. 'TD_PRIORITY_FLG' 10. 'NAV_OPT_CD'. Out of these fields, only one is a primary key; 'TD_TYPE_CD' is the primary key for 'CI_TD_TYPE'. 
# Table 'CI_TD_TYPE' has 5 foreign keys as listed:  'NAV_OPT_CD' is foreign key from table 'CI_NAV_OPT', 'NAV_OPT_CD' is foreign key from table 'CI_NAV_OPT', 'CRE_BATCH_CD' is foreign key from table 'CI_BATCH_CTRL', 'MESSAGE_NBR' is foreign key from table 'CI_MSG', and 'RTE_BATCH_CD' is foreign key from table 'CI_BATCH_CTRL'.
# 'CI_TD_TYPE' is a Primary Table.

# Field Descriptions for table 'CI_TD_TYPE':

#   1. 'TD_TYPE_CD' (CHAR):- field name for To Do Type
#   2. 'CRE_BATCH_CD' (CHAR):- field name for Creation Process
#   3. 'MESSAGE_CAT_NBR' (NUMBER):- field name for Message Category,  'precision': 5
#   4. 'MESSAGE_NBR' (NUMBER):- field name for Message Number,  'precision': 5
#   5. 'RTE_BATCH_CD' (CHAR):- field name for Routing Process
#   6. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
#   7. 'OWNER_FLG' (CHAR):- field name for Owner
#   8. 'TD_USAGE_TYPE_FLG' (CHAR):- field name for To Do Type Usage
#   9. 'TD_PRIORITY_FLG' (CHAR):- field name for Priority
#   10. 'NAV_OPT_CD' (CHAR):- field name for Navigation Option

# The child tables of 'CI_TD_TYPE' are ['CI_TD_TYPE_CHAR', 'CI_CHTY_TDTY', 'CI_TD_TYPE_L', 'CI_TD_DRLKEY_TY', 'CI_TD_SRTKEY_TY', 'CI_TD_TYPE_ALG', 'CI_TD_VAL_ROLE', 'CI_TD_EX_LIST', 'CI_TD_SRTKEY_TY_L']. 
# (Generated when 'MAINT_OBJ_CD'=TO DO TYPE)

# --------------------------------------------------------------------------

# Table 'CI_TD_TYPE_CHAR' is used for storing To Do Type Characteristic. Table 'CI_TD_TYPE_CHAR' has 12 fields (columns) which are:  1. 'TD_TYPE_CD' 2. 'CHAR_TYPE_CD' 3. 'SEQ_NUM' 4. 'CHAR_VAL' 5. 'ADHOC_CHAR_VAL' 6. 'CHAR_VAL_FK1' 7. 'CHAR_VAL_FK2' 8. 'CHAR_VAL_FK3' 9. 'CHAR_VAL_FK4' 10. 'CHAR_VAL_FK5' 11. 'SRCH_CHAR_VAL' 12. 'VERSION'. Out of these fields, 3 are primary keys. The composite primary keys are:  1. 'TD_TYPE_CD'  2. 'SEQ_NUM'  3. 'CHAR_TYPE_CD' . 
# Table 'CI_TD_TYPE_CHAR' has 3 foreign keys as listed:  'CHAR_VAL' is foreign key from table 'CI_CHAR_VAL', 'TD_TYPE_CD' is foreign key from table 'CI_TD_TYPE', and 'CHAR_TYPE_CD' is foreign key from table 'CI_CHAR_TYPE'.
# 'CI_TD_TYPE_CHAR' is a child table of 'CI_TD_TYPE' table.

# Field Descriptions for table 'CI_TD_TYPE_CHAR':

#   1. 'TD_TYPE_CD' (CHAR):- field name for To Do Type
#   2. 'CHAR_TYPE_CD' (CHAR):- field name for Characteristic Type
#   3. 'SEQ_NUM' (NUMBER):- field name for Sequence,  'precision': 3
#   4. 'CHAR_VAL' (CHAR):- field name for Characteristic Value
#   5. 'ADHOC_CHAR_VAL' (VARCHAR2):- field name for Adhoc Characteristic Value
#   6. 'CHAR_VAL_FK1' (VARCHAR2):- field name for Characteristic Value FK 1
#   7. 'CHAR_VAL_FK2' (VARCHAR2):- field name for Characteristic Value FK 2
#   8. 'CHAR_VAL_FK3' (VARCHAR2):- field name for Characteristic Value FK 3
#   9. 'CHAR_VAL_FK4' (VARCHAR2):- field name for Characteristic Value FK 4
#   10. 'CHAR_VAL_FK5' (VARCHAR2):- field name for Characteristic Value FK 5
#   11. 'SRCH_CHAR_VAL' (VARCHAR2):- field name for Search Characteristic Value
#   12. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

# --------------------------------------------------------------------------

# Table 'CI_CHTY_TDTY' is used for storing To Do Type Template Characteristics. Table 'CI_CHTY_TDTY' has 13 fields (columns) which are:  1. 'TD_TYPE_CD' 2. 'CHAR_TYPE_CD' 3. 'CHAR_VAL' 4. 'REQUIRED_SW' 5. 'DEFAULT_SW' 6. 'SORT_SEQ' 7. 'VERSION' 8. 'ADHOC_CHAR_VAL' 9. 'CHAR_VAL_FK1' 10. 'CHAR_VAL_FK2' 11. 'CHAR_VAL_FK3' 12. 'CHAR_VAL_FK4' 13. 'CHAR_VAL_FK5'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'CHAR_TYPE_CD'  2. 'TD_TYPE_CD' . 
# Table 'CI_CHTY_TDTY' has 3 foreign keys as listed:  'CHAR_VAL' is foreign key from table 'CI_CHAR_VAL', 'CHAR_TYPE_CD' is foreign key from table 'CI_CHAR_TYPE', and 'TD_TYPE_CD' is foreign key from table 'CI_TD_TYPE'.
# 'CI_CHTY_TDTY' is a child table of 'CI_TD_TYPE' table.

# Field Descriptions for table 'CI_CHTY_TDTY':

#   1. 'TD_TYPE_CD' (CHAR):- field name for To Do Type
#   2. 'CHAR_TYPE_CD' (CHAR):- field name for Characteristic Type
#   3. 'CHAR_VAL' (CHAR):- field name for Characteristic Value
#   4. 'REQUIRED_SW' (CHAR):- field name for Required
#   5. 'DEFAULT_SW' (CHAR):- field name for Default
#   6. 'SORT_SEQ' (NUMBER):- field name for Sequence,  'precision': 2
#   7. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
#   8. 'ADHOC_CHAR_VAL' (VARCHAR2):- field name for Adhoc Characteristic Value
#   9. 'CHAR_VAL_FK1' (VARCHAR2):- field name for Characteristic Value FK 1
#   10. 'CHAR_VAL_FK2' (VARCHAR2):- field name for Characteristic Value FK 2
#   11. 'CHAR_VAL_FK3' (VARCHAR2):- field name for Characteristic Value FK 3
#   12. 'CHAR_VAL_FK4' (VARCHAR2):- field name for Characteristic Value FK 4
#   13. 'CHAR_VAL_FK5' (VARCHAR2):- field name for Characteristic Value FK 5

# --------------------------------------------------------------------------

# Table 'CI_TD_TYPE_L' is used for storing To Do Type Language. Table 'CI_TD_TYPE_L' has 6 fields (columns) which are:  1. 'TD_TYPE_CD' 2. 'LANGUAGE_CD' 3. 'VERSION' 4. 'DESCR' 5. 'OWNER_FLG' 6. 'DESCRLONG'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'LANGUAGE_CD'  2. 'TD_TYPE_CD' . 
# Table 'CI_TD_TYPE_L' has 2 foreign keys as listed:  'TD_TYPE_CD' is foreign key from table 'CI_TD_TYPE', and 'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE'.
# 'CI_TD_TYPE_L' is a child table of 'CI_TD_TYPE' table.

# Field Descriptions for table 'CI_TD_TYPE_L':

#   1. 'TD_TYPE_CD' (CHAR):- field name for To Do Type
#   2. 'LANGUAGE_CD' (CHAR):- field name for Language
#   3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
#   4. 'DESCR' (VARCHAR2):- field name for Description
#   5. 'OWNER_FLG' (CHAR):- field name for Owner
#   6. 'DESCRLONG' (VARCHAR2):- field name for Detailed Description

# --------------------------------------------------------------------------

# Table 'CI_TD_DRLKEY_TY' is used for storing To Do Type Drill Key. Table 'CI_TD_DRLKEY_TY' has 6 fields (columns) which are:  1. 'TD_TYPE_CD' 2. 'SEQ_NUM' 3. 'FLD_NAME' 4. 'TBL_NAME' 5. 'VERSION' 6. 'OWNER_FLG'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'TD_TYPE_CD'  2. 'SEQ_NUM' . 
# Table 'CI_TD_DRLKEY_TY' has 3 foreign keys as listed:  'FLD_NAME' is foreign key from table 'CI_MD_FLD', 'TD_TYPE_CD' is foreign key from table 'CI_TD_TYPE', and 'TBL_NAME' is foreign key from table 'CI_MD_TBL'.
# 'CI_TD_DRLKEY_TY' is a child table of 'CI_TD_TYPE' table.

# Field Descriptions for table 'CI_TD_DRLKEY_TY':

#   1. 'TD_TYPE_CD' (CHAR):- field name for To Do Type
#   2. 'SEQ_NUM' (NUMBER):- field name for Sequence,  'precision': 3
#   3. 'FLD_NAME' (CHAR):- field name for Field
#   4. 'TBL_NAME' (CHAR):- field name for Table
#   5. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
#   6. 'OWNER_FLG' (CHAR):- field name for Owner

# --------------------------------------------------------------------------

# Table 'CI_TD_SRTKEY_TY' is used for storing To Do Type Sort Key. Table 'CI_TD_SRTKEY_TY' has 6 fields (columns) which are:  1. 'TD_TYPE_CD' 2. 'SEQ_NUM' 3. 'VERSION' 4. 'DEFAULT_SW' 5. 'ORDER_FLG' 6. 'OWNER_FLG'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'SEQ_NUM'  2. 'TD_TYPE_CD' . 
# Table 'CI_TD_SRTKEY_TY' has only one foreign key; 'TD_TYPE_CD' is a foreign key from table 'CI_TD_TYPE'.
# 'CI_TD_SRTKEY_TY' is a child table of 'CI_TD_TYPE' table.

# Field Descriptions for table 'CI_TD_SRTKEY_TY':

#   1. 'TD_TYPE_CD' (CHAR):- field name for To Do Type
#   2. 'SEQ_NUM' (NUMBER):- field name for Sequence,  'precision': 3
#   3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
#   4. 'DEFAULT_SW' (CHAR):- field name for Default
#   5. 'ORDER_FLG' (CHAR):- field name for Sort Order
#   6. 'OWNER_FLG' (CHAR):- field name for Owner

# --------------------------------------------------------------------------

# Table 'CI_TD_TYPE_ALG' is used for storing To Do Type Algorithms. Table 'CI_TD_TYPE_ALG' has 5 fields (columns) which are:  1. 'TD_TYPE_CD' 2. 'TD_TYPE_SEVT_FLG' 3. 'SEQ_NUM' 4. 'ALG_CD' 5. 'VERSION'. Out of these fields, 3 are primary keys. The composite primary keys are:  1. 'TD_TYPE_SEVT_FLG'  2. 'TD_TYPE_CD'  3. 'SEQ_NUM' . 
# Table 'CI_TD_TYPE_ALG' has 2 foreign keys as listed:  'ALG_CD' is foreign key from table 'CI_ALG', and 'TD_TYPE_CD' is foreign key from table 'CI_TD_TYPE'.
# 'CI_TD_TYPE_ALG' is a child table of 'CI_TD_TYPE' table.

# Field Descriptions for table 'CI_TD_TYPE_ALG':

#   1. 'TD_TYPE_CD' (CHAR):- field name for To Do Type
#   2. 'TD_TYPE_SEVT_FLG' (CHAR):- field name for System Event
#   3. 'SEQ_NUM' (NUMBER):- field name for Sequence,  'precision': 3
#   4. 'ALG_CD' (CHAR):- field name for Algorithm
#   5. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

# --------------------------------------------------------------------------

# Table 'CI_TD_VAL_ROLE' is used for storing To Do Type Role. Table 'CI_TD_VAL_ROLE' has 4 fields (columns) which are:  1. 'VERSION' 2. 'DEFAULT_SW' 3. 'TD_TYPE_CD' 4. 'ROLE_ID'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'ROLE_ID'  2. 'TD_TYPE_CD' . 
# Table 'CI_TD_VAL_ROLE' has 2 foreign keys as listed:  'TD_TYPE_CD' is foreign key from table 'CI_TD_TYPE', and 'ROLE_ID' is foreign key from table 'CI_ROLE'.
# 'CI_TD_VAL_ROLE' is a child table of 'CI_TD_TYPE' table.

# Field Descriptions for table 'CI_TD_VAL_ROLE':

#   1. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
#   2. 'DEFAULT_SW' (CHAR):- field name for Default
#   3. 'TD_TYPE_CD' (CHAR):- field name for To Do Type
#   4. 'ROLE_ID' (CHAR):- field name for To Do Role

# --------------------------------------------------------------------------

# Table 'CI_TD_EX_LIST' is used for storing To Do Type Message Overrides. Table 'CI_TD_EX_LIST' has 7 fields (columns) which are:  1. 'TD_TYPE_CD' 2. 'MESSAGE_CAT_NBR' 3. 'MESSAGE_NBR' 4. 'OVERRIDE_ROLE' 5. 'EXCLUDE_SW' 6. 'VERSION' 7. 'SCR_CD'. Out of these fields, 3 are primary keys. The composite primary keys are:  1. 'TD_TYPE_CD'  2. 'MESSAGE_NBR'  3. 'MESSAGE_CAT_NBR' . 
# Table 'CI_TD_EX_LIST' has 4 foreign keys as listed:  'TD_TYPE_CD' is foreign key from table 'CI_TD_TYPE', 'SCR_CD' is foreign key from table 'CI_SCR', 'MESSAGE_CAT_NBR' is foreign key from table 'CI_MSG', and 'OVERRIDE_ROLE' is foreign key from table 'CI_ROLE'.
# 'CI_TD_EX_LIST' is a child table of 'CI_TD_TYPE' table.

# Field Descriptions for table 'CI_TD_EX_LIST':

#   1. 'TD_TYPE_CD' (CHAR):- field name for To Do Type
#   2. 'MESSAGE_CAT_NBR' (NUMBER):- field name for Message Category,  'precision': 5
#   3. 'MESSAGE_NBR' (NUMBER):- field name for Message Number,  'precision': 5
#   4. 'OVERRIDE_ROLE' (CHAR):- field name for Override Role
#   5. 'EXCLUDE_SW' (CHAR):- field name for Exclude To Do Entry
#   6. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
#   7. 'SCR_CD' (CHAR):- field name for Script

# --------------------------------------------------------------------------

# Table 'CI_TD_SRTKEY_TY_L' is used for storing To Do Type Sort Key Language. Table 'CI_TD_SRTKEY_TY_L' has 6 fields (columns) which are:  1. 'TD_TYPE_CD' 2. 'SEQ_NUM' 3. 'LANGUAGE_CD' 4. 'VERSION' 5. 'DESCR' 6. 'OWNER_FLG'. Out of these fields, 3 are primary keys. The composite primary keys are:  1. 'LANGUAGE_CD'  2. 'TD_TYPE_CD'  3. 'SEQ_NUM' . 
# Table 'CI_TD_SRTKEY_TY_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'TD_TYPE_CD' is foreign key from table 'CI_TD_SRTKEY_TY'.
# 'CI_TD_SRTKEY_TY_L' is a child table of 'CI_TD_TYPE' table.

# Field Descriptions for table 'CI_TD_SRTKEY_TY_L':

#   1. 'TD_TYPE_CD' (CHAR):- field name for To Do Type
#   2. 'SEQ_NUM' (NUMBER):- field name for Sequence,  'precision': 3
#   3. 'LANGUAGE_CD' (CHAR):- field name for Language
#   4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
#   5. 'DESCR' (VARCHAR2):- field name for Description
#   6. 'OWNER_FLG' (CHAR):- field name for Owner
# ---------------------------------------------------------------------------
  
# """,
#     "TO_DO_TYPE": """
# Tables and Field Reference for storing To Do Type:

#   1. 'CI_TD_TYPE' (Primary Table):
#       -Fields: 'TD_TYPE_CD', 'CRE_BATCH_CD', 'MESSAGE_CAT_NBR', 'MESSAGE_NBR', 'RTE_BATCH_CD', 'VERSION', 'OWNER_FLG', 'TD_USAGE_TYPE_FLG', 'TD_PRIORITY_FLG', 'NAV_OPT_CD'.
#       -Primary Key: 'TD_TYPE_CD'

#   2. 'CI_TD_TYPE_L':
#       -Fields: 'TD_TYPE_CD', 'LANGUAGE_CD', 'VERSION', 'DESCR', 'OWNER_FLG', 'DESCRLONG'. 
#       -Composite Primary Key: 'LANGUAGE_CD', 'TD_TYPE_CD' 

#   3. 'CI_TD_TYPE_CHAR':
#       -Fields: 'TD_TYPE_CD', 'CHAR_TYPE_CD', 'SEQ_NUM', 'CHAR_VAL', 'ADHOC_CHAR_VAL', 'CHAR_VAL_FK1', 'CHAR_VAL_FK2', 'CHAR_VAL_FK3', 'CHAR_VAL_FK4', 'CHAR_VAL_FK5', 'SRCH_CHAR_VAL', 'VERSION'. 
#       -Composite Primary Key: 'TD_TYPE_CD', 'SEQ_NUM', 'CHAR_TYPE_CD' 
  
#   4. 'CI_TD_TYPE_ALG':
#       -Fill all 5 Fields: 'TD_TYPE_CD', 'TD_TYPE_SEVT_FLG', 'SEQ_NUM', 'ALG_CD', 'VERSION'.
#       -Composite Primary Key: 'TD_TYPE_SEVT_FLG', 'TD_TYPE_CD', 'SEQ_NUM' 
  
#   5. 'CI_CHTY_TDTY':
#       -Fields: 'TD_TYPE_CD', 'CHAR_TYPE_CD', 'CHAR_VAL', 'REQUIRED_SW', 'DEFAULT_SW', 'SORT_SEQ', 'VERSION', 'ADHOC_CHAR_VAL', 'CHAR_VAL_FK1', 'CHAR_VAL_FK2', 'CHAR_VAL_FK3', 'CHAR_VAL_FK4', 'CHAR_VAL_FK5'. 
#       -Composite Primary Key: 'CHAR_TYPE_CD', 'TD_TYPE_CD'

#   6. 'CI_TD_DRLKEY_TY':
#       -Fields: 'TD_TYPE_CD', 'SEQ_NUM', 'FLD_NAME', 'TBL_NAME', 'VERSION', 'OWNER_FLG'. 
#       -Composite Primary Key: 'TD_TYPE_CD', 'SEQ_NUM' 

#   7. 'CI_TD_SRTKEY_TY':
#       -Fields: 'TD_TYPE_CD', 'SEQ_NUM', 'VERSION', 'DEFAULT_SW', 'ORDER_FLG', 'OWNER_FLG'. 
#       -Composite Primary Key: 'SEQ_NUM', 'TD_TYPE_CD'

#   8. 'CI_TD_SRTKEY_TY_L':
#       -Fields: 'TD_TYPE_CD', 'SEQ_NUM', 'LANGUAGE_CD', 'VERSION', 'DESCR', 'OWNER_FLG'.
#       -Composite Primary Key: 'LANGUAGE_CD', 'TD_TYPE_CD', 'SEQ_NUM' 

#   9. 'CI_TD_VAL_ROLE':
#       -Fill al 4 Fields: 'TD_TYPE_CD', 'ROLE_ID', 'VERSION', 'DEFAULT_SW'.
#       -Composite Primary Key: 'ROLE_ID', 'TD_TYPE_CD'

#   10. 'CI_TD_EX_LIST':
#       -Fill all 7 Fields: 'TD_TYPE_CD', 'MESSAGE_CAT_NBR', 'MESSAGE_NBR', 'OVERRIDE_ROLE', 'EXCLUDE_SW', 'VERSION', 'SCR_CD'. 
#       -Composite Primary Key: 'TD_TYPE_CD', 'MESSAGE_NBR', 'MESSAGE_CAT_NBR'

# Instructions:
#   -Insert To Do Type in 'CI_TD_TYPE'.
#   -Insert language details in 'CI_TD_TYPE_L'.
#   -Insert to do type characteristics in 'CI_TD_TYPE_CHAR'.
#   -Insert To Do Type Algorithms in 'CI_TD_TYPE_ALG'.
#   -Insert Template Characteristics in 'CI_CHTY_TDTY'.
#   -Insert Drill Key in 'CI_TD_DRLKEY_TY'.
#   -Insert Sort Key in 'CI_TD_SRTKEY_TY'.
#   -Insert Sort Key Language in 'CI_TD_SRTKEY_TY_L'.
#   -Insert To Do Type Role in 'CI_TD_VAL_ROLE'.
#   -Insert Message Overrides in 'CI_TD_EX_LIST'.

# Fill ALL tables with ALL fields correctly. Field Names must not be changed even to the slightest since changing a field name may have catastrophic effects in an SQL query. eg: Don't convert 'ALG_CD' to 'ALGORITHM_CD' on your own. Respect the name given.

# """,
"TO_DO_TYPE":"""

Following are steps to configure To Do Type:

Step 1: Fill the below CI_TD tables with 1 insert query.

  -CI_TD_TYPE: This is the primary table for storing To Do Type. 10 fields: TD_TYPE_CD (PK), CRE_BATCH_CD, MESSAGE_CAT_NBR, MESSAGE_NBR, RTE_BATCH_CD, VERSION, OWNER_FLG, TD_USAGE_TYPE_FLG, TD_PRIORITY_FLG, and NAV_OPT_CD.

  -CI_TD_TYPE_L: 6 fields: TD_TYPE_CD (PK), LANGUAGE_CD (PK), VERSION, DESCR, DESCRLONG and OWNER_FLG. 

  -CI_TD_TYPE_ALG: 5 fields: TD_TYPE_CD (PK), TD_TYPE_SEVT_FLG (PK), SEQ_NUM (PK), ALG_CD, and VERSION. 

  -CI_TD_TYPE_CHAR: 12 fields: TD_TYPE_CD (PK), CHAR_TYPE_CD (PK), SEQ_NUM (PK), CHAR_VAL, ADHOC_CHAR_VAL, CHAR_VAL_FK1, CHAR_VAL_FK2, CHAR_VAL_FK3, CHAR_VAL_FK4, CHAR_VAL_FK5, SRCH_CHAR_VAL, and VERSION. 

  -CI_CHTY_TDTY: 13 fields: TD_TYPE_CD (PK), CHAR_TYPE_CD (PK), CHAR_VAL, REQUIRED_SW, DEFAULT_SW, SORT_SEQ, VERSION, ADHOC_CHAR_VAL, CHAR_VAL_FK1, CHAR_VAL_FK2, CHAR_VAL_FK3, CHAR_VAL_FK4, and CHAR_VAL_FK5. 
 
  -CI_TD_DRLKEY_TY: 6 fields: TD_TYPE_CD (PK), SEQ_NUM (PK), FLD_NAME, TBL_NAME, VERSION, and OWNER_FLG. 

  -CI_TD_SRTKEY_TY: 6 fields: TD_TYPE_CD (PK), SEQ_NUM (PK), VERSION, DEFAULT_SW, ORDER_FLG, and OWNER_FLG. 

  -CI_TD_VAL_ROLE: 4 fields: TD_TYPE_CD (PK), ROLE_ID (PK), VERSION, and DEFAULT_SW.

  -CI_TD_SRTKEY_TY_L: 6 fields: TD_TYPE_CD (PK), SEQ_NUM (PK), LANGUAGE_CD (PK), VERSION, DESCR, and OWNER_FLG. 

  -CI_TD_EX_LIST: 7 fields: TD_TYPE_CD (PK), MESSAGE_CAT_NBR (PK), MESSAGE_NBR (PK), OVERRIDE_ROLE, EXCLUDE_SW, VERSION, and SCR_CD. 

  Only output queries for the above exact 10 tables with the exact field names mentioned. It is illegal to change any table/ field names. 
""",
    "USER_GROUP": """

Table 'SC_USER_GROUP' is used for storing User Group. Table 'SC_USER_GROUP' has 3 fields (columns) which are:  1. 'USR_GRP_ID' 2. 'VERSION' 3. 'OWNER_FLG'. Out of these fields, only one is a primary key; 'USR_GRP_ID' is the primary key for 'SC_USER_GROUP'
'SC_USER_GROUP' is a Primary Table.

Field Descriptions for table 'SC_USER_GROUP':

  1. 'USR_GRP_ID' (CHAR):- field name for User Group
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  3. 'OWNER_FLG' (CHAR):- field name for Owner

The child tables of 'SC_USER_GROUP' are ['SC_ACCESS_CNTL', 'CI_USR_GRP_SC', 'SC_USER_GROUP_L', 'SC_USR_GRP_PROF']. 

---------------------------------------------------------------------------

Table 'SC_USER_GROUP_L' is used for storing User Group Language. Table 'SC_USER_GROUP_L' has 5 fields (columns) which are:  1. 'USR_GRP_ID' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'VERSION' 5. 'OWNER_FLG'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'USR_GRP_ID'  2. 'LANGUAGE_CD' . 
'SC_USER_GROUP_L' is a child table.

Field Descriptions for table 'SC_USER_GROUP_L':

  1. 'USR_GRP_ID' (CHAR):- field name for User Group
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  5. 'OWNER_FLG' (CHAR):- field name for Owner

--------------------------------------------------------------------------

Table 'SC_ACCESS_CNTL' is used for storing User Group Access Control. Table 'SC_ACCESS_CNTL' has 5 fields (columns) which are:  1. 'USR_GRP_ID' 2. 'APP_SVC_ID' 3. 'ACCESS_MODE' 4. 'VERSION' 5. 'OWNER_FLG'. Out of these fields, 3 are primary keys. The composite primary keys are:  1. 'USR_GRP_ID'  2. 'APP_SVC_ID'  3. 'ACCESS_MODE' . 
'SC_ACCESS_CNTL' is a child table.

Field Descriptions for table 'SC_ACCESS_CNTL':

  1. 'USR_GRP_ID' (CHAR):- field name for User Group
  2. 'APP_SVC_ID' (CHAR):- field name for Application Service
  3. 'ACCESS_MODE' (CHAR):- field name for Access Mode
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  5. 'OWNER_FLG' (CHAR):- field name for Owner

--------------------------------------------------------------------------

Table 'CI_USR_GRP_SC' is used for storing User Group Security Type. Table 'CI_USR_GRP_SC' has 5 fields (columns) which are:  1. 'USR_GRP_ID' 2. 'APP_SVC_ID' 3. 'SC_TYPE_CD' 4. 'AUTH_LEVEL_NBR' 5. 'VERSION'. Out of these fields, 3 are primary keys. The composite primary keys are:  1. 'APP_SVC_ID'  2. 'USR_GRP_ID'  3. 'SC_TYPE_CD' . 
'CI_USR_GRP_SC' is a child table.

Field Descriptions for table 'CI_USR_GRP_SC':

  1. 'USR_GRP_ID' (CHAR):- field name for User Group
  2. 'APP_SVC_ID' (CHAR):- field name for Application Service
  3. 'SC_TYPE_CD' (CHAR):- field name for Security Type
  4. 'AUTH_LEVEL_NBR' (CHAR):- field name for Authorization Level
  5. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

--------------------------------------------------------------------------

Table 'SC_USR_GRP_PROF' is used for storing User Group Profile. Table 'SC_USR_GRP_PROF' has 5 fields (columns) which are:  1. 'USR_GRP_ID' 2. 'APP_SVC_ID' 3. 'EXPIRATION_DT' 4. 'VERSION' 5. 'OWNER_FLG'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'APP_SVC_ID'  2. 'USR_GRP_ID' . 
'SC_USR_GRP_PROF' is a child table.

Field Descriptions for table 'SC_USR_GRP_PROF':

  1. 'USR_GRP_ID' (CHAR):- field name for User Group
  2. 'APP_SVC_ID' (CHAR):- field name for Application Service
  3. 'EXPIRATION_DT' (DATE):- field name for Expiration Date, 'nullable': True
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  5. 'OWNER_FLG' (CHAR):- field name for Owner
---------------------------------------------------------------------------

Fill all the tables above with respect to the question.

""",

    "DATA_ACCESS_ROLE": """

Table 'CI_DAR' is used for storing Data Access Role. Table 'CI_DAR' has 2 fields (columns) which are:  1. 'DAR_CD' 2. 'VERSION'. Out of these fields, only one is a primary key; 'DAR_CD' is the primary key for 'CI_DAR'
'CI_DAR' is a Primary Table.

Field Descriptions for table 'CI_DAR':

  1. 'DAR_CD' (CHAR):- field name for Data Access Role
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

The child tables of 'CI_DAR' are ['CI_DAR_L', 'CI_DAR_USR', 'CI_ACC_GRP_DAR']. 
(Generated when 'MAINT_OBJ_CD'=DATA ACCESS)

--------------------------------------------------------------------------

Table 'CI_DAR_L' is used for storing Data Access Role Language. Table 'CI_DAR_L' has 4 fields (columns) which are:  1. 'DAR_CD' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'DAR_CD'  2. 'LANGUAGE_CD' . 
Table 'CI_DAR_L' has 2 foreign keys as listed:  'DAR_CD' is foreign key from table 'CI_DAR', and 'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE'.
'CI_DAR_L' is a child table of 'CI_DAR' table.

Field Descriptions for table 'CI_DAR_L':

  1. 'DAR_CD' (CHAR):- field name for Data Access Role
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

--------------------------------------------------------------------------

Table 'CI_DAR_USR' is used for storing Data Access User. Table 'CI_DAR_USR' has 4 fields (columns) which are:  1. 'DAR_CD' 2. 'USER_ID' 3. 'EXPIRE_DT' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'DAR_CD'  2. 'USER_ID' . 
Table 'CI_DAR_USR' has 2 foreign keys as listed:  'DAR_CD' is foreign key from table 'CI_DAR', and 'USER_ID' is foreign key from table 'SC_USER'.
'CI_DAR_USR' is a child table of 'CI_DAR' table.

Field Descriptions for table 'CI_DAR_USR':

  1. 'DAR_CD' (CHAR):- field name for Data Access Role
  2. 'USER_ID' (CHAR):- field name for User
  3. 'EXPIRE_DT' (DATE):- field name for Expire Date, 'nullable': True
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

--------------------------------------------------------------------------

Table 'CI_ACC_GRP_DAR' is used for storing Access Group / Data Access Group. Table 'CI_ACC_GRP_DAR' has 3 fields (columns) which are:  1. 'ACCESS_GRP_CD' 2. 'DAR_CD' 3. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'ACCESS_GRP_CD'  2. 'DAR_CD' . 
Table 'CI_ACC_GRP_DAR' has 2 foreign keys as listed:  'ACCESS_GRP_CD' is foreign key from table 'CI_ACC_GRP', and 'DAR_CD' is foreign key from table 'CI_DAR'.
'CI_ACC_GRP_DAR' is a child table of 'CI_DAR' table.

Field Descriptions for table 'CI_ACC_GRP_DAR':

  1. 'ACCESS_GRP_CD' (CHAR):- field name for Access Group
  2. 'DAR_CD' (CHAR):- field name for Data Access Role
  3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
---------------------------------------------------------------------------
""",
    "ACCESS_GROUP": """
    
Table 'CI_ACC_GRP' is used for storing Access Group. Table 'CI_ACC_GRP' has 2 fields (columns) which are:  1. 'ACCESS_GRP_CD' 2. 'VERSION'. Out of these fields, only one is a primary key; 'ACCESS_GRP_CD' is the primary key for 'CI_ACC_GRP'
'CI_ACC_GRP' is a Primary Table.

Field Descriptions for table 'CI_ACC_GRP':

  1. 'ACCESS_GRP_CD' (CHAR):- field name for Access Group
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

The child tables of 'CI_ACC_GRP' are ['CI_ACC_GRP_L', 'CI_ACC_GRP_ROLE', 'CI_ACC_GRP_DAR']. 
(Generated when 'MAINT_OBJ_CD'=ACCT GROUP)

--------------------------------------------------------------------------

Table 'CI_ACC_GRP_L' is used for storing Access Group Language. Table 'CI_ACC_GRP_L' has 4 fields (columns) which are:  1. 'ACCESS_GRP_CD' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'LANGUAGE_CD'  2. 'ACCESS_GRP_CD' . 
Table 'CI_ACC_GRP_L' has 2 foreign keys as listed:  'ACCESS_GRP_CD' is foreign key from table 'CI_ACC_GRP', and 'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE'.
'CI_ACC_GRP_L' is a child table of 'CI_ACC_GRP' table.

Field Descriptions for table 'CI_ACC_GRP_L':

  1. 'ACCESS_GRP_CD' (CHAR):- field name for Access Group
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

--------------------------------------------------------------------------

Table 'CI_ACC_GRP_ROLE' is used for storing Access Group Role. Table 'CI_ACC_GRP_ROLE' has 4 fields (columns) which are:  1. 'ACCESS_GRP_CD' 2. 'TD_TYPE_CD' 3. 'ROLE_ID' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'ACCESS_GRP_CD'  2. 'TD_TYPE_CD' . 
Table 'CI_ACC_GRP_ROLE' has 2 foreign keys as listed:  'ACCESS_GRP_CD' is foreign key from table 'CI_ACC_GRP', and 'ROLE_ID' is foreign key from table 'CI_TD_VAL_ROLE'.
'CI_ACC_GRP_ROLE' is a child table of 'CI_ACC_GRP' table.

Field Descriptions for table 'CI_ACC_GRP_ROLE':

  1. 'ACCESS_GRP_CD' (CHAR):- field name for Access Group
  2. 'TD_TYPE_CD' (CHAR):- field name for To Do Type
  3. 'ROLE_ID' (CHAR):- field name for To Do Role
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

--------------------------------------------------------------------------

Table 'CI_ACC_GRP_DAR' is used for storing Access Group / Data Access Group. Table 'CI_ACC_GRP_DAR' has 3 fields (columns) which are:  1. 'ACCESS_GRP_CD' 2. 'DAR_CD' 3. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'ACCESS_GRP_CD'  2. 'DAR_CD' . 
Table 'CI_ACC_GRP_DAR' has 2 foreign keys as listed:  'ACCESS_GRP_CD' is foreign key from table 'CI_ACC_GRP', and 'DAR_CD' is foreign key from table 'CI_DAR'.
'CI_ACC_GRP_DAR' is a child table of 'CI_ACC_GRP' table.

Field Descriptions for table 'CI_ACC_GRP_DAR':

  1. 'ACCESS_GRP_CD' (CHAR):- field name for Access Group
  2. 'DAR_CD' (CHAR):- field name for Data Access Role
  3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
---------------------------------------------------------------------------

""",
    "TENDER_SOURCE": """
Table 'CI_TNDR_SRCE' is used for storing Tender Source. Table 'CI_TNDR_SRCE' has 12 fields (columns) which are:  1. 'TNDR_SOURCE_CD' 2. 'TNDR_SRCE_TYPE_FLG' 3. 'SA_ID' 4. 'CURRENCY_CD' 5. 'EXT_SOURCE_ID' 6. 'BANK_ACCT_KEY' 7. 'BANK_CD' 8. 'VERSION' 9. 'DFLT_START_BALANCE' 10. 'MAX_AMT_BALANCE' 11. 'PRINTER_IP_ADDRESS' 12. 'PRINTER_PORT'. Out of these fields, only one is a primary key; 'TNDR_SOURCE_CD' is the primary key for 'CI_TNDR_SRCE'. 
Table 'CI_TNDR_SRCE' has 3 foreign keys as listed:  'SA_ID' is foreign key from table 'CI_SA', 'BANK_CD' is foreign key from table 'CI_BANK_ACCOUNT', and 'CURRENCY_CD' is foreign key from table 'CI_CURRENCY_CD'.
'CI_TNDR_SRCE' is a Primary Table.

Field Descriptions for table 'CI_TNDR_SRCE':

  1. 'TNDR_SOURCE_CD' (CHAR):- field name for Tender Source
  2. 'TNDR_SRCE_TYPE_FLG' (CHAR):- field name for Tender Source Type
  3. 'SA_ID' (CHAR):- field name for Service Agreement
  4. 'CURRENCY_CD' (CHAR):- field name for Currency Code
  5. 'EXT_SOURCE_ID' (CHAR):- field name for External Source ID
  6. 'BANK_ACCT_KEY' (CHAR):- field name for Bank Account
  7. 'BANK_CD' (CHAR):- field name for Bank
  8. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  9. 'DFLT_START_BALANCE' (NUMBER):- field name for Default Starting Balance,  'precision': 15
  10. 'MAX_AMT_BALANCE' (NUMBER):- field name for Max Amount Balance,  'precision': 15
  11. 'PRINTER_IP_ADDRESS' (VARCHAR2):- field name for Printer IP Address, 'nullable': True
  12. 'PRINTER_PORT' (VARCHAR2):- field name for Printer Port, 'nullable': True

The child tables of 'CI_TNDR_SRCE' are ['CI_TNDR_SRCE_L']. 
(Generated when 'MAINT_OBJ_CD'=TENDER SRC)

--------------------------------------------------------------------------

Table 'CI_TNDR_SRCE_L' is used for storing Tender Source Language. Table 'CI_TNDR_SRCE_L' has 4 fields (columns) which are:  1. 'TNDR_SOURCE_CD' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'TNDR_SOURCE_CD'  2. 'LANGUAGE_CD' . 
Table 'CI_TNDR_SRCE_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'TNDR_SOURCE_CD' is foreign key from table 'CI_TNDR_SRCE'.
'CI_TNDR_SRCE_L' is a child table of 'CI_TNDR_SRCE' table.

Field Descriptions for table 'CI_TNDR_SRCE_L':

  1. 'TNDR_SOURCE_CD' (CHAR):- field name for Tender Source
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
---------------------------------------------------------------------------
""",
    "TENDER_TYPE": """
Table 'CI_TENDER_TYPE' is used for storing Tender Type. Table 'CI_TENDER_TYPE' has 10 fields (columns) which are:  1. 'TENDER_TYPE_CD' 2. 'VERSION' 3. 'LIKE_CASH_SW' 4. 'GENERATE_APAY_SW' 5. 'EXT_TYPE_FLG' 6. 'REQ_EXT_SRC_ID_SW' 7. 'REQ_EXPIRE_DT_SW' 8. 'ALLOW_CASH_BACK_SW' 9. 'BUS_OBJ_CD' 10. 'TENDER_AUTH_FLG'. Out of these fields, only one is a primary key; 'TENDER_TYPE_CD' is the primary key for 'CI_TENDER_TYPE'. 
Table 'CI_TENDER_TYPE' has only one foreign key; 'BUS_OBJ_CD' is a foreign key from table 'F1_BUS_OBJ'.
'CI_TENDER_TYPE' is a Primary Table.

Field Descriptions for table 'CI_TENDER_TYPE':

  1. 'TENDER_TYPE_CD' (CHAR):- field name for Tender Type
  2. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  3. 'LIKE_CASH_SW' (CHAR):- field name for Like Cash (Yes 'Y' or No 'N')
  4. 'GENERATE_APAY_SW' (CHAR):- field name for Generate Auto Pay (Yes 'Y' or No 'N')
  5. 'EXT_TYPE_FLG' (CHAR):- field name for External Type
  6. 'REQ_EXT_SRC_ID_SW' (CHAR):- field name for Require External Source ID (Yes 'Y' or No 'N')
  7. 'REQ_EXPIRE_DT_SW' (CHAR):- field name for Expiration Date Required (Yes 'Y' or No 'N')
  8. 'ALLOW_CASH_BACK_SW' (CHAR):- field name for Allow Cash Back (Yes 'Y' or No 'N')
  9. 'BUS_OBJ_CD' (CHAR):- field name for Business Object
  10. 'TENDER_AUTH_FLG' (CHAR):- field name for Tender Authorization, value: 'C1NR'

The child tables of 'CI_TENDER_TYPE' are ['CI_TENDER_TYPE_L']. 
(Generated when 'MAINT_OBJ_CD'=TENDER TYPE)

--------------------------------------------------------------------------

Table 'CI_TENDER_TYPE_L' is used for storing Tender Type Language. Table 'CI_TENDER_TYPE_L' has 4 fields (columns) which are:  1. 'TENDER_TYPE_CD' 2. 'LANGUAGE_CD' 3. 'DESCR' 4. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'LANGUAGE_CD'  2. 'TENDER_TYPE_CD' . 
Table 'CI_TENDER_TYPE_L' has 2 foreign keys as listed:  'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', and 'TENDER_TYPE_CD' is foreign key from table 'CI_TENDER_TYPE'.
'CI_TENDER_TYPE_L' is a child table of 'CI_TENDER_TYPE' table.

Field Descriptions for table 'CI_TENDER_TYPE_L':

  1. 'TENDER_TYPE_CD' (CHAR):- field name for Tender Type
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'DESCR' (VARCHAR2):- field name for Description
  4. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

These tables are to be used for configuring tender types, or types of tenders.
---------------------------------------------------------------------------

""",
#     "TERMS_OF_SERVICE_TYPE": """
# Table 'CI_TOS_TYPE' is used for storing Terms of Service Type. Table 'CI_TOS_TYPE' has 3 fields (columns) which are:  1. 'TOS_TYPE_CD' 2. 'TMPL_SA_USAGE_FLG' 3. 'VERSION'. Out of these fields, only one is a primary key; 'TOS_TYPE_CD' is the primary key for 'CI_TOS_TYPE'
# 'CI_TOS_TYPE' is a Primary Table.

# Field Descriptions for table 'CI_TOS_TYPE':

#   1. 'TOS_TYPE_CD' (CHAR):- field name for Terms of Service Type
#   2. 'TMPL_SA_USAGE_FLG' (CHAR):- field name for Template SA Usage
#   3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

# The child tables of 'CI_TOS_TYPE' are ['CI_TOS_TYPE_CE', 'CI_TOS_TYPE_L', 'CI_CHTY_TOSTY', 'CI_UATY_TOSTY']. 
# (Generated when 'MAINT_OBJ_CD'=TOS TYPE)

# --------------------------------------------------------------------------

# Table 'CI_TOS_TYPE_CE' is used for storing Terms of Service Type Covered Entity. Table 'CI_TOS_TYPE_CE' has 6 fields (columns) which are:  1. 'TOS_TYPE_CD' 2. 'CHAR_TYPE_CD' 3. 'SORT_SEQ5' 4. 'REQUIRED_SW' 5. 'DEFAULT_SW' 6. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'CHAR_TYPE_CD'  2. 'TOS_TYPE_CD' . 
# Table 'CI_TOS_TYPE_CE' has 2 foreign keys as listed:  'CHAR_TYPE_CD' is foreign key from table 'CI_CHAR_TYPE', and 'TOS_TYPE_CD' is foreign key from table 'CI_TOS_TYPE'.
# 'CI_TOS_TYPE_CE' is a child table of 'CI_TOS_TYPE' table.

# Field Descriptions for table 'CI_TOS_TYPE_CE':

#   1. 'TOS_TYPE_CD' (CHAR):- field name for Terms of Service Type
#   2. 'CHAR_TYPE_CD' (CHAR):- field name for Characteristic Type
#   3. 'SORT_SEQ5' (NUMBER):- field name for Sequence,  'precision': 5
#   4. 'REQUIRED_SW' (CHAR):- field name for Required
#   5. 'DEFAULT_SW' (CHAR):- field name for Default
#   6. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

# --------------------------------------------------------------------------

# Table 'CI_TOS_TYPE_L' is used for storing Terms of Service Type Language. Table 'CI_TOS_TYPE_L' has 4 fields (columns) which are:  1. 'TOS_TYPE_CD' 2. 'LANGUAGE_CD' 3. 'VERSION' 4. 'DESCR'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'TOS_TYPE_CD'  2. 'LANGUAGE_CD' . 
# Table 'CI_TOS_TYPE_L' has 2 foreign keys as listed:  'TOS_TYPE_CD' is foreign key from table 'CI_TOS_TYPE', and 'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE'.
# 'CI_TOS_TYPE_L' is a child table of 'CI_TOS_TYPE' table.

# Field Descriptions for table 'CI_TOS_TYPE_L':

#   1. 'TOS_TYPE_CD' (CHAR):- field name for Terms of Service Type
#   2. 'LANGUAGE_CD' (CHAR):- field name for Language
#   3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
#   4. 'DESCR' (VARCHAR2):- field name for Description

# --------------------------------------------------------------------------

# Table 'CI_CHTY_TOSTY' is used for storing Terms of Service Type Template Characteristics. Table 'CI_CHTY_TOSTY' has 13 fields (columns) which are:  1. 'TOS_TYPE_CD' 2. 'CHAR_TYPE_CD' 3. 'SORT_SEQ5' 4. 'REQUIRED_SW' 5. 'DEFAULT_SW' 6. 'CHAR_VAL' 7. 'VERSION' 8. 'ADHOC_CHAR_VAL' 9. 'CHAR_VAL_FK1' 10. 'CHAR_VAL_FK2' 11. 'CHAR_VAL_FK3' 12. 'CHAR_VAL_FK4' 13. 'CHAR_VAL_FK5'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'TOS_TYPE_CD'  2. 'CHAR_TYPE_CD' . 
# Table 'CI_CHTY_TOSTY' has 3 foreign keys as listed:  'TOS_TYPE_CD' is foreign key from table 'CI_TOS_TYPE', 'CHAR_TYPE_CD' is foreign key from table 'CI_CHAR_TYPE', and 'CHAR_TYPE_CD' is foreign key from table 'CI_CHAR_VAL'.
# 'CI_CHTY_TOSTY' is a child table of 'CI_TOS_TYPE' table.

# Field Descriptions for table 'CI_CHTY_TOSTY':

#   1. 'TOS_TYPE_CD' (CHAR):- field name for Terms of Service Type
#   2. 'CHAR_TYPE_CD' (CHAR):- field name for Characteristic Type
#   3. 'SORT_SEQ5' (NUMBER):- field name for Sequence,  'precision': 5
#   4. 'REQUIRED_SW' (CHAR):- field name for Required
#   5. 'DEFAULT_SW' (CHAR):- field name for Default
#   6. 'CHAR_VAL' (CHAR):- field name for Characteristic Value
#   7. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
#   8. 'ADHOC_CHAR_VAL' (VARCHAR2):- field name for Adhoc Characteristic Value
#   9. 'CHAR_VAL_FK1' (VARCHAR2):- field name for Characteristic Value FK 1
#   10. 'CHAR_VAL_FK2' (VARCHAR2):- field name for Characteristic Value FK 2
#   11. 'CHAR_VAL_FK3' (VARCHAR2):- field name for Characteristic Value FK 3
#   12. 'CHAR_VAL_FK4' (VARCHAR2):- field name for Characteristic Value FK 4
#   13. 'CHAR_VAL_FK5' (VARCHAR2):- field name for Characteristic Value FK 5

# --------------------------------------------------------------------------

# Table 'CI_UATY_TOSTY' is used for storing UA Type Terms of Service Type. Table 'CI_UATY_TOSTY' has 3 fields (columns) which are:  1. 'UA_TYPE_CD' 2. 'TOS_TYPE_CD' 3. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'UA_TYPE_CD'  2. 'TOS_TYPE_CD' . 
# Table 'CI_UATY_TOSTY' has 2 foreign keys as listed:  'TOS_TYPE_CD' is foreign key from table 'CI_TOS_TYPE', and 'UA_TYPE_CD' is foreign key from table 'CI_UA_TYPE'.
# 'CI_UATY_TOSTY' is a child table of 'CI_TOS_TYPE' table.

# Field Descriptions for table 'CI_UATY_TOSTY':

#   1. 'UA_TYPE_CD' (CHAR):- field name for Umbrella Agreement Type
#   2. 'TOS_TYPE_CD' (CHAR):- field name for Terms of Service Type
#   3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
# ---------------------------------------------------------------------------
# """,
"TOS_TYPE":"""
Fill the below tables with insert queries that include all the field names provided.

Step 1: CI_TOS_TYPE: It is the primary storage for Terms of Service Types. It consists of 3 fields:
  -TOS_TYPE_CD (PK)(CHAR): Field name for Terms of Service Type
  -TMPL_SA_USAGE_FLG (CHAR): Field name for Template SA Usage
  -VERSION (NUMBER): Field name for Version, with a precision of 5

Step 2: CI_TOS_TYPE_L: It comprises 4 fields:
  -TOS_TYPE_CD (PK)(CHAR): Field name for Terms of Service Type
  -LANGUAGE_CD (PK)(CHAR): Field name for Language
  -VERSION (NUMBER): Field name for Version, with a precision of 5
  -DESCR (VARCHAR2): Field name for Description

Step 3: CI_TOS_TYPE_CE: It consists of 6 fields:
  -TOS_TYPE_CD (PK)(CHAR): Field name for Terms of Service Type
  -CHAR_TYPE_CD (PK)(CHAR): Field name for Characteristic Type
  -SORT_SEQ5 (NUMBER): Field name for Sequence, with a precision of 5
  -REQUIRED_SW (CHAR): Field name for Required
  -DEFAULT_SW (CHAR): Field name for Default
  -VERSION (NUMBER): Field name for Version, with a precision of 5

Step 4: CI_CHTY_TOSTY: It includes 13 fields:
  -TOS_TYPE_CD (PK)(CHAR): Field name for Terms of Service Type
  -CHAR_TYPE_CD (PK)(CHAR): Field name for Characteristic Type
  -SORT_SEQ5 (NUMBER): Field name for Sequence, with a precision of 5
  -REQUIRED_SW (CHAR): Field name for Required
  -DEFAULT_SW (CHAR): Field name for Default
  -CHAR_VAL (CHAR): Field name for Characteristic Value
  -VERSION (NUMBER): Field name for Version, with a precision of 5
  -ADHOC_CHAR_VAL (VARCHAR2): Field name for Adhoc Characteristic Value
  -CHAR_VAL_FK1 (VARCHAR2): Field name for Characteristic Value FK 1
  -CHAR_VAL_FK2 (VARCHAR2): Field name for Characteristic Value FK 2
  -CHAR_VAL_FK3 (VARCHAR2): Field name for Characteristic Value FK 3
  -CHAR_VAL_FK4 (VARCHAR2): Field name for Characteristic Value FK 4
  -CHAR_VAL_FK5 (VARCHAR2): Field name for Characteristic Value FK 5

Step 5: CI_UATY_TOSTY: It contains 3 fields:
  -TOS_TYPE_CD (PK)(CHAR): Field name for Terms of Service Type
  -UA_TYPE_CD (PK)(CHAR): Field name for Umbrella Agreement Type
  -VERSION (NUMBER): Field name for Version, with a precision of 5

""",

"USER_ROLE": """

Table 'CI_ROLE_USER' is used for storing Role User. Table 'CI_ROLE_USER' has 3 fields (columns) which are:  1. 'ROLE_ID' 2. 'USER_ID' 3. 'VERSION'. Out of these fields, 2 are primary keys. The composite primary keys are:  1. 'ROLE_ID'  2. 'USER_ID' . 
Table 'CI_ROLE_USER' has 2 foreign keys as listed:  'USER_ID' is foreign key from table 'SC_USER', and 'ROLE_ID' is foreign key from table 'CI_ROLE'.
'CI_ROLE_USER' is a child table of 'SC_USER' table.

Field Descriptions for table 'CI_ROLE_USER':

  1. 'ROLE_ID' (CHAR):- field name for To Do Role
  2. 'USER_ID' (CHAR):- field name for User
  3. 'VERSION' (NUMBER):- field name for Version,  'precision': 5

---------------------------------------------------------------------------

Table 'SC_USER' is used for storing User. Table 'SC_USER' has 24 fields (columns) which are:  1. 'USER_ID' 2. 'LANGUAGE_CD' 3. 'FIRST_NAME' 4. 'LAST_NAME' 5. 'TNDR_SOURCE_CD' 6. 'VERSION' 7. 'DISP_PROF_CD' 8. 'TD_ENTRY_AGE_DAYS1' 9. 'TD_ENTRY_AGE_DAYS2' 10. 'ACCESS_GRP_CD' 11. 'EMAILID' 12. 'USER_TYPE_FLG' 13. 'PORTAL_OVRD_USER' 14. 'FAV_OVRD_USER' 15. 'DASHBOARD_WIDTH' 16. 'HOME_NAV_OPT_CD' 17. 'DISP_ALL_PREM_SW' 18. 'OWNER_FLG' 19. 'TIME_ZONE_CD' 20. 'EXT_USER_ID' 21. 'USER_ENABLE_FLG' 22. 'F1_SECURITY_HASH' 23. 'DASHBOARD_LOC_FLG' 24. 'DASHBOARD_STATE_FLG'. Out of these fields, only one is a primary key; 'USER_ID' is the primary key for 'SC_USER'. 
Table 'SC_USER' has 8 foreign keys as listed:  'DISP_PROF_CD' is foreign key from table 'CI_DISP_PROF', 'HOME_NAV_OPT_CD' is foreign key from table 'CI_NAV_OPT', 'FAV_OVRD_USER' is foreign key from table 'SC_USER', 'TIME_ZONE_CD' is foreign key from table 'CI_TIME_ZONE', 'LANGUAGE_CD' is foreign key from table 'CI_LANGUAGE', 'TNDR_SOURCE_CD' is foreign key from table 'CI_TNDR_SRCE', 'PORTAL_OVRD_USER' is foreign key from table 'SC_USER', and 'ACCESS_GRP_CD' is foreign key from table 'CI_ACC_GRP'.
'SC_USER' is a Primary Table.

Field Descriptions for table 'SC_USER':

  1. 'USER_ID' (CHAR):- field name for User
  2. 'LANGUAGE_CD' (CHAR):- field name for Language
  3. 'FIRST_NAME' (VARCHAR2):- field name for First Name
  4. 'LAST_NAME' (VARCHAR2):- field name for Last Name
  5. 'TNDR_SOURCE_CD' (CHAR):- field name for Tender Source
  6. 'VERSION' (NUMBER):- field name for Version,  'precision': 5
  7. 'DISP_PROF_CD' (CHAR):- field name for Display Profile
  8. 'TD_ENTRY_AGE_DAYS1' (NUMBER):- field name for Lower Age Limit for Yellow Bar,  'precision': 3
  9. 'TD_ENTRY_AGE_DAYS2' (NUMBER):- field name for Upper Age Limit for Yellow Bar,  'precision': 3
  10. 'ACCESS_GRP_CD' (CHAR):- field name for Access Group
  11. 'EMAILID' (VARCHAR2):- field name for Email Address
  12. 'USER_TYPE_FLG' (CHAR):- field name for User Type
  13. 'PORTAL_OVRD_USER' (CHAR):- field name for Portals Profile User
  14. 'FAV_OVRD_USER' (CHAR):- field name for Favorites Profile User
  15. 'DASHBOARD_WIDTH' (VARCHAR2):- field name for Dashboard Width
  16. 'HOME_NAV_OPT_CD' (CHAR):- field name for Home Page
  17. 'DISP_ALL_PREM_SW' (CHAR):- field name for Display All Premises
  18. 'OWNER_FLG' (CHAR):- field name for Owner
  19. 'TIME_ZONE_CD' (CHAR):- field name for Time Zone
  20. 'EXT_USER_ID' (VARCHAR2):- field name for External User Id
  21. 'USER_ENABLE_FLG' (CHAR):- field name for User Enable
  22. 'F1_SECURITY_HASH' (VARCHAR2):- field name for F1_SECURITY_HASH
  23. 'DASHBOARD_LOC_FLG' (CHAR):- field name for Dashboard Location
  24. 'DASHBOARD_STATE_FLG' (CHAR):- field name for Dashboard State

""",
"CALCULATION_RULE":"""
Fill the below tables with insert queries that include all the field names provided.

Step 1: C1_CALC_RULE: It is used for storing Calculation Rule. It consists of 15 fields:
  -CALC_GRP_CD (PK)(VARCHAR2):- field name for Calculation Group
  -CALC_RULE_CD (PK)(VARCHAR2):- field name for Calculation Rule
  -CR_EXEC_SEQ (NUMBER):- field name for Sequence, with a precision of 5
  -REF_CALC_GRP_CD (VARCHAR2):- field name for Calculation Group
  -CALC_RULE_STEP_ALG_CD (CHAR):- field name for Step Multiplier Algorithm
  -CALC_RULE_VAL_ALG_CD (CHAR):- field name for Algorithm
  -UOM_CD (VARCHAR2):- field name for Unit of Measure
  -TOU_CD (VARCHAR2):- field name for Time of Use
  -SQI_CD (VARCHAR2):- field name for SQI
  -ITEM_TYPE_CD (VARCHAR2):- field name for Item Type
  -BF_CD (CHAR):- field name for Bill Factor
  -BUS_OBJ_CD (CHAR):- field name for Business Object
  -BO_DATA_AREA (CLOB):- field name for Business Object Data Area, nullable: True
  -VERSION (NUMBER):- field name for Version, with a precision of 5
  -DST_ID (CHAR):- field name for Distribution Code

Step 2: C1_CALC_RULE_L: It is used for storing Calculation Rule Language. It consists of 7 fields:
  -CALC_GRP_CD (PK)(VARCHAR2):- field name for Calculation Group
  -CALC_RULE_CD (PK)(VARCHAR2):- field name for Calculation Rule
  -LANGUAGE_CD (PK)(CHAR):- field name for Language
  -DESCR_TMPLT (VARCHAR2):- field name for Description On Bill
  -DESCR100 (VARCHAR2):- field name for Description
  -DESCRLONG (VARCHAR2):- field name for Detailed Description
  -VERSION (NUMBER):- field name for Version, with a precision of 5

Step 3: C1_CALC_RULE_TRGT_CAT: It is used for storing Calculation Rule Target Category. It consists of 5 fields:
  -CALC_GRP_CD (PK)(VARCHAR2):- field name for Calculation Group
  -CALC_RULE_CD (PK)(VARCHAR2):- field name for Calculation Rule
  -CL_CAT_TYPE_CD (PK)(VARCHAR2):- field name for Category Type
  -CL_CAT_VAL (PK)(VARCHAR2):- field name for Category Value
  -VERSION (NUMBER):- field name for Version, with a precision of 5
  
Step 4: C1_CALC_RULE_CHAR: It is used for storing Calculation Rule Characteristics. It consists of 12 fields:
  -CALC_GRP_CD (PK)(VARCHAR2):- field name for Calculation Group
  -CALC_RULE_CD (PK)(VARCHAR2):- field name for Calculation Rule
  -CHAR_TYPE_CD (PK)(CHAR):- field name for Characteristic Type
  -CHAR_VAL (CHAR):- field name for Characteristic Value
  -ADHOC_CHAR_VAL (VARCHAR2):- field name for Adhoc Characteristic Value
  -CHAR_VAL_FK1 (VARCHAR2):- field name for Characteristic Value FK 1
  -CHAR_VAL_FK2 (VARCHAR2):- field name for Characteristic Value FK 2
  -CHAR_VAL_FK3 (VARCHAR2):- field name for Characteristic Value FK 3
  -CHAR_VAL_FK4 (VARCHAR2):- field name for Characteristic Value FK 4
  -CHAR_VAL_FK5 (VARCHAR2):- field name for Characteristic Value FK 5
  -VERSION (NUMBER):- field name for Version, with a precision of 5
  -SRCH_CHAR_VAL (VARCHAR2):- field name for Search Characteristic Value

Step 5: C1_CALC_RULE_MBR_CAT: It is used for storing Calculation Rule Member Category. It consists of 5 fields:
  -CALC_GRP_CD (PK)(VARCHAR2):- field name for Calculation Group
  -CALC_RULE_CD (PK)(VARCHAR2):- field name for Calculation Rule
  -CL_CAT_TYPE_CD (PK)(VARCHAR2):- field name for Category Type
  -CL_CAT_VAL (PK)(VARCHAR2):- field name for Category Value
  -VERSION (NUMBER):- field name for Version, with a precision of 5

"""
}

to_do_type_1="""
Tables and Field Reference for storing To Do Type:

  1. 'CI_TD_TYPE' (Primary Table):
      -Fields: 'TD_TYPE_CD', 'CRE_BATCH_CD', 'MESSAGE_CAT_NBR', 'MESSAGE_NBR', 'RTE_BATCH_CD', 'VERSION', 'OWNER_FLG', 'TD_USAGE_TYPE_FLG', 'TD_PRIORITY_FLG', 'NAV_OPT_CD'.
      -Primary Key: 'TD_TYPE_CD'

  2. 'CI_TD_TYPE_L':
      -Fields: 'TD_TYPE_CD', 'LANGUAGE_CD', 'VERSION', 'DESCR', 'DESCRLONG', 'OWNER_FLG'. 
      -Composite Primary Key: 'LANGUAGE_CD', 'TD_TYPE_CD' 

  3. 'CI_TD_TYPE_ALG':
      -Fill all 5 Fields: 'TD_TYPE_CD', 'TD_TYPE_SEVT_FLG', 'SEQ_NUM', 'ALG_CD', 'VERSION'.
      -Composite Primary Key: 'TD_TYPE_SEVT_FLG', 'TD_TYPE_CD', 'SEQ_NUM' 
  
  4. 'CI_TD_TYPE_CHAR':
      -Fields: 'TD_TYPE_CD', 'CHAR_TYPE_CD', 'SEQ_NUM', 'CHAR_VAL', 'ADHOC_CHAR_VAL', 'CHAR_VAL_FK1', 'CHAR_VAL_FK2', 'CHAR_VAL_FK3', 'CHAR_VAL_FK4', 'CHAR_VAL_FK5', 'SRCH_CHAR_VAL', 'VERSION'. 
      -Composite Primary Key: 'TD_TYPE_CD', 'SEQ_NUM', 'CHAR_TYPE_CD' 
  
  5. 'CI_CHTY_TDTY':
      -Fields: 'TD_TYPE_CD', 'CHAR_TYPE_CD', 'CHAR_VAL', 'REQUIRED_SW', 'DEFAULT_SW', 'SORT_SEQ', 'VERSION', 'ADHOC_CHAR_VAL', 'CHAR_VAL_FK1', 'CHAR_VAL_FK2', 'CHAR_VAL_FK3', 'CHAR_VAL_FK4', 'CHAR_VAL_FK5'. 
      -Composite Primary Key: 'CHAR_TYPE_CD', 'TD_TYPE_CD'

  

Instructions:
  -Insert To Do Type in 'CI_TD_TYPE'.
  -Insert language details in 'CI_TD_TYPE_L'.
  -Insert To Do Type Algorithms in 'CI_TD_TYPE_ALG'.
  -Insert to do type characteristics in 'CI_TD_TYPE_CHAR'.
  -Insert Template Characteristics in 'CI_CHTY_TDTY'.
  
"""

to_do_type_2="""
Now fill the remaining tables:

  6. 'CI_TD_DRLKEY_TY':
      -Fields: 'TD_TYPE_CD', 'SEQ_NUM', 'FLD_NAME', 'TBL_NAME', 'VERSION', 'OWNER_FLG'. 
      -Composite Primary Key: 'TD_TYPE_CD', 'SEQ_NUM' 

  7. 'CI_TD_SRTKEY_TY':
      -Fields: 'TD_TYPE_CD', 'SEQ_NUM', 'VERSION', 'DEFAULT_SW', 'ORDER_FLG', 'OWNER_FLG'. 
      -Composite Primary Key: 'SEQ_NUM', 'TD_TYPE_CD'

  8. 'CI_TD_SRTKEY_TY_L':
      -Fields: 'TD_TYPE_CD', 'SEQ_NUM', 'LANGUAGE_CD', 'VERSION', 'DESCR', 'OWNER_FLG'.
      -Composite Primary Key: 'LANGUAGE_CD', 'TD_TYPE_CD', 'SEQ_NUM' 

  9. 'CI_TD_VAL_ROLE':
      -Fill al 4 Fields: 'TD_TYPE_CD', 'ROLE_ID', 'VERSION', 'DEFAULT_SW'.
      -Composite Primary Key: 'ROLE_ID', 'TD_TYPE_CD'

  10. 'CI_TD_EX_LIST':
      -Fill all 7 Fields: 'TD_TYPE_CD', 'MESSAGE_CAT_NBR', 'MESSAGE_NBR', 'OVERRIDE_ROLE', 'EXCLUDE_SW', 'VERSION', 'SCR_CD'. 
      -Composite Primary Key: 'TD_TYPE_CD', 'MESSAGE_NBR', 'MESSAGE_CAT_NBR'


  Instructions:
  -Insert Drill Key in 'CI_TD_DRLKEY_TY'.
  -Insert Sort Key in 'CI_TD_SRTKEY_TY'.
  -Insert Sort Key Language in 'CI_TD_SRTKEY_TY_L'.
  -Insert To Do Type Role in 'CI_TD_VAL_ROLE'.
  -Insert Message Overrides in 'CI_TD_EX_LIST'.
"""