# main.py
# by: @hectorsvill

import requests
import smtplib


class Accouont:
    def __init__(self, accoundId):
        self.accoundId = accoundId
        self.hnumreward24 = None
        self.hreward24 = None
        self.workers = None
        self.worker_keys = None
        self.miner = None
        self.fetchJsonData()

    def showMinerStatus(self):
        miner = account.miner
        miner_stats = f"name: {'stoicminer0'}\n" \
                      f"offline: {miner['offline']}\n" \
                      f"Last Beat: {miner['lastBeat']}\n" \
                      f"Current Hash Rate: {miner['hr']}\n" \
                      f"Average Hash Rate: {miner['hr2']}"
        print(miner_stats)

    def fetchJsonData(self):
        baseUrl = "https://rvn.2miners.com/api/accounts/"
        url = baseUrl + self.accoundId
        response = requests.get(url)
        if response.status_code != 200:
            print("error with response. ")
        else:
            json_data = response.json()
            self.hnumreward24 = json_data['24hnumreward']
            self.hreward24 = json_data['24hreward']
            self.workers = json_data['workers']
            self.worker_keys = self.workers.keys()
            self.miner = self.workers['stoicminer0']

def sendEmail():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
    except:
        print('error with email. ')

if __name__ == '__main__':
    accountId = "RFDLFJhd7W1h4AUTxsQu7XY7DQHALvPmJu"
    account = Accouont(accoundId=accountId)
    account.showMinerStatus()
