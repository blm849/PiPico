import network

# Wi-Fi credentials
ssid = 'Teksavvy095z'
password = 'yell0w123'

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Connect to your network
wlan.connect(ssid, password)