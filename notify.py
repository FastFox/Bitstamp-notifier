#!/usr/bin/python
import sys
import pynotify
import time
import urllib2
 
if __name__ == "__main__":
	if not pynotify.init("icon-summary-body"):
		sys.exit(1)
								  
	url = "https://www.bitstamp.net/api/ticker/"

	while 1:
		json = eval(urllib2.urlopen(url).read())
		buy = json['ask']
		sell = json['bid'] 
		last = json['last']

		n = pynotify.Notification(
			"Bitstamp",
			"Buy: " + buy + "; Sell: " + sell + "; Last: " + last,
			"notification-message-im")
		n.show()
		time.sleep(60)
