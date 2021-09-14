import os
import time
from datetime import date 
from datetime import datetime

def send_messages(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

def get_today():
    return datetime.today().strftime('%A')

def get_hour():
    return datetime.now().strftime("%H:%M")

now = get_hour()
day = get_today()
phone = "8185578599"

send_messages(phone, "Hello, This is TheGamingCube's Bot")
send_messages(phone, "This will be a bot that notifies you when you have class!")

while True:
    time.sleep(60)
    now = get_hour()
    day = get_today()
    print("now =", now)
    print("today = ", day)
    if day == "Monday" or day == "Wednesday":
        if now == "7:55":
            send_messages(phone, "You Have Class in 5 Minutes, get ready to join")
        elif now == "7:59":
            send_messages(phone, "One Minute Till AP Bio!")
            send_messages(phone, "https://us02web.zoom.us/j/96182082414?pwd=eUc0SXpsS09ndmhhVWRzamtIcmRrQT09")
        elif now == "9:25":
            send_messages(phone, "You Have Class in 5 Minutes, get ready to join")
        elif now == "9:29":
            send_messages(phone, "One Minute Till AP Calculus BC!")
            send_messages(phone, "https://zoom.us/j/95979662195?pwd=d1RKRDFsaUR2ZUFMemowRVNGUTcxUT09")
        elif now == "10:55":
            send_messages(phone, "You Have Class in 5 Minutes, get ready to join")
        elif now == "10:59":
            send_messages(phone, "One Minute Till Digital Photo!")
            send_messages(phone, "https://meet.google.com/lookup/edzlr67rei?authuser=1&hs=179")
        elif now == "14:30":
            send_messages(phone,"Attendence Forms")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=1")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=2")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=3")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=7")
        if day == "Monday" and now == "14:59":
            send_messages(phone, "One Minute Till XC Google Meets")
            send_messages(phone, "https://meet.google.com/lookup/edzlr67rei?authuser=1&hs=179")

    elif day == "Tuesday" or day == "Thursday":
        if now == "7:55":
            send_messages(phone, "You Have Class in 5 Minutes, get ready to join")
        elif now == "7:59":
            send_messages(phone, "One Minute Till AP Gov!")
            send_messages(phone, "https://us02web.zoom.us/j/89078038414?pwd=M3VUc1pyU1FWQlI5QS9ySGFjZ0pjQT09")
        elif now == "9:25":
            send_messages(phone, "You Have Class in 5 Minutes, get ready to join")
        elif now == "9:29":
            send_messages(phone, "One Minute Till ERWC(English)!")
            send_messages(phone, "https://us02web.zoom.us/j/82412177292?pwd=UXpIWmVhKzJmb296WWt2eG1WV2s5Zz09")
        elif now == "14:30":
            send_messages(phone,"Attendence Forms")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=4")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=5")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=7")
    
    elif day == "Friday":
        if now == "8:55":
            send_messages(phone, "If you would like to attend office hours find the class and time on here")
            send_messages(phone, "https://docs.google.com/document/d/1zWlMsYWrB7KzbIUgNECZ-hWzDCvJBQuUCTP6wPg1fKU/edit")
            send_messages(phone, "AP Bio - https://us02web.zoom.us/j/96343587368?pwd=WGpTTXFNSDRLcVVkSTN4bzRZQ1FmZz09")
            send_messages(phone, "AP Calc BC - https://zoom.us/j/95904304937?pwd=dGEwUnVrU1FObFZiUzBKV0lENTd1dz09")
            send_messages(phone, "Digital Photo does not have friday office hours")
            send_messages(phone, "AP Gov - https://us02web.zoom.us/j/84029102432?pwd=WGE5TE9jRndjRENQMWRQTndLYWJXUT09")
            send_messages(phone, "ERWC - https://us02web.zoom.us/j/82383516265?pwd=OFE4Z0ljZnltZDR1NkVuWGxlMWlUdz09")
        if now == "15:00":
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=1")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=2")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=3")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=4")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=5")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=7")

    elif day == "Saturday":
        if now == "12:25":
            send_messages(phone, "You Have Class in 5 Minutes, get ready to join")
        elif now == "12:29":
            send_messages(phone, "One Minute Till CS 130 - Introduction to Algorithms (GCC)")
            send_messages(phone, "https://cccconfer.zoom.us/j/93266916651?pwd=enN3em1xMzRjbTlFRWpXMEN1aVRnZz09")
    
    else:
        if now == "12:00":
            send_messages(phone, "No classes today but make sure to get your work done and prepare for any upcoming tests.")