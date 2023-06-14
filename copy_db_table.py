"""
This software is provided as is! Do whatever you want with it.
"""

import boto3
import sys
import os



def fetch_items(table_object, last_eval=None):
    if last_eval:
        response = table_object.scan(ExclusiveStartKey=last_eval)
    else:
        response = table_object.scan()
    return response["Items"], response.get("LastEvaluatedKey", None)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: %s \n\t <source_table_name> <destination_table_name>\n"% sys.argv[0])
        print("options:")
        print("\t -c \t creates a new table")
        sys.exit(1)

    src_table = sys.argv[1]
    dst_table = sys.argv[2]

    dynamodb = boto3.resource('dynamodb')

    src_table_object = dynamodb.Table(src_table)
    dst_table_object = dynamodb.Table(dst_table)

    print(src_table_object, dst_table_object)

    try: 
        src_table_schema = src_table_object.key_schema
        print(src_table_schema)
    except Exception as e:
        print(e)
        print("Table %s does not exist" % src_table) 
        sys.exit(1)

    if '-c' in sys.argv:
        try: 
            dst_table_object.table_status # basically this will throw an exception
            print("table already exists cannot create new table... exiting!") # if no exception then exit
            sys.exit(1)
        except Exception as e:
            pass
            
        print("Creating new table...")
        dst_table_object = dynamodb.create_table(
            TableName=dst_table,
            KeySchema=src_table_object.key_schema,
            AttributeDefinitions=src_table_object.attribute_definitions,
            BillingMode=src_table_object.billing_mode_summary["BillingMode"]
        )
        
        dst_table_object.wait_until_exists()


    total_items = 0
    last_eval = None
    while True:
        items, last_eval = fetch_items(src_table_object, last_eval=last_eval)
        print(len(items), last_eval)
        for i in items:
            dst_table_object.put_item(Item=i)
            total_items += 1
        if not last_eval:
            break


    print("total items copied: ", total_items)