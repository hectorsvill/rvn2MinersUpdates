# main.py
# by: @hectorsvill

import smtplib
import requests


class MailService:
    def __init__(self, gmail_user, gmail_password):
        self.gmail_user = gmail_user
        self.gmail_password = gmail_password

    def send_email(self, mail_to, subject_text, body_text):
        email_text = f"""\
        To: {mail_to}
        Subject: {subject_text}

        {body_text}
        """

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self.gmail_user, self.gmail_password)
            server.sendmail(self.gmail_user, mail_to, email_text)
            server.close()
        except:
            print('error with email.')


class Account:
    def __init__(self, address):
        self.id = address
        self.numreward24h = None
        self.reward24h = None
        self.workers = None
        self.worker_keys = None
        self.miner = None
        self.fetch_stats()

        self.mail_service = None

    def show_miner_status(self):
        miner = account.miner
        miner_stats = f"name: {'stoicminer0'}\n" \
                      f"24hnumreward: {self.numreward24h}\n" \
                      f"24hreward: {self.reward24h}\n" \
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
            self.numreward24h = json_data['24hnumreward']
            self.reward24h = json_data['24hreward']
            self.workers = json_data['workers']
            self.worker_keys = self.workers.keys()
            self.miner = self.workers['stoicminer0']

    def send_email(self, mail_to):
        if self.mail_service is None:
            print("Mail Service is None")
        else:
            subject_text = "rvn 2Miners Update"
            body_text = self.show_miner_status()
            self.mail_service.send_email(mail_to, subject_text, body_text)



if __name__ == '__main__':
    rvn_address = "RFDLFJhd7W1h4AUTxsQu7XY7DQHALvPmJu"
    account = Account(rvn_address)
    my_gmail_user = ""
    my_gmail_password = ""
    send_mail_to = ""

    account.mail_service = MailService(my_gmail_user, my_gmail_password)
    account.send_email(send_mail_to)