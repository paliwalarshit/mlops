import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("arshitpaliwal9@gmail.com", "9460191899")


    # message
message_success = "Achieved your desired accuracy without tweeking . Congrats "


    # sending the mail
s.sendmail("arshitpaliwal9", message_success)


    # terminating the session
s.quit()
