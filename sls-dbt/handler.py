import boto3
import os

FARGATE_VPC = os.environ['FARGATE_VPC']
FARGATE_SN1 = os.environ['FARGATE_SN1']
FARGATE_SN2 = os.environ['FARGATE_SN2']
FARGATE_SG = os.environ['FARGATE_SG']
FARGATE_CLUSTER = os.environ['FARGATE_CLUSTER']

def hello(event, context):

    client = boto3.client('ecs')

    response = client.run_task(
        cluster=FARGATE_CLUSTER,
        launchType = 'FARGATE',
        taskDefinition='dbt-fargate:3', # replace with your task definition name and revision
        count = 1,
        platformVersion='LATEST',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    FARGATE_SN1,
                    FARGATE_SN2
                ],
            'assignPublicIp': 'ENABLED'
            }
        }
    )
    print(response)
    return str(response)
