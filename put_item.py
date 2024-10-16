import boto3
import os
import logging
from dotenv import load_dotenv
load_dotenv()

# setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# set up credentials
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
REGION = os.environ.get('REGION')
TABLE_NAME = os.environ.get('TABLE_NAME')

# setup client
dynamodb = boto3.client("dynamodb",
                             aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                             region_name= REGION)



# Put item in table
user = dynamodb.put_item(
     TableName = TABLE_NAME,
     Item={
        'Roll No.': {'S': 'F20BB116'}, 
        'Batch': {'N': '2020'},         
        'Name': {'S': 'Junaid Farooq'},
        'Section': {'S': 'Afternoon B'},
        'Specialization': {'S': 'IT'},
        'Subjects': {'L': [            
            {'S': 'DCCN'}, {'S': 'IP'}, {'S': 'DSA'}, {'S': 'OOAD'}
        ]}
    }
)