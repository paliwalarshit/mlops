import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("arshitpaliwal9@gmail.com", "9460191899")


    # message
message = "Your accuracy is less than 90% .Try again"


    # sending the mail
s.sendmail("arshitpaliwal9@gmail.com", message)


    # terminating the session
s.quit()
