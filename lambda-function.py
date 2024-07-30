import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-greeting-serverless-app')
def lambda_handler(event, context):
    response = table.get_item(Key={
        'id':'0'
    })
    view = response['Item']['view']
    view = view + 1
    
    print(view)
    
    response = table.put_item(Item={
        'id':'0',
        'view': view
    })
    
    return view
