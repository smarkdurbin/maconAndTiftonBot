# maconAndTiftonBot

`maconAndTiftonBot` is a Twitter bot for AWS Lambda. See more about Macon and Tifton [here](https://twitter.com/maconandtifton).

## Requirements

* Twitter Developer Account
* AWS Account

## AWS Services Used

* AWS Lambda 
* Amazon DynamoDB 
* AWS Systems Manager

## Setup Your Own Twitter Bot
* Create a DynamoDB table called `maconAndTiftonTweets` (if you change this, change table name in the lambda_handler as well). Create a single hash key called `content`.
* Input your Twitter credentials into Systems Manager Parameter Store.
    * `twitter_api_key`
    * `twitter_api_secret`
    * `twitter_access_token`
    * `twitter_access_secret`
* Create a Lambda function.
* 
