# main.py
# by: @hectorsvill

import smtplib
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from twilio.rest import Client


class MailService:
    def __init__(self, gmail_user, gmail_password):
        self.gmail_user = gmail_user
        self.gmail_password = gmail_password
        self.mail_to = None

    def send_email(self, subject_text, body_text):
        if self.mail_to is None:
            print("MailService error: mail_to is None")
        else:
            email_text = f"""\
            To: {self.mail_to}
            Subject: {subject_text}
    
            {body_text}
            """

            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(self.gmail_user, self.gmail_password)
                server.sendmail(self.gmail_user, self.mail_to, email_text)
                server.close()
            except:
                print('error with email.')


class TwillioService:
    def __init__(self, account_sid, auth_token, from_number):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number
        self.to_number = None

    def send_sms(self, body_text):
        if self.to_number[0] != "1":
            print("send_sms error: to_number must start with +")
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body=body_text,
            from_=self.from_number,
            to=self.to_number
        )
        print(message.sid)


class Account:
    def __init__(self, address):
        self.id = address
        self.numreward24h = None
        self.reward24h = None
        self.workers = None
        self.miner = None
        self.fetch_stats()
        self.mail_service = None
        self.scheduler = None
        self.twillio_service = None

    def show_miner_status(self):
        miner_stats = \
            f"name: {'stoicminer0'}\n" \
            f"24hnumreward: {self.numreward24h}\n" \
            f"24hreward: {self.reward24h}\n" \
            f"{self.workers_stats()}\n"
        return miner_stats

    def workers_stats(self):
        miner_stats_text = []
        for key in self.workers:
            stats_text = \
                f"ID                : {key}\n" \
                f"offline           : {self.workers[key]['offline']}\n" \
                f"Last Beat         : {self.workers[key]['lastBeat']}\n" \
                f"Current Hash Rate : {self.workers[key]['hr']}\n" \
                f"Average Hash Rate : {self.workers[key]['hr2']}\n"

            miner_stats_text.append(stats_text)
        return miner_stats_text

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
            self.miner = self.workers['stoicminer0']

    def send_email(self):
        if self.mail_service is None:
            print("Mail Service is None")
        else:
            subject_text = "rvn 2Miners Update"
            body_text = self.show_miner_status()
            self.mail_service.send_email(subject_text, body_text)
            print(f"email sent: {self.mail_service.mail_to}")

    def schedule_email_updates(self, number_seconds):
        self.scheduler = BlockingScheduler()
        self.scheduler.add_job(self.send_email, 'interval', seconds=number_seconds)
        self.scheduler.start()

    def send_sms(self):
        account.twillio_service.send_sms(account.show_miner_status(), "+16262441779")

    def schedule_sms_updates(self, number_seconds):
        if self.twillio_service is None:
            print("error: twillio_service is None")
        else:
            self.scheduler = BlockingScheduler()
            self.scheduler.add_job(self.send_sms, 'interval', seconds=number_seconds)
            self.scheduler.start()


if __name__ == '__main__':
    rvn_address = ""
    account = Account(rvn_address)

    # send email updates
    # my_gmail_user = ""
    # my_gmail_password = ""
    # account.mail_service = MailService(my_gmail_user, my_gmail_password)
    # account.mail_service.mail_to = ""
    # account.schedule_email_updates(60)

    # send sms updates
    # account.twillio_service = TwillioService(account_sid="", auth_token="", from_number="")
    # account.twillio_service.to_number = ""
    # account.schedule_sms_updates(10)
