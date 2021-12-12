# A simple bot written by u/ProbablyNotLime
import thefuzz.fuzz as fuzz
from thefuzz import *
import praw

# Set up reddit variables
client_id = "hidden"
client_secret = "hidden"
username = "WalterKosterBot"
password = "hidden"
user_agent = "<console:WalterKoster:GENTLEMAN:1.0>"
comment_text = "..., a short view back to the past. Thirty years ago, Niki Lauda told us ‘take a monkey, place him into the cockpit and he is able to drive the car.’ Thirty years later, Sebastian told us ‘I had to start my car like a computer, it’s very complicated.’ And Nico Rosberg said that during the race – I don’t remember what race –  he pressed the wrong button on the wheel. Question for you both: is Formula One driving today too complicated with twenty and more buttons on the wheel, are you too much under effort, under pressure? What are your wishes for the future concerning the technical programme during the race? Less buttons, more? Or less and more communication with your engineers?"
trigger_word = ["gentlemen", "gentleman"]

# Main Loop
while True:
    
    # Login
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         username=username,
                         password=password,
                         user_agent=user_agent)

    # Set up the subreddit
    subreddit = reddit.subreddit("formuladank")
    
    print("In work...")

    # Check for comments
    try:
        for comment in subreddit.stream.comments(skip_existing=True):
            print(comment.body)
            for item in trigger_word:
                if fuzz.ratio(comment.body.lower(), item) == 100:
                    comment.reply(comment_text)
                    print ("Succesfully replied")
                    break
    # Exit
    except KeyboardInterrupt:
        print("Shuting down...")
        break
    
    # Error handling
    except Exception as error:
        print(f"Error: {error}")
        print("Trying to restart...")