
# Alert functions: alarm and emergency email


# import packages

import smtplib
import ssl
import pygame

def sound_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("Data_alert/alarm.wav")
    pygame.mixer.music.play()
    print('[ALERT]: Sound played')


def send_email(username, contact_name, contact_email,fatigue_percentage):
    """
    The function sends an email to an emergency contact, letting him know the driver is asleep
    Note:
    In order to send an email using this Google account, we had to enable "less secure app access".
    This needs to be done once in a while, since Google automatically turns this setting off if it is not being used.
    """
    sender_email = "innovisiontn@gmail.com"
    sender_password = "cvfy wwpc xekk bbhe"
    message = open("Data_alert/email_message.txt").read().replace("CONTACT_NAME", contact_name).replace("DRIVER_NAME", username).replace("FATIGUE_PERCENTAGE", str(fatigue_percentage))  # read the message and paste contact and driver names
    with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465, context=ssl.create_default_context()) as server:
        server.login(sender_email, sender_password)  # log into sender account
        server.sendmail(sender_email, contact_email, message)  # send the email to emergency contact
    print('[ALERT]: mail sent')