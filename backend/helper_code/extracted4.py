import cx_Oracle
import json
from datetime import datetime
from dotenv import load_dotenv
import os

def connect_to_db(username, password, hostname, port, service_name):
    try:
        cx_Oracle.init_oracle_client(lib_dir=r"/home/alfiya-anware/opt/Oracle/instantclient_23_4")
        dsn_tns = cx_Oracle.makedsn(hostname, port, service_name=service_name)
        conn = cx_Oracle.connect(user=username, password=password, dsn=dsn_tns)
        print("Connection successful!")
        return conn
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(f"Error connecting to the database: {error.message}")
        return None

def convert_to_serializable(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, cx_Oracle.LOB):
        return obj.read()
    return obj

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, cx_Oracle.LOB):
            return obj.read()
        return super(CustomEncoder, self).default(obj)

def get_table_columns(cursor, table_name):
    query = f"""
    SELECT column_name, data_type, data_precision, nullable
    FROM all_tab_columns
    WHERE table_name = '{table_name.upper()}'
    """
    cursor.execute(query)
    columns = []
    rows=cursor.fetchall()
    for row in rows:
        fld_name=row[0]
        fld_desc_query = f"""
            select LABEL_LONG from CI_MD_FLD_L where FLD_NAME = '{fld_name}'
            """
        cursor.execute(fld_desc_query)
        row1=cursor.fetchall()
        lookup_fld_query = f"""
            select FIELD_VALUE from CI_LOOKUP_VAL where FIELD_NAME = '{fld_name}'
            """
        cursor.execute(lookup_fld_query)
        row2=cursor.fetchall()
        columns.append({
            "name": fld_name,
            "type": row[1],
            "description": row1[0][0].strip(),
            "precision": row[2],
            "nullable": row[3] == 'Y',
            "values": row2
        })
    return columns

def get_foreign_keys(cursor, table_name):
    query = f"""
    select CONST_ID, TBL_NAME, REF_CONST_ID from CI_MD_CONST where TBL_NAME = '{table_name.upper()}' AND CONST_TYPE_FLG='FK'
    """
    cursor.execute(query)
    foreign_keys = []

    rows=cursor.fetchall()

    for row in rows:
        ref_const_id=row[2]
        ftable_query = f"""
            select TBL_NAME from CI_MD_CONST where CONST_ID = '{ref_const_id}'
            """
        cursor.execute(ftable_query)
        row1=cursor.fetchall()
        # print(row1)

        const_id=row[0]
        field_query = f"""
            select FLD_NAME from CI_MD_CONST_FLD where CONST_ID = '{const_id}'
            """
        cursor.execute(field_query)
        row2=cursor.fetchall()

        foreign_keys.append({
            "column": row2[0][0].strip(),
            "references": {
                "table": (row1[0][0]).strip(),
                "column": ref_const_id
            }
        })
    return foreign_keys

def get_primary_key(cursor, table_name):
    query = f"""
    select CONST_ID from CI_MD_CONST where TBL_NAME = '{table_name.upper()}' AND CONST_TYPE_FLG='PK'
    """
    cursor.execute(query)
    row = cursor.fetchone()
    
    if not row:
        return []
    
    const_id = row[0]
    
    # Query to find the primary key fields based on the constraint ID
    field_query = f"""
    SELECT FLD_NAME 
    FROM CI_MD_CONST_FLD 
    WHERE CONST_ID = '{const_id}'
    """
    cursor.execute(field_query)
    rows = cursor.fetchall()
    
    # Extract the field names from the query result
    primary_keys = [r[0].strip() for r in rows]
    
    return primary_keys

def get_table_desc(cursor, table_name):
    query = f"""
    select DESCR, DESCRLONG from CI_MD_TBL_L where TBL_NAME = '{table_name.upper()}'
    """
    cursor.execute(query)
    row = cursor.fetchone()
    
    if not row:
        return []
    
    desc = row[0] + row[1]
    
    return desc

def generate_schema(cursor, table_names):
    schema = []
    for table_name in table_names:
        desc = get_table_desc(cursor, table_name)
        columns = get_table_columns(cursor, table_name)
        foreign_keys = get_foreign_keys(cursor, table_name)
        primary_keys = get_primary_key(cursor, table_name)
    
        
        schema.append({
            "name": table_name,
            "columns": columns,
            "description": desc,
            "foreignKeys": foreign_keys,
            "primaryKeys": primary_keys
        })
    return schema

def fetch_data(cursor, table_name, maint_obj_cd=None, tbl_name=None):
    where_clause = ""
    if maint_obj_cd:
        where_clause = f"WHERE MAINT_OBJ_CD = '{maint_obj_cd}'"
    elif tbl_name:
        where_clause = f"WHERE TBL_NAME = '{tbl_name}'"
    
    if where_clause:
        query = f"SELECT * FROM {table_name} {where_clause} AND ROWNUM <= 50"
    else:
        query = f"SELECT * FROM {table_name} WHERE ROWNUM <= 50"

    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
    data = []
    for row in rows:
        row_data = {}
        for col_name, col_value in zip(columns, row):
            if isinstance(col_value, cx_Oracle.LOB):
                row_data[col_name] = col_value.read()
            else:
                row_data[col_name] = col_value
        data.append(row_data)
    return data



