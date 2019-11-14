from django.conf import settings
import smtplib

from django.contrib import messages


def my_send_mail(request, name, email, number, text):
    msg = """
        You have a new contact request from """ + name + """

        Name: """ + name + """       
        Email: """ + email + """
        Number: """ + number + """
        Message: """ + text + """
    """
    msg.format(name, email, number, text)

    email_msg = "Subject: Contact Request \n\n" + msg.format()
    smtp = smtplib.SMTP('smtp.gmail.com')
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    recipiant = 'share.enquiries@gmail.com'

    messages.success(request, 'Thanks for getting in touch!')

    smtp.sendmail(settings.EMAIL_HOST_USER, recipiant, email_msg)

    smtp.quit()


def authError(request):
    messages.warning(request, 'Sorry, Your email can not be sent at this time!')

