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

def form_status(value):
    ''' Will form a status to post and return it '''
    
    card = chandle.get_name(value)
    description = chandle.get_description(value)
    
    status = f'''{card} ~ {description}'''
    
    return status

def post_status(value):
    ''' Take input value and post status '''
    
    media = chandle.get_image(value) # Find the card's image
    s = form_status(value) # Create the status for card
    
    api.update_with_media(media, status=s) # Post to twitter
    
    return
# The bot needs to watch for mentions and then parse the text for commands
# Bot will then call on relevant value_functions and card_handler stuff and reply
# Perhaps look in to asyc/await
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        
        print('Mention seen on {} at {}'.format(vf.date(), vf.time()))
        print(f'"{status.text}"')
        
        if 'random card' in status.text:
            
            card_num = vf.random_value()
            try:
                print(post_status(card_num))
            except:
                print("Error occurred: sys.exc_info()[0]")
                pass


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track = ['@PoastThe', '@poastthe'])