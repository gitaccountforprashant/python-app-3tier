'''
customhost = "employee.coghw13fheqo.us-east-2.rds.amazonaws.com"
customuser = "intellipaat"
custompass = "intellipaat123"
customdb = "employee"
custombucket = "addemployee"
customregion = "us-east-2"
'''
import os

customhost = os.environ["DB_HOST"]
customuser = os.environ["DB_USER"]
custompass = os.environ["DB_PASS"]
customdb =  os.environ["DB_NAME"]
custombucket = os.environ["AWS_S3_BUCKET"]
customregion = os.environ["AWS_REGION"]
