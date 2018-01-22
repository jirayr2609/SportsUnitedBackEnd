from rest_framework import viewsets
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from accounts.models import *
import datetime

class SendEmail(object):
	def __init__(self):
		self.url = 'https://sporta.com/'
		self.company_name = 'SPORTA'
		self.from_email = 'e.amespizarro@gmail.com'
		self.cc = ['plugr@zahncenternyc.com']

	def release_email(self, sub, body, frm, to, cc=None):
		constructing_email = EmailMessage(sub, body, frm, to, cc=cc)
		constructing_email.send()

	def send_confirm_registration(self, new_registered_user, token):
		subject = '[SPORTA] Thank you for registering!'
		body = 'Please confirm your email and continue with your registration by going to the following link ' + 'localhost:8080/register/confirmation/' + token
		self.release_email(subject, body, self.from_email, [new_registered_user], self.cc)

	# def send_request_approval(self, partner_emails, deal_name, partner_slug):
	# 	subject = '[Pinebase] Pending user approval'
	# 	body = 'You have request to view the deal ' + deal_name + '. Please visit http://li100-185.members.linode.com:8077/deals/edit-partner/manage/' + partner_slug + '/'
	# 	self.release_email(subject, body, self.from_email, partner_emails, self.cc)

	# def send_approved_request(self, requester_email):
	# 	subject = '[Pinebase] Your request has been approved'
	# 	body = 'Your request for ____deal name____ has been approved. Please visitPlease http://li100-185.members.linode.com:8077/deals/ to view the deal'
	# 	self.release_email(subject, body, self.from_email, [requester_email], self.cc)

	# def send_message_notification(self, reciever): # reciver  = ['a@abc.com', 'b@abc.com']
	# 	subject = '[Pinebase] You recieved a new message'
	# 	body = 'New Message from ___sender name____. Please check your inbox to view the message or follow this link http://li100-185.members.linode.com:8077/deals/sometlinkheretoinbox'
	# 	self.release_email(subject, body, self.from_email, reciever, self.cc)

	# def send_document_request(self, partner_email_list):
	# 	subject = '[Pinebase] You recieved a new document request'
	# 	body = 'Document request from ___sender name____. Please check your account to view request or follow this link http://li100-185.members.linode.com:8077/deals/edit-partner/manage/alpine'
	# 	self.release_email(subject, body, self.from_email, partner_email_list, self.cc)


	# def send_approved_document(self, requester_email):
	# 	subject = '[Pinebase] Your document request has been approved'
	# 	body = 'Document request for ____deal name____ is now approved. Please http://li100-185.members.linode.com:8077/deals/ .../.. to download the document'
	# 	self.release_email(subject, body, self.from_email, [requester_email], self.cc)

	# def send_ioi(self, partner_emails, deal_name):
	# 	subject = '[Pinebase] New IOI on your open deal'
	# 	body = 'To view your new indication of interest on ' + deal_name + '. Please visit http://li100-185.members.linode.com:8077/deals/'
	# 	self.release_email(subject, body, self.from_email, partner_emails, self.cc)

	# def get_partner_emails(self, deal_instance):
	# 	email_list = []
	# 	for partner in deal_instance.partners.all():
	# 		users = partner.user.all()
	# 		for user in users:
	# 			email_list.append(user.email)
	# 	return email_list




