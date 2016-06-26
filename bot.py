from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Ignore this stuff, it just makes the selenium run in "background"
display = Display(visible=0, size=(800, 600))
display.start()

#Variable used in functions
a = 0

#Stuff that you got to change
login_email = "" #Your facebook email
login_password = "" #Your facebook password

#Sending details
reciever_url       = input("Enter the reciever url: ")
reciever_name      = input("Enter the reciever name: ")
reciever_runtime   = input("How many times do you want to run this?: ")
reciever_sleeptime = input("How long do you want the pause between the messages to be?: ")
print(" 1. Count up to "+ str(reciever_runtime) + " | " " 2. Spam the time")
reciever_option    = input("What do you want to do?: ")

# If conditions to test if theres enough data to run the bot
#Check email
if login_email == "":
    print ("You need to enter your e-mail address!")
    mail_check = 0
else:
    mail_check = 1

#Check Password
if login_password == "":
    print ("You need to enter your password!")
    password_check = 0
else:
    password_check = 1

#Check reciever url
if reciever_url == "":
    print ("You need to enter the reciever url!")
    reciever_check = 0
else:
    reciever_check = 1

#Check runtime
if reciever_runtime == "":
    print ("You need to enter how many times you want to run this!")
    runtime_check = 0
else:
    runtime_check = 1

#Check sleep time
if reciever_sleeptime == "":
    print ("You need to enter the pause between messages!")
    sleeptime_check = 0
else:
    sleeptime_check = 1


#Setting up the driver, I'm using Chrome, not sure if it will work on Firefox
driver = webdriver.Chrome()

def fb_login(username, password):

    driver.get("http://m.facebook.com") #Going to the mobile version of Facebook cuz it's easier.

    #Typing the login details
    #Typing the e-mail
    email_textbox = driver.find_element_by_xpath("""//*[@id="u_0_1"]/div[1]/div/input""")
    email_textbox.send_keys(username)

    #Here i'm typing the password
    password_textbox = driver.find_element_by_xpath("""//*[@id="u_0_2"]""")
    password_textbox.send_keys(password)

    #Setting the button path
    login_button = driver.find_element_by_xpath("""//*[@id="u_0_6"]""")
    #Clicking the button
    login_button.click()

    #Waiting for the page to load
    driver.implicitly_wait(3)

    #Clicking the "Ok" button in order to log in
    skip_button = driver.find_element_by_xpath("""//*[@id="root"]/div/div/div/div[3]/div[2]/form/div/button""")
    skip_button.click()

    #Going to user
    driver.get(reciever_url)


def send_message(sleep_time, send_msg):
    #Entering the message
    #Setting path to the textbox
    message_textbox = driver.find_element_by_xpath("""//*[@id="composerInput"]""")
    #Typing the message
    message_textbox.send_keys(send_msg)

    #Sending the message
    #Setting path
    send_button = driver.find_element_by_xpath("""//*[@id="u_0_5"]""")
    #Clicking the button in order to send the message
    send_button.click()

    #Wait time before sending another message IN SECONDS!
    time.sleep( sleep_time )

print("Logging in...please wait")

def print_stats():
        print ("________________________________________________")
        print ("Message has been sent to: " + str(reciever_name))
        print ("Messages count: " + str(a) + " of " + str(reciever_runtime))
        print ("________________________________________________")

def fb_actual_loggin():
    # Login to Facebook if there's enought data
    if mail_check == 1 and password_check == 1 and reciever_check == 1:
        fb_login(login_email, login_password)
        print("Succsefully logged in!")
        succes_loging = 1
    else:
        print("Couldn't log in")
    succes_loging = 0


def infinite_count():
    a = 0
    while a <= int(reciever_runtime):
        a = a + 1
        send_message(float(reciever_sleeptime),a)
        print_stats()
    else:
        print("All the messages have been sent Lord Sam!")

def spam_time():
    a = 0
    while a <= int(reciever_runtime):
        a = a + 1
        message_to_send = "Este ora: " + str(time.strftime("%H:%M:%S")) 
        send_message(float(reciever_sleeptime),message_to_send)
        print_stats()
    else:
        print("All the messages have been sent Lord Sam!")


#Calling the log in function in order to log in, duh
fb_actual_loggin()


#Do stuff based on the user option
if int(reciever_option) == 1:
    infinite_count()

elif int(reciever_option) == 2:
     spam_time()

else:
    print ("Your option doesn't exist")

