import json

def lambda_handler(event, context):
    print("Event Data -> ",event)
    print("Trigger received")
    

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Testing for S3 Event notification completed ! !')
    }
