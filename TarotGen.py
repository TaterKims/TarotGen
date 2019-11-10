# The main file for the bot
# value_functions and card_handler are imported into this

import json, random, tweepy, logging, datetime, time # Does doing this instead of importing per line affect efficiency? 
import value_functions as val_functions
import card_handler as chandle

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="TarotGen.log", encoding='UTF-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Open twitter stuff
j = open('t.json')
k = json.load(j)

# Import twitter stuff
c = k['consumer']
cs = k['consumer_secret']
a = k['access']
acs = k['access_secret']

# TWITTER STUFF
auth = tweepy.OAuthHandler(c, cs)
auth.set_access_token(a, acs)
api = tweepy.API(auth)
print("Authorized!")
print("~~ Welcome to The Tarot Poast! ~~")

# !! Functions, functions, functions !!
def delete_statuses():
    '''  Will delete ALL statuses in user timeline '''
    
    timeline = tweepy.Cursor(api.user_timeline).items()
    
    for status in timeline:
        api.destroy_status(status.id)
        
    return

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

posts = 78 # Bot will post for 78 days at interval of days and then quit
day = 86400 # A day in seconds

while posts >= 0:
    
    value = val_functions.random_value() # Reinit value to a new random value every loop
    
    today = val_functions.date() # Get today
    time = val_functions.time() # Get now
    val_functions.value_log(today, time, value) # Save
    
    # If the generated value isn't in the log...
    if val_functions.compare_previous(value) is False:
        
        # ... Attempt post
        try:
            
            post_status(value)
            print("Status posted!")
            
        except:
            
            print("Error posting!")
            break
    else:
        
        #... Otherwise restart loop and try again
        continue
    
    posts -= 1 # Decrement posts by 1
    time.sleep(day) # Now wait a day before loop starts
    
print("Done posting!iu8")