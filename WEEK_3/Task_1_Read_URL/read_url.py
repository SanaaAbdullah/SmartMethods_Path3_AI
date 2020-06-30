

import requests

# The url is from the page I created for the control panel to print the letter of the chosen button 
url = 'http://localhost/robot/Letter.php'
url_content =requests.get(url)

print(url_content.text)

