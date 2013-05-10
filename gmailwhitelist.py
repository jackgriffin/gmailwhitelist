#!/usr/bin/python
import sys
import uuid
import re
import smtplib
import email

# spammy address
address = 'mail.google.com'
username = 'jgriffinwhitelist@gmail.com'
password = 'notarobot'
unsorted = 'unsorted'
approved = 'INBOX'
denied = 'nonwhitelist'

def checkmail():
	M = imaplib.IMAP4_SSL(address)
	M.login(username, password)
	M.select("INBOX", readonly=True)
	