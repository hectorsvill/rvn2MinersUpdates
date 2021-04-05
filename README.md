# rvn2MinersUpdates
rvn.2miners.com/api/


#### Setup
##### Install libraries
- Install necessary packages.

```bash
pip3 install requests
pip3 install smtplib
pip3 install apscheduler
pip3 install twilio
```

#### Usage
##### SMS Updates
 - Set rvn address you want to track on 2Miners.
 - Create an account with twillio and enable sms.
 - Setup TwillioSerivice with your account sid, auth token and the number provided.
 - Set account.twillio_service.to_number - The number you want to send updates to. 
 - Call schedule_sms_updates and set a second interval

```python3
if __name__ == '__main__':
    rvn_address = ""
    account = Account(rvn_address)
    account.twillio_service = TwillioService(account_sid="", auth_token="", from_number="")
    account.twillio_service.to_number = ""
    account.schedule_sms_updates(10)
```
