# dynamodb-copy-table
Simple python script for copying a table


## usage

To install requirments (only 1)

`pip3 install boto3`

To copy from one table to another.

`python3 copy_db_table.py <input> <output>`

Same as above but will create a new table

`python3 copy_db_table.py <input> <output> -c`


Inspired by https://github.com/techgaun/dynamodb-copy-table, but updated with boto3.
