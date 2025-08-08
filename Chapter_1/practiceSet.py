#1st qns
# print(''' Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
# like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
# When the blazing sun is set, and the grass with dew is wet. Then you show your little
# light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
# are.
# Then the traveler in the dark thanks you for your tiny spark. How could he see where to
# go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
# As your bright and tiny spark lights the traveler in the dark, though I know not what you
# are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are. ''')

#2nd qns   install the exrternal module - pyttsx3

# import pyttsx3
# engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# engine.say("I will speak this text")
# engine.runAndWait()


# 3rd qns

import os

# Select the directory that you want to list 
directory_path = '/'

# Use the os module to list the directory contents 
contents = os.listdir(directory_path)

# Print the contents of the directory
for item in contents:
    print(item)