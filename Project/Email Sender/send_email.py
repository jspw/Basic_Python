import smtplib,webbrowser,getpass
#simple mail transport protocole -> smtp 

def get_mail():
    servicesAvailable = ['hotmail','gmail','yahoo','outlook']
    while True:
        mail_id = input("E-mail : ")
        if '@' in mail_id and '.com' in mail_id :
            at_pos = mail_id.find('@')
            com_pos = mail_id.find('.com')
            sp=mail_id[at_pos+1:com_pos]
            if sp in servicesAvailable :
                return mail_id,sp
                break

            else :
                print("We don't provide service for " + sp)
                print("We provide service for ")
                print(servicesAvailable)
                continue
        else :
            print("Invalid E-mail\nPlease retype again ")
            continue



def set_smtp_domain(serviceProvider):
    if serviceProvider == 'gmail':
        return 'smtp.gmail.com'
    elif serviceProvider == 'outlook' or serviceProvider == 'hotmail':
        return 'smtp-mail.outlook.com'
    elif serviceProvider == 'yahoo':
        return 'smtp-mail.yahoo.com'



print("Welcome ! You can send E-mail through the programme")
print("Please , Enter your email and password")
user_email,sp = get_mail()
password=getpass.getpass("Password: ")

while True:
    try:
        domain = set_smtp_domain(sp)
        connection = smtplib.SMTP(domain,587)
        connection.ehlo()
        connection.starttls()
        connection.login(user_email,password)

    except:
        print("Something is Wrong please try again")
        print("Please , Enter your email and password")
        user_email,sp = get_mail()
        password=input("Password: ")
        continue

    else :
        print("Login successfull")
        break;


print("Please enter recevier's E-mail adress")
receverAddress,receverSp = get_mail()
print("Please type Subject and Message ")
Subject = input("Subject : ")
Message = input("Message : ")

connection.sendmail(user_email,receverAddress,("Subject: " + str(Subject) + "\n\n" + str(Message)))
print("E-mail send successfully")
print("Thanks for using our service")


connection.quit() # finished  
