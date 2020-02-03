# TarotGen

## A bot that will post 78-156 statuses. Each status will be a random choice of a tarot card.

The status will consist of 3 elements:
    1. The card name.
    2. An image of the card.
    3. A description of the card.
    4. Up to 3 keywords associated with the card. *Optional*

Each card can have a reversed state, each reversal has a different meaning, figure out how to handle this somewhat elegantly.
Format for reversal is "rX" where X is the card number.

## To do
- [x] Set up Tweepy (or whatever Twitter lib)
- [x] Create template for twitter status.
- [x] Create function for getting associated image.
- [x] Create function to clear all or x posts.
- [x] Create function to log previous picks.
- [x] Create function to match generated choice to previous choices.
- [x] Create function to match generate value to a card.
- [] Set up JSON file for cards: 
- [x] JSON Value : Name
- [x] JSON Value : Image path
- [x] JSON Value : Upright Description
- [] JSON Value : Reversal description
- [] JSON Value : Keyword
- [x] Set up Logging
- [x] Set up random card choice
- [x] Set up a system for finding relevant card items:
- [x] Image 
- [x] Upright description
- [x] Reversal description
