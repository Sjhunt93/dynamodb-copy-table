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


## Run in docker 

This repository contains a dockerfile for you, to create an image and run the script. 

`docker build . -t copy-dynamo-table:latest`

`docker run -e AWS_DEFAULT_REGION=your-region -e AWS_ACCESS_KEY_ID=your-key -e AWS_SECRET_ACCESS_KEY=your-secret --rm -it copy-dynamo-table:latest src-table dest-table`

Additional you can specify a `-c` argument to enable table creation e.g.
`docker run -e AWS_DEFAULT_REGION=your-region -e AWS_ACCESS_KEY_ID=your-key -e AWS_SECRET_ACCESS_KEY=your-secret --rm -it copy-dynamo-table:latest src-table dest-table -c`