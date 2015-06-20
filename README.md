Dependencies:
Selenium (sudo pip install selenium)
Need to install FirFow broswer

find_email_addresses.py will open a FireFox browser to load all the initialtion javascript to be finished
and then load the html content.
Then it search any email address on the website and all the hyperlink and clickable component 
It will find email address from all the hyperlink that has the same domain with the typed url. 
Also, it will click all the clickable compenents on the html to discover possible redirection and check email from there.

Useage emaple:
python find_email_addresses.py jana.com\n
python find_email_addresses.py jana.com/contact
python find_email_addresses.py getflyp.com
python find_email_addresses.py getflyp.com/contact
