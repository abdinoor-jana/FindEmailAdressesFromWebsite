# FindEmailAdressesFromWebsite
third-party libraries used:
selenium, lepl.apps.rfc3696,urllib2

find_email_addresses.py will open FireFox browser to load html content and wait all the initialtion javascript to be finished.
Then it search any email address on the website and all the hyperlink and clickable component 
It will find email address from all the hyperlink that has the same domain with the typed url. 
Also, it will click all the clickable compenents on the html to discover possible redirection and check email from there.

Useage emaple:
python find_email_addresses.py jana.com
python find_email_addresses.py jana.com/contact
python find_email_addresses.py getflyp.com
python find_email_addresses.py getflyp.com/contact
