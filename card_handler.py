# File for where card shit happens and stuff
import json

def get_name(value):
    ''' Matches input value to the name of a card '''
    
    t = open('cards.json')
    tarot = json.load(t)
    
    card_names = [cards[1] for cards in tarot['card_names'].items()]
    
    return card_names[value]

def get_description(value):
    ''' Gets the relevant definition from input value '''
    
    t = open('cards.json')
    tarot = json.load(t)
    
    descriptions = [description[1] for description in tarot['card_descriptions'].items()]
    
    return descriptions[value]

def get_image(value):
    ''' Returns the path of relevant image '''
    t = open('cards.json')
    tarot = json.load(t)
    
    path = [image[1] for image in tarot['card_images'].items()]
    
    return path[value]
