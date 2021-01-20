# TweetsSentimentAnalysis

## Description

This project refers to problem of analysing sentiment about some topics discussed on the internet. Main data source and best suitable social media is Twitter - place where chatting is everything. Given such comprehensive source of data we can model the process of sentiment extraction given many various intents. Please remark that analyzed tweets are going to be in polish.

## Program flow

The diagram presents the application flow structure.

![](documentation/resources/block_schema.png)

Interpretation:

- Firstly we obtain a batch of tweets out of Twitter API. We most probably want to get tweets from a specific time interval. It optimises the use of database service, since no redundant attempts to add existing data.
- In this step we make some of preprocessing for example look for keywords, specific expressions in polish or words with the most sentiment value.
- Next step is text analytics. At this time we make use of Azure Services where text get translated to english and then sentiment is being measured.
- After receiving response, output data will be processed and combined with input tweet. In the end data is going to be added to database with all main extracted features
- Finally reports will be created in PowerApps. With use of Azure Functions we can get all the changes made to database or sum up any information from given time interval. Use of PowerApps shortens development of UI leaving user with decent experience.

## Azure architecture

![](documentation/resources/azure_schemat.png)

## Data sources

Information about Tweet's hashtags we can find in "entities" JSON field.
API v1.1 provide searching by hashtags.

Subscriptions: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/overview

![](documentation/resources/subscriptions.png)

How to build a standard query: https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/guides/build-standard-queries

![](documentation/resources/hashtag_search.png)

To build back-end application, we can use Azure FunctionApps or Azure container with custom server environment.

We get Tweets data from Twitter API in JSON object. In next step, the response must be processed to get data like Tweet Id, Tweet text, hashtags, author ect.
After that, the Tweets content will be sent to sentiment analysis. The response and Tweets data will be sent to database.


## Text Analytics Azure Services
After getting data as JSONs, we can send them to sentiment analysis by Text Analytics Azure Services.
Azure offers sentiment analysis  which provides API for detecting negative and positive sentiments. 
AI models are provided by service, so we need just to send content to analysis. There are 3 labels: positive, negative and neutral. 
If there is at least one negative sentence and at least positive sentence, API will return mixed sentence: 

![alt text](https://github.com/kielczykowski/TweetsSentimentAnalysis/blob/twitter/docs/documentation/resources/sentence_analysis.png)

Buliding an example query with some tweet text: 
```
{
  "documents": [
    {
      "language": "en",
      "id": "1",
      "text": "Congratulations SpaceX Team!"
    }
  ]
}
```
Analysis is performed upon receipt of the request. There is an limit of number of requests per second for each payment tier. Text analytics API is stateless, so no data is stored on Azure accound, so there is a need to store collected data from Azure text API.
## Data storage

We would want to storage all data from specific tweets and the score of our sentiment analysis. Beacasue tweets are recived in JSON we were thinkig of using NoSQL database. Azure provides two types of NoSQL database services: MongoDB Atlas and Cosmos DB. We decided to use Cosmos DB because it is more universal and gives many usefull options of using DB. Moreover it is designed to directly connect with PowerApps and MongoDB Atlas is not.

## PowerApps reporting

We decided to created reports in PowerApps because:

- it is easy to configure without writing a lot of code
- integration with Azure Functions; they enable timer, data processing and web enpoint for service like solutions
- has out of the box integration with Twitter and MS applications (can come in handy at some point)
- easily expandable
