from django.core.mail import send_mail
from validate_email import validate_email
import threading
from apps.Users.models import User
from apps.Organizations.models import Organization
from apps.Appointments.models import Appointment

#region sendemail
# def sendEmail(request, user, organization, appointment):

#     orgAddress = organization.address + ", " + organization.city + ", " + organization.country
#     print(appointment)
#     # Use " if validate_email(email, verify=True): " for verifying email. But it will take more time to send email.
#     if not validate_email(user.emailAddress):
#         return
#     subject='Appointment Request Received'
#     body=('Hello,\n\n' 
#     'We have received your appointment request.\n'
#     'Location: ' + organization.name + '\n'
#     'Address: ' + orgAddress + '\n'
#     #'Date: ' + appointment.dateOfAppointment + '\n'
#     #'Time: ' + appointment.timeOfAppointment + '\n\n'
#     'You will receive a confirmation email, once your appointment is confirmed.\n\n'
#     'Note:  The waiting period may vary depending on the process.\n\n'
#     'Thank you. Have a great day!!')
#     frm='kinreshvpatel02@gmail.com'
#     to=[]
#     to.append(user.emailAddress)
#     send_mail(subject, body, frm, to, fail_silently=False)
#     print("email sent")
#endregion

def sendEmail2(request, templateID, userID, organizationID, appointmentID):
    user = User.objects.get(id=userID)
    organization = Organization.objects.get(id=organizationID)
    appointment = Appointment.objects.get(id=appointmentID)

    user_name = str(user.name).title()
    email = user.emailAddress
    orgAddress = organization.address + ", " + organization.city + ", " + organization.country
    date = str(appointment.dateOfAppointment)
    time = str(appointment.timeOfAppointment)
    # Use " if validate_email(email, verify=True): " for verifying email. But it will take more time to send email.
    if not validate_email(email):
        return
    if templateID == 1:
        subject='Appointment Request Received'
        body=('Hello ' + user_name + ',\n\n' 
        'We have received your appointment request.\n\n'
        'Location: ' + organization.name + '\n'
        'Address: ' + orgAddress + '\n'
        'Date: ' + date + '\n'
        'Time: ' + time + '\n\n'
        'You will receive a confirmation email, once your appointment is confirmed.\n\n'
        'Note:  The waiting period may vary depending on the process.\n\n'
        'Thank you. Have a great day!!')
    elif templateID == 2:
        subject='Confirmation of Appointment'
        body=('Hello ' + user_name + ',\n\n' 
        'Your appointment is confirmed.\n\n'
        'Location: ' + organization.name + '\n'
        'Address: ' + orgAddress + '\n'
        'Date: ' + date + '\n'
        'Time: ' + time + '\n\n'
        'Please arrive 10 minutes early of your scheduled appointment time.\n\n'
        'Note:  Bring necessary documents with you if needed.\n\n'
        'Thank you. Have a great day!!')
    elif templateID == 3:
        subject='Appointment Completed'
        body=('Hello ' + user_name + ',\n\n' 
        'Thank you for your time. Your appointment is now completed.\n\n'
        'Location: ' + organization.name + '\n'
        'Address: ' + orgAddress + '\n'
        'Date: ' + date + '\n'
        'Time: ' + time + '\n\n'
        'See you next time!!\n\n'
        'To book more appointments. Visit www.xyz.com/search\n\n')
    frm='kinreshvpatel02@gmail.com'
    to=[]
    to.append(email)
    send_mail(subject, body, frm, to, fail_silently=False)
    print("email sent")

def SendAsyncEmail(request, templateID, userID, organizationID, appointmentID):
    t = threading.Thread(target=sendEmail2, args=[request, templateID, userID, organizationID, appointmentID])
    t.start()
