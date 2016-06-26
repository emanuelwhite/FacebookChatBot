# FacebookChatBot
  Simple Facebook Bot that send specific messages to your friends
  
##Setting it up
  You need Python3.5 in order to run this script. After you installed Python3.5 stay with me, I'm gonn' explain below how this works.
  
  First of all, you gonn' need to install some libraries
  run the following commands in the terminal as a super user:
  
  <ol>
    <li>pip install pyvirtualdisplay</li>
    <li>pip install install selenium </li>
    <li>apt-get install chromium-browser </li>
  </ol>
  <p>Now I don't really know if this is neccessary but I had to do it, so just go <a href="http://chromedriver.storage.googleapis.com/index.html?path=2.9/">Here</a> and download the WebDriver according to your Operating System.</p>
  <p>Now that you downloaded it move that file into the /usr/bin of course that's avaiable if you're on linux. For windows users: I don't know and I don't care.</p>
  
  Alright, time to play with the code!
  
  Open the file bot.py with any text editor and change the following variables: <b>login_email</b> and <b>login_password</b> I guess that's pretty self-explanatory about what you should be writing in there
  
  Now, you should see another variables: <b>reciever_url</b> and <b>reciever_name</b>
  <p>Here's the thing, you don't have to edit them in the code, you'll be asked to input stuff in them when you will run the bot, so let me explain you really quick about what you should put in there.</p>
  <p>You have to go to <b>m.facebook.com</b> and log in, once you're logged in go the <b>Messages</b> tab, after that click on the person that you want to message and copy the url</p>
  <p>When you run the script and you're asked for the Recievers URL you just enter that url that you copied</p>
  <p>The other one <b>reciever_name</b> it's not important...it's just so that you will know where you are sending the messages if you have multiple instances of the bot running.</p>
  
  <p>If you want some custom messages just edit the variable <b>your_message</b>
  
  Now, in order to run it open the terminal and run the following command:
  <b>sudo python3.5 bot.py</b>
  
  That's all! 
