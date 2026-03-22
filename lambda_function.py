import boto3
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch')
sns = boto3.client('sns')

 
ELB_NAME = "arn:aws:elasticloadbalancing:ap-south-1:324583653988:loadbalancer/app/elb-test/8ea69159b94f7c81"
SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:324583653988:elb-error-alert-topic"
THRESHOLD = 10

def lambda_handler(event, context):
    try:
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(minutes=5)

        # 1. Get ELB 5xx metrics
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/ApplicationELB',
            MetricName='HTTPCode_ELB_5XX_Count',
            Dimensions=[
                {
                    'Name': 'LoadBalancer',
                    'Value': ELB_NAME
                }
            ],
            StartTime=start_time,
            EndTime=end_time,
            Period=300,
            Statistics=['Sum']
        )

        datapoints = response['Datapoints']

        if not datapoints:
            print("No data found")
            return

        error_count = datapoints[0]['Sum']
        print(f"5xx Error Count: {error_count}")

        # 2. Check threshold
        if error_count > THRESHOLD:
            message = f"⚠️ High ELB 5xx Errors detected: {error_count} errors in last 5 minutes"

            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Message=message,
                Subject="ELB 5xx Error Alert"
            )

            print("Alert sent!")
        else:
            print("No issues detected")

    except Exception as e:
        print(f"Error: {str(e)}")