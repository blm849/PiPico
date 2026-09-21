import network
import requests

# Wi-Fi credentials
ssid = 'Teksavvy095z'
password = 'yell0w123'

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Connect to your network
wlan.connect(ssid, password)

# Make GET request
response = requests.get("http://google.com")
# Get response code
response_code = response.status_code
# Get response content
response_content = response.content

# Print results
print('Response code: ', response_code)
print('Response content:', response_content)