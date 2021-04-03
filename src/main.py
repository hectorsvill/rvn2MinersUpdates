# main.py
# by: @hectorsvill

import requests
import smtplib


class Accouont:
    def __init__(self, jsoon_data):
        self.json_data = jsoon_data
        self.hnumreward24 = jsoon_data['24hnumreward']
        self.hreward24 = json_data['24hreward']
        self.workers = jsoon_data['workers']
        self.worker_keys = self.workers.keys()
        self.miner = self.workers['stoicminer0']

    def showMinerStatus(self):
        miner = account.miner
        miner_stats = f"name: {'stoicminer0'}\n" \
                      f"offline: {miner['offline']}\n" \
                      f"Last Beat: {miner['lastBeat']}\n" \
                      f"Current Hash Rate: {miner['hr']}\n" \
                      f"Average Hash Rate: {miner['hr2']}"

        print(miner_stats)

baseUrl = "https://rvn.2miners.com/api/accounts/"
accountId = "RFDLFJhd7W1h4AUTxsQu7XY7DQHALvPmJu"
url = baseUrl + accountId

def fetch2MinersJsonData(accouont):
    response = requests.get(url)
    if response.status_code != 200:
        print("error with response. ")
    json_data = response.json()
    return json_data


def sendEmail():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
    except:
        print('error with email. ')

if __name__ == '__main__':
    json_data = fetch2MinersJsonData(accouont=accountId)
    account = Accouont(jsoon_data=json_data)
    account.showMinerStatus()