def generate_text_description(schema, table_data=None, parent=None):
    
    descriptions = []
    
    description = "\n---------------------------------------------------------------------------\n\n"
    for table in schema:
        table_name = table['name']
        num_columns = len(table['columns'])
        foreign_keys = table['foreignKeys']
        prim_keys = table['primaryKeys']
        desc=table['description']

        num_foreign_keys = len(foreign_keys)
        # print(prim_keys)

        description += "\n--------------------------------------------------------------------------\n\n"
        
        description += f"Table '{table_name}' is used for storing {desc.strip()}. "
        description += f"Table '{table_name}' has"
        description += f" {num_columns} fields (columns) which are: "

        fld_descr=""
        c=1
        for column in table['columns']:
            description += f" {c}. '{column['name']}'"   
            fld_descr+=f"\n  {c}. '{column['name']}' ({column['type']}):- field name for {column['description']},  'precision': {column['precision']}, 'nullable': {column['nullable']}"
            if column['values']:
                fld_descr+=f", 'values': {', '.join(item[0] for item in column['values'])}"
        
            c+=1
        
        num_prim_keys=len(prim_keys)

        if num_prim_keys==1:
            description += f". Out of these fields, only one is a primary key; '{prim_keys[0]}' is the primary key for '{table_name}'"
        elif num_prim_keys>0:
            k=1
            description += f". Out of these fields, {num_prim_keys} are primary keys. The composite primary keys are: "
            for key in prim_keys:
                description += f" {k}. '{key}' "   
                k+=1

        if num_foreign_keys==1:
            description += f". \nTable '{table_name}' has only one foreign key; "
            description += f"'{foreign_keys[0]['column']}' is a foreign key from table '{foreign_keys[0]['references']['table']}'."
        elif num_foreign_keys > 1:
            description += f". \nTable '{table_name}' has {num_foreign_keys} foreign keys as listed: "
            # description += f"Foreign Keys:\n"
            counter=num_foreign_keys
            for fk in foreign_keys:
                if counter>1:
                    description += f" '{fk['column']}' is foreign key from table '{fk['references']['table']}',"
                elif counter==1:
                    description += f" and '{fk['column']}' is foreign key from table '{fk['references']['table']}'."
                counter-=1
        if parent!=None:
            description += f"\n'{table_name}' is a child table of '{parent}' table."
        else:
            description += f"\n'{table_name}' is a Primary Table."
    

        # description += f"\nData:\n"
        # if table_name in table_data:
        #     for row in table_data[table_name]:
        #         description += "  "
        #         for key, value in row.items():
        #             description += f"{key}: {value}, "
        #         description += "\n"
        description+=f"""

Field Descriptions for table '{table_name}':
"""
        description+=fld_descr
    
        
        descriptions.append(description)
        description=""
    
    return "\n".join(descriptions)


def save_text(filename, descriptions):
    with open(filename, "w") as f:
        for description in descriptions:
            f.write(description)

def main():
    load_dotenv()

    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    hostname = os.getenv('DB_HOSTNAME')
    port = os.getenv('DB_PORT')
    service_name = os.getenv('DB_SERVICE_NAME')

    print(f"Connecting to {hostname}:{port}/{service_name} with user {username}")
    
    conn = connect_to_db(username, password, hostname, port, service_name)
    cursor = conn.cursor()

    # maint_obj_cd_values = ['BILL CYCLE', 'MAIN OBJ', 'PREM TYPE', 'PHONE TYPE', 'CURR CODE', 'CUST CNT TYP', 'COUNTRY', 'CHAR TYPE', 'PER REL TYPE']
    # maint_obj_cd_values = ['ID TYPE', 'ACCT REL TYP', 'TIME ZONE', 'LANGUAGE', 'UOM', 'SQI', 'GEO TYPE']
    # maint_obj_cd_values = ['WORK CAL', 'GL CALENDAR', 'W1-ACTCAL', 'LOOKUP', 'CIS DIVISION', 'GL DIVISION', 'DEBT CLASS']
    # maint_obj_cd_values = ['BILL FACTOR', 'TO DO ROLE', 'TO DO TYPE', 'USER GROUP', 'DATA ACCESS', 'ACCT GROUP', 'TENDER SRC', 'TENDER TYPE', 'TOS TYPE']
    maint_obj_cd_values = ['F1-USRGRP-SC', 'C1-CALC-R-EL', 'C1-CALC-RULE', 'USER-SC']

    descriptions=""

    for m_o_val in maint_obj_cd_values:
        child_tbl_names=[]
        rows = fetch_data(cursor, "CI_MD_MO_TBL", maint_obj_cd=m_o_val)
        for row in rows:
            if row['TBL_ROLE_FLG']=='PRIM':
                primary_table = row['TBL_NAME'].strip()
                print("Primary table:", primary_table)
            else:
                child_tbl_names.append(row['TBL_NAME'].strip())
        print(f"Child tables where mo_val={m_o_val}", child_tbl_names)
        # table_names+=child_tbl_names

        
        schema = generate_schema(cursor, [primary_table])
        descriptions+=generate_text_description(schema)
        
        descriptions+=f"\n\nThe child tables of '{primary_table}' are {child_tbl_names}. \n(Generated when 'MAINT_OBJ_CD'={m_o_val})\n"

        schema = generate_schema(cursor, child_tbl_names)
        descriptions+=generate_text_description(schema, parent=primary_table)
    

    save_text("schema_description4.txt", descriptions)
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()


    