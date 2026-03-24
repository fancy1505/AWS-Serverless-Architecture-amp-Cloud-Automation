import json
import boto3

comprehend = boto3.client('comprehend')

def lambda_handler(event, context):
    try:
        # 1. Extract review text
        review = event.get('review', '')
        
        if not review:
            return {
                'statusCode': 400,
                'body': 'No review text provided'
            }

        # 2. Call Amazon Comprehend
        response = comprehend.detect_sentiment(
            Text=review,
            LanguageCode='en'
        )

        sentiment = response['Sentiment']
        confidence = response['SentimentScore']

        # 3. Log result
        print(f"Review: {review}")
        print(f"Sentiment: {sentiment}")
        print(f"Confidence Scores: {confidence}")

        # 4. Return response
        return {
            'statusCode': 200,
            'body': {
                'review': review,
                'sentiment': sentiment,
                'confidence': confidence
            }
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': str(e)
        }
