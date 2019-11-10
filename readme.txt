# TarotGen

A bot that will post 78-156 statuses. Each status will be a random choice of a tarot card.

The status will consist of 3 elements:
    1. The card name.
    2. An image of the card.
    3. A description of the card.
    4. Up to 3 keywords associated with the card. *Optional*

Each card can have a reversed state, each reversal has a different meaning, figure out how to handle this somewhat elegantly.
Format for reversal is "rX" where X is the card number.

It has become apparent that this should be split into multiple files.
    - Twitter handler
    - Number handler
    - Tarot association handler

TODO:
    * [x] Set up Tweepy (or whatever Twitter lib)
    * [*] Create template for twitter status.
    * [*] Create function for getting associated image.
    * [*] Create function to clear all or x posts.
    * [*] Create function to log previous picks.
    * [*] Create function to match generated choice to previous choices.
    * [*] Create function to match generate value to a card.
    * [] Set up JSON file for cards: 
        [*] Value : Name
        [*] Value : Image path
        [*] Value : Upright Description
        [] Value : Reversal description
        [] Keyword value : Keyword
    * [*] Set up Logging
    * [*] Set up random card choice
    * [*] Set up a system for finding relevant card items:
        [*] Image 
        [*] Upright description
        [*] Reversal description
    