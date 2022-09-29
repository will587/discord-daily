import csv
import requests
from csv import writer
import random
import time

def get_message():
    with open('Phrases.csv') as csvfile:
        readCSV = list(csv.reader(csvfile, delimiter=','))
        phrase = readCSV[random.randrange(0, len(list(csv.reader(open('Phrases.csv')))))]
        print("Sent: " + str(phrase))
        return phrase

def ran(message):
    # The payload will be the message that you wish to say in the server
    payload = {
        'content': message
    }

    header = {
        'authorization': "Mzc5NjI2MzU2NDUyODg0NDgw.GmdKgw.Q7IjHISGtq39_wstRBVfuIxZ-5nenslpX24svU"
    }

    # You can find the channel ID by simply right clicking on the channel you wish to input messages into and
    # pressing "Copy ID"
    r = requests.post("https://discord.com/api/v9/channels/931386327914659901/messages", data=payload, headers=header)


while True:
    ran(get_message())
    time.sleep(random.randint(86400, 86401))