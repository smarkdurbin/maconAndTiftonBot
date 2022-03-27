import boto3
from boto3.dynamodb.conditions import Key, Attr
import csv
import datetime
import tweepy

def lambda_handler(event, context):
    try:
        # Create SSM Client.
        aws_client = boto3.client('ssm')
    
        # Get twitter keys from Parameter Store.
        parameters = aws_client.get_parameters(
            Names=[
                'twitter_api_key',
                'twitter_api_secret',
                'twitter_access_token',
                'twitter_access_secret'
            ],
            WithDecryption=True
        )
    
        # Define dict for twitter keys.
        twitter_keys = {}
        
        # Convert list of parameters into simpler dict.
        for parameter in parameters['Parameters']:
            twitter_keys[parameter['Name']] = parameter['Value']
            
        # Create twitter client.
        twitter_client = tweepy.Client(
            consumer_key=twitter_keys.get('twitter_api_key'),
            consumer_secret=twitter_keys.get('twitter_api_secret'),
            access_token=twitter_keys.get('twitter_access_token'),
            access_token_secret=twitter_keys.get('twitter_access_secret')
        )
        
        # Create DynamoDB resource.
        dynamodb = boto3.resource('dynamodb')
        
        # Define tweets table.
        tweets_table = dynamodb.Table('maconAndTiftonTweets')
        
        # Scan table for unposted tweets.
        unposted_tweets = tweets_table.scan(
            FilterExpression=Attr('posted').not_exists(),
            Limit=1
        )['Items']
        
        # If no unposted tweets
        if not unposted_tweets:
            print("No tweets found to post.")
            
            return
        
        # Define next tweet.
        next_tweet = unposted_tweets[0]
        
        # If tweet created.
        if twitter_client.create_tweet(text=next_tweet['content']):
            # Update posted field in table row with current timestamp.
            tweets_table.update_item(
                Key={
                    'content': next_tweet['content']
                },
                UpdateExpression='SET posted = :val1',
                ExpressionAttributeValues={
                    ':val1': str(datetime.datetime.now())
                }
            )
    
    except Exception as e:
        print(str(e))
    