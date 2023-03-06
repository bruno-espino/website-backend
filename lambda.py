import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitCount')
def lambda_handler(event, context):
    response = table.get_item(
    Key={
        'Count':0,
    }
)
    record_count = response['Item']['Counter'] + 1
    
    table.update_item(
    Key={
        'Count': 0,
    },
      ExpressionAttributeNames={
        '#C': 'Counter'
    },
    UpdateExpression='SET #C = :val1',
    ExpressionAttributeValues={
        ':val1': record_count
    }
)
 

    return record_count