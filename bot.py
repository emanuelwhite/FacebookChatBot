from pyvirtualdisplay import Display
from selenium import webdriver
import datetime
import time
from selenium.webdriver.common.keys import Keys

display = Display(visible=0, size=(800, 600))
display.start()


login_email = "" #Your facebook email
login_password = "" #Your facebook password

reciever_url   = input("Enter the reciever url: ")
reciever_name  = input("Enter the reciever name: ")

def send_message():
    
    
    #Setting up the driver, I'm using Chrome, not sure if it will work on Firefox
    driver = webdriver.Chrome()
    driver.get("http://m.facebook.com") #Going to the mobile version of Facebook cuz it's easier.

    #Typing the login details
    #Typing the e-mail
    email_textbox = driver.find_element_by_xpath("""//*[@id="u_0_1"]/div[1]/div/input""")
    email_textbox.send_keys(login_email)

    #Here i'm typing the password
    password_textbox = driver.find_element_by_xpath("""//*[@id="u_0_2"]""")
    password_textbox.send_keys(login_password)

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
    i = 0
    while True:
        i = i + 1
        print ("________________________________________________")
        print ("Messange has been sent to: " + str(reciever_name))
        print ("Message count: " + str(i))
        print ("________________________________________________")

        #Getting time
        now = datetime.datetime.now()
        t_minute = now.minute
        t_ore = now.hour
        t_secunde = now.second

        #Composing message
        your_message = "Este ora " + str(t_ore) + " și " + str(t_minute) + " minute " + "si " + str(t_secunde) + " secunde"

        #Entering the message
        #Setting path to the textbox
        message_textbox = driver.find_element_by_xpath("""//*[@id="composerInput"]""")
        #Typing the message
        message_textbox.send_keys(your_message)


        #Sending the message
        #Setting path to the button
        send_button = driver.find_element_by_xpath("""//*[@id="u_0_5"]""")
        #Clicking the button in order to send the message
        send_button.click()

        #Wait time before sending another message IN SECONDS!
        time.sleep( 1 )
