import tweepy
from datetime import time, timedelta, timezone, datetime
import time
from threading import Timer
import re
import sys

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    user = api.me()
    print("HELLO %r" % user.name)
    print('TWITTER ACCOUNT %r' % user.screen_name)

    def sched() :
        tweet = input('Enter Your tweet! ')

        print("Enter time after which you want to tweet :")
        user_input = input("Format : DAYS:HOURS:MINUTES:SECONDS  ")
        input_list = user_input.split(':')
        numbers = [int(x.strip()) for x in input_list]
        sec = numbers[0]*86400 + numbers[1]*3600 + numbers[2]*60 + numbers[3]

        def tweeet() :
            display = api.update_status(status=tweet)
            print("You tweeted %r" % tweet)

        def timer():
            Timer(sec, tweeet, ()).start()
        timer()

    def timeline():
        posts = api.home_timeline(tweet_mode='extended',count = 10)
        for post in posts:
            if post.is_quote_status != "false":
                print("Retweeted:")
            else:
                print("Tweeted:")
            id = post.id
            text = post.full_text
            print (text)
    def user():
        posts = api.user_timeline(tweet_mode='extended',count = 10)
        for post in posts:
            if post.is_quote_status != "false":
                print("Retweeted:")
            else:
                print("Tweeted:")
            id = post.id
            text = post.full_text
            print (text)

    def time1():
        tweet = input('Enter Your tweet! ')
        print("Enter time after which you want to delete the tweet :")
        user_input = input("Format : DAYS:HOURS:MINUTES:SECONDS  ")
        input_list = user_input.split(':')
        numbers = [int(x.strip()) for x in input_list]

        sec = numbers[0]*86400 + numbers[1]*3600 + numbers[2]*60 + numbers[3]

        display = api.update_status(status=tweet)
        id = display.id
        print("You tweeted %s" %tweet)

        def delete():
            api.destroy_status(id)
            print('Your Tweet %s is deleted now'%tweet)

        def timer():
            Timer(sec, delete, ()).start()

        timer()

    def search():
        flag = 0
        for status in mytweets:
        	tweet_string = status.text
        	word = sys.argv[1]
        	if re.search(word, tweet_string, re.IGNORECASE):
        		if status.retweeted == True:
        			print('=========\nRetweeted:  ' + tweet_string + '\n=========')
        		else:
        			print('=========\nTweeted:  ' + tweet_string + '\n=========')
        		flag = 1

        if flag == 0:
        	print('Sorry! No tweets found matching your search request!')
    def voiceSave(text,id):
        from gtts import gTTS
        import vlc
        import os
        language = 'en'
        myobj = gTTS(text=text,lang=language,slow=False)
        file = str(id) + ".mp3"
        myobj.save(file)
        os.system("mpg321 " + file)

    def audio():
        posts = api.user_timeline(tweet_mode='extended',count = 10)

        for post in posts:
            if post.is_quote_status != "false":
                print("You retweeted:")
            else:
                print("You tweeted:")
            id = post.id
            text = post.full_text
            voiceSave(text,id)


    while True:
        print("Try following activities on our Twitter CLI : ")
        print("1.GET TIMELINE TWEETS")
        print("2.GET USER TWEETS")
        print("3.SCHEDULE TWEETS")
        print("4.TIME YOUR TWEETS")
        print("5.SORT YOUR TWEETS IN CATEGORIES")
        print("6.LISTEN TO THE AUDIO FILE OF YOUR TIMELINE")
        choice = input(">>> ").lower().rstrip()
        if choice=='1':
            timeline()
        elif choice=='2':
            user()
        elif choice=='3':
            sched()
        elif choice=='4':
            time1()
        elif choice=='5':
            search()
        elif choice=='6':
            audio()
