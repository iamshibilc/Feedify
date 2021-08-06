import os
import time
import sys
import random
import requests
y = '\033[1;30;43m'
m = '\x1b[1;96m'
u = '\x1b[1;95m'
h = '\x1b[1;97m'
p = '\x1b[1;37m'
k = '\x1b[1;33m'
b = '\x1b[1;34m'
bm = '\x1b[96m'
d = '\033[1;37;40m'
os.system('rm -rf config')
from tqdm import tqdm
from instabot import Bot
import instabot
from bullet import Password
def delay_counter(delay_time):
    while delay_time:
        mins, secs = divmod(delay_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("  NEXT REFRESHING => ",timer, end="\r\u001b[0m")
        time.sleep(1)
        delay_time -= 1

bot = Bot(
    max_likes_per_day=450,
    max_follows_per_day=300,
    max_unfollows_per_day=200,
    max_comments_per_day=100,
    max_messages_per_day=50,
    max_likes_to_like=45,
    min_likes_to_like=0,
    max_followers_to_follow=500,
    min_followers_to_follow=100,
    max_following_to_follow=random.randint(1,100000),
    min_following_to_follow=2,
    min_media_count_to_follow=2,
    like_delay=random.randint(1,15),
    follow_delay=20,
    unfollow_delay=20,
    comment_delay=20,
    message_delay=20,
   filter_users=True,
)

def Banner():
 print("╔═══╦═══╦═══╦═══╗ ╔╗──╔══╦╗╔═╦═══╦═══╗")
 print("║╔══╣╔══╣╔══╩╗╔╗║ ║║──╚╣╠╣║║╔╣╔══╣╔═╗║")
 print("║╚══╣╚══╣╚══╗║║║║ ║║───║║║╚╝╝║╚══╣╚═╝║")
 print("║╔══╣╔══╣╔══╝║║║║ ║║─╔╗║║║╔╗║║╔══╣╔╗╔╝")
 print("║║──║╚══╣╚══╦╝╚╝║ ║╚═╝╠╣╠╣║║╚╣╚══╣║║╚╗")
 print("╚╝──╚═══╩═══╩═══╝ ╚═══╩══╩╝╚═╩═══╩╝╚═╝")
def login():
 os.system('clear')
 print (m)
 Banner()
 variable = requests.get('https://docs.google.com/spreadsheets/d/1Ij4ARxsQAyhlXt0eLnZ8d6MwXxOue5W96Cm3xJP3O90/edit?usp=drivesdk')
 print ('			   ')
 USERNAME = input (h+'[?] Username : \x1b[1;37m')
 if USERNAME in variable.text:
  cli= Password(prompt=h+"[?} Password : ", hidden="•")
  result = cli.launch()
  print ('\033[1;37;40m		   ')
  bot.login(username=USERNAME, password=result, use_cookie=False)
  feedify()
 else:
  print ("\033[36m")
  print ("\033[31m [x] YOUR USERNAME IS NOT IN OUR DATABASE!!")
  print ("\033[31m [x] KINDLY CONTACT OUR ADMINISTRATORS!!")    
  print ("\033[31m [x] CONTACT AS TELEGRAM @SIMZEOVER !!")
  print ("                                      ")     	
def feedify():
 print ('		')
 bot.get_timeline_medias
 bot.like_timeline()
 delay_counter(15)
 feedify()
login()

