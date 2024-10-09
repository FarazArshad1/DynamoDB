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
dynamodb = boto3.resource("dynamodb",
                             aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                             region_name= REGION)

table = dynamodb.Table(TABLE_NAME)


user = table.get_item(
    Key = { 
        "Roll No." : 'F20BB125',
        "Batch" : 2020 
    }
)

# DynamoDb give the Item along with Metadata, But we only want Item data. So we'll filter out
print(user.get("Item"))