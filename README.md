# maconAndTiftonBot

`maconAndTiftonBot` is a Twitter bot for AWS Lambda. See more about Macon and Tifton [here](https://twitter.com/maconandtifton).

The Lambda function in this project will search for tweets in a DynamoDB table, and post them if they have not already been posted. You can use Amazon EventBridge to automate the execution of the Lambda function.

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
* Create a Lambda function in the AWS Management Console.
* Clone this repository.
* Initialize a virtual environment and install the dependencies using `requirements.txt`
* Create a Lambda deployment .zip file from this project directory.
* Upload your deployment to the Lambda function you created.
* Configure an Amazon EventBridge Rule to execute the Lambda function once per day.
