import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")

# Create API object
api = tweepy.API(auth)

# Define the user you want to check
username = 'your_twitter_username'

# Get followers and following
followers = api.followers_ids(username)
friends = api.friends_ids(username)

# Find who you are following but who aren't following you back
not_following_back = [user for user in friends if user not in followers]

# Print these users
for user in not_following_back:
    print(user)
