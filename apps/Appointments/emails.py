from django.core.mail import send_mail
from validate_email import validate_email

def sendEmail(request, user, organization, appointment):
    
    orgAddress = organization.address + ", " + organization.city + ", " + organization.country
    print(appointment)
    # Use " if validate_email(email, verify=True): " for verifying email. But it will take more time to send email.
    if not validate_email(user.emailAddress):
        return
    subject='Appointment Request Received'
    body=('Hello,\n\n' 
    'We have received your appointment request.\n'
    'Location: ' + organization.name + '\n'
    'Address: ' + orgAddress + '\n'
    #'Date: ' + appointment.dateOfAppointment + '\n'
    #'Time: ' + appointment.timeOfAppointment + '\n\n'
    'You will receive a confirmation email, once your appointment is confirmed.\n\n'
    'Note:  The waiting period may vary depending on the process.\n\n'
    'Thank you. Have a great day!!')
    frm='kinreshvpatel02@gmail.com'
    to=[]
    to.append(user.emailAddress)
    send_mail(subject, body, frm, to, fail_silently=False)
    print("email sent")