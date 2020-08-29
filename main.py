import csv, sys
from twilio.rest import Client
import schedule, time

message = 'daily announcement.txt'
csv_file = 'WCHS Daily Morning Announcements!.csv'

account_sid = 'ACb1cf5ec8359933c381db1afe5db7293a'
auth_token = '0a0be69e9bf9b3b751090604ae314a1b'
sender = '+14178155435'

with open(message, 'r') as content_file:
    sms = content_file.read()

with open(csv_file, 'r') as csv_file1:
    num_Reader = csv.reader(csv_file1)
    next(num_Reader)
    numbers = set(p[3] for p in num_Reader)


print(message)


def job():
    client = Client(account_sid, auth_token)
    for num in numbers:
        print("Sending to +1" + num)
        message = client.messages.create(to="+1" + num, from_=sender, body=sms)
    print("Done")

job()
schedule.every().monday.at("09:00").do(job)
schedule.every().tuesday.at("09:00").do(job)
schedule.every().wednesday.at("09:00").do(job)
schedule.every().thursday.at("09:32").do(job)
schedule.every().friday.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
