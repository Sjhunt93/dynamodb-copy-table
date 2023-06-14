FROM python:3.8-alpine 

WORKDIR /project
COPY copy_db_table.py /project/copy_db_table.py 

RUN python -m pip install boto3 

ENTRYPOINT ["python", "copy_db_table.py"]
