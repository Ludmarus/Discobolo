$ pip install tweepy
-
import tweepy

auth = tweepy.OAuthHandler("YOU_CONSUMER_KEY", "YOUR_CONSUMER_SECRET")
auth.set_access_token("YOUR_ACCESS_TOKEN", "YOUR_ACCESS_SECRET")
api = tweepy.API(auth)

# Tweet something
tweet = api.update_status("My first tweet!")

# Like the tweet you just made
api.create_favorite(tweet.id)
rs = ResultStream(rule_payload=rule,
                  max_results=500,
                  max_pages=1,
                  **premium_search_args)

print(rs)

{
  "data": [
    {
      "conversation_id": "1304102743196356610",
      "id": "1307025659294674945",
      "possibly_sensitive": false,
      "public_metrics": {
        "retweet_count": 11,
        "reply_count": 2,
        "like_count": 70,
        "quote_count": 1
      },
      "entities": {
        "urls": [
          {
            "start": 74,
            "end": 97,
            "url": "https://t.co/oeF3ZHeKQQ",
            "expanded_url": "https://dev.to/twitterdev/understanding-the-new-tweet-payload-in-the-twitter-api-v2-1fg5",
            "display_url": "dev.to/twitterdev/und…",
            "images": [
              {
                "url": "https://pbs.twimg.com/news_img/1317156296982867969/2uLfv-Bh?format=jpg&name=orig",
                "width": 1128,
                "height": 600
              },
              {
                "url": "https://pbs.twimg.com/news_img/1317156296982867969/2uLfv-Bh?format=jpg&name=150x150",
                "width": 150,
                "height": 150
              }
            ],
            "status": 200,
            "title": "Understanding the new Tweet payload in the Twitter API v2",
            "description": "Twitter recently announced the new Twitter API v2, rebuilt from the ground up to deliver new features...",
            "unwound_url": "https://dev.to/twitterdev/understanding-the-new-tweet-payload-in-the-twitter-api-v2-1fg5"
          }
        ]
      },
      "text": "Here’s an article that highlights the updates in the new Tweet payload v2 https://t.co/oeF3ZHeKQQ",
      "in_reply_to_user_id": "2244994945",
      "created_at": "2020-09-18T18:36:15.000Z",
      "author_id": "2244994945",
      "referenced_tweets": [
        {
          "type": "replied_to",
          "id": "1304102743196356610"
        }
      ],
      "lang": "en",
      "source": "Twitter Web App"
    }
  ],
  "includes": {
    "users": [
      {
        "created_at": "2013-12-14T04:35:55.000Z",
        "profile_image_url": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",
        "entities": {
          "url": {
            "urls": [
              {
                "start": 0,
                "end": 23,
                "url": "https://t.co/3ZX3TNiZCY",
                "expanded_url": "https://developer.twitter.com/en/community",
                "display_url": "developer.twitter.com/en/community"
              }
            ]
          },
          "description": {
            "hashtags": [
              {
                "start": 17,
                "end": 28,
                "tag": "TwitterDev"
              },
              {
                "start": 105,
                "end": 116,
                "tag": "TwitterAPI"
              }
            ]
          }
        },
        "id": "2244994945",
        "verified": true,
        "location": "127.0.0.1",
        "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
        "pinned_tweet_id": "1293593516040269825",
        "username": "TwitterDev",
        "public_metrics": {
          "followers_count": 513961,
          "following_count": 2039,
          "tweet_count": 3635,
          "listed_count": 1672
        },
        "name": "Twitter Dev",
        "url": "https://t.co/3ZX3TNiZCY",
        "protected": false
      }
    ],
    "tweets": [
      {
        "conversation_id": "1304102743196356610",
        "id": "1304102743196356610",
        "possibly_sensitive": false,
        "public_metrics": {
          "retweet_count": 31,
          "reply_count": 12,
          "like_count": 104,
          "quote_count": 4
        },
        "entities": {
          "mentions": [
            {
              "start": 146,
              "end": 158,
              "username": "suhemparack"
            }
          ],
          "urls": [
            {
              "start": 237,
              "end": 260,
              "url": "https://t.co/CjneyMpgCq",
              "expanded_url": "https://twitter.com/TwitterDev/status/1304102743196356610/video/1",
              "display_url": "pic.twitter.com/CjneyMpgCq"
            }
          ],
          "hashtags": [
            {
              "start": 8,
              "end": 19,
              "tag": "TwitterAPI"
            }
          ]
        },
        "attachments": {
          "media_keys": [
            "13_1303848070984024065"
          ]
        },
        "text": "The new #TwitterAPI includes some improvements to the Tweet payload. You’re probably wondering — what are the main differences? 🧐\n\nIn this video, @SuhemParack compares the v1.1 Tweet payload with what you’ll find using our v2 endpoints. https://t.co/CjneyMpgCq",
        "created_at": "2020-09-10T17:01:37.000Z",
        "author_id": "2244994945",
        "lang": "en",
        "source": "Twitter Media Studio"
      }
    ]
  }
}
