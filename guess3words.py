from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import urllib.request
import csv
import json
import random
import pandas as pd
import time 
import re
import functools  
import time  


  


# disable image load
option = webdriver.ChromeOptions()
chrome_prefs = {}
option.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=option)
# driver.maximize_window()
#######some sites if the size of window not big enought the button not reachable
#driver.set_window_size(250,600)

url = "https://www.laughteronlineuniversity.com/three-word-quotes/"

data = []


# try to open chrome driver and extract information from website
try:
        
# /html/body/div[1]/div/main/div/section/article/div[1]/ol
# /html/body/div[1]/div/main/div/section/article/div[1]/ol/li/ol
# //*[@id="post-3633"]/div[1]/ol/li/ol
# *[@id="post-3633"]/div[1]/ol/li/ol

        counter = 1
        driver.get(url)
        fields_container = driver.find_element(By.XPATH, "//*[@id='post-3633']/div[1]/ol/li/ol")
        elements = fields_container.find_elements(By.TAG_NAME, "li")
        for elem in elements:
            # check print
            print(elem)
            if counter == 120:
                    break
            else:
                x = elem.text
                data.append(x)
                counter += 1
                # check print
                print("append to data: ", x)
except:
        print("checkpoint exception unable to retrieve data, default data will be upload")
        data = [ 'Remember to Live', 'Reward high performance', 'Seize the day', 'Set clear targets', 'Sexy is confidence', 'Share the wealth', 'Share your vision', 'Speak the truth', 'Success is yours', 'Teamwork dream work', 'This will pass', 'Time heals everything', 'Track all progress', 'Train your team', 'Trust the process', 'Value your time']
        pass


# closes the chrome driver
driver.close() 

# check print
print(data)

#foo cleans the text from non alphabet characters in words
def clean_text(text):
    cleaned_words = []
    for sentence in text:
        # extract individual words
        words = re.findall(r'\b\w+\b', sentence.lower()) 
        cleaned_words.append(words)
    return cleaned_words


cleaned_list = clean_text(data)
cleaned_list = cleaned_list

# check print
print(cleaned_list)

 

# chooses random 3 words from list
ran = random.randint(0,(len(cleaned_list)-1))
w = cleaned_list[ran]

# mirror empty list for game
x = []
for i in w:
      temp = ["_" * len(i)]
      x.append(temp)

# check print
print(w,x)
print("#"*25) 


# foo checks if letter in words
def check_if_letter_in(words, x, letter, points, letters_in):
      if letter in letters_in:
            print("you alredy enter the letter enter another letter")
            arr1 = [x,points, letters_in]
            return arr1
      temp = len(letters_in)
      flag = 0
      k = 0
      wx = ""
      x = x
      [letters_in.append(letter) for i in words if letter in i and letter not in letters_in]
      if temp < len(letters_in):
            flag = 1
      for i in words:
            for j in range(len(i)):
                  if  i[j] in letters_in:
                        wx += i[j]
                  else:
                     wx += "_"
                     continue
            x[k] = wx
            k += 1
            wx = ""
            
      if flag == 0:
        print(f'the letter you enter {letter} in not in the words')
        points -= 1
        arr1 = [x, points, letters_in]
        return arr1
      else:
            points += 5
            print("you hit with tha letter: ", letter)
            arr1 = [x,points, letters_in]
            return arr1


# starts variables for game
points = 0
letters_in = []

# flag 4 timer
flag = 0

# runs the game loop, change to foo in next version
while True:
      
      #timer blox
      if flag == 0:
        print("you have 30 seconds for 100 ponit bonus")
        # time save time at the start of the game
        t1 = time.time()
        flag = 1
      else:
           t2 = 30 - (time.time() - t1)
           if t2 > 0:
                print(f'{t2} seconds remaining for 100 bonus')

      # check print
      print(w,x,letters_in,points)
      
      letter = input("please enter letter: ")
      
      # check if letter input
      if letter.isalpha():
            
            #lowercase all letter if needed
            letter = letter.lower()

            # check if letter func
            foo_list = check_if_letter_in(w, x, letter, points, letters_in)
            #check print
            print("check func return: , ", foo_list)

            # update variables, new updates from check letter function
            x = foo_list[0]
            points = foo_list[1]
            letters_in = foo_list[2]
            
            # check if guess all words
            if x == w:
                  t2 = time.time() - t1 
                  if t2 <= 30.99:
                       points += 100
                       print("nice you hit the words in less than 30 seconds you get 100 point bonus")
                  print("nice you guess the words your score is: ", points)
                  break
            else:
                  continue
      #condition else if not a letter is not input and continue to the top
      else:
            print("please enter letter only")
            continue
      