# main.py
# by: @hectorsvill

import requests
import smtplib


class Account:
    def __init__(self, address):
        self.id = address
        self.hnumreward24 = None
        self.hreward24 = None
        self.workers = None
        self.worker_keys = None
        self.miner = None
        self.fetch_stats()

    def show_miner_status(self):
        miner = account.miner
        miner_stats = f"name: {'stoicminer0'}\n" \
                      f"24hnumreward: {self.hnumreward24}\n" \
                      f"24hreward: {self.hreward24}\n" \
                      f"offline: {miner['offline']}\n" \
                      f"Last Beat: {miner['lastBeat']}\n" \
                      f"Current Hash Rate: {miner['hr']}\n" \
                      f"Average Hash Rate: {miner['hr2']}"
        return miner_stats

    def fetch_stats(self):
        base_url = "https://rvn.2miners.com/api/accounts/"
        url = base_url + self.id
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

    def send_email(self, gmail_user, gmail_password, mail_to):
        subject_text = "Raven 2Miner Update - 1 Online"
        body_text = self.show_miner_status()

        email_text = f"""\
        From: {gmail_user}
        To: {mail_to}
        Subject: {subject_text}

        {body_text}
        """

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, mail_to, email_text)
            server.close()
        except:
            print('error with email.')


if __name__ == '__main__':
    rvn_address = "RFDLFJhd7W1h4AUTxsQu7XY7DQHALvPmJu"
    account = Account(rvn_address)
    my_gmail_user = ""
    my_gmail_password = ""
    send_mail_to = ""
    account.send_email(my_gmail_user, my_gmail_password, send_mail_to)
