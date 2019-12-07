# Currently 2 things to implement;
# [] @bot random card
# [] @bot <card>
import json, tweepy, random, sys
import value_functions as vf
import card_handler as chandle

j = open('t.json')
k = json.load(j)

c = k['consumer']
cs = k['consumer_secret']
a = k['access']
acs = k['access_secret']

auth = tweepy.OAuthHandler(c, cs)
auth.set_access_token(a, acs)
api = tweepy.API(auth)
print("Authorized!")
print("~~ Streamer engaged! ~~")

def post_status(value, user):
    ''' Take input value and post status '''
    
    card = chandle.get_name(value)
    description = chandle.get_description(value)
    
    s = f"@{user} {card} - {description}"
    
    media = chandle.get_image(value) # Find the card's image
    
    api.update_with_media(media, status=s) # Post to twitter
    
    return

# The bot needs to watch for mentions and then parse the text for commands
# Bot will then call on relevant value_functions and card_handler stuff and reply
# Perhaps look in to asyc/await
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        
        print('Mention seen on {} at {}'.format(vf.date(), vf.time()))
        print(f'From: {status.user.screen_name} - "{status.text}"')
        
        if 'random card' in status.text:
            
            card_num = vf.random_value()
            try:
                print(post_status(card_num, status.user.screen_name))
            except:
                print("Error occurred: sys.exc_info()[0]")
                pass


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track = ['@PoastThe', '@poastthe'], is_async=True)