#!/usr/bin/python

import SoftLayer
import requests
import yaml
import json
import pprint

credsFile = open("softcreds.yaml",'r')
creds = yaml.load(credsFile)

#print creds['username']
#print creds['api_key']

client = SoftLayer.Client(username=(creds['username']), api_key=(creds['api_key']))

# this section just verified the creditial import 
#user = creds['username']
#passwrd = creds['password']
#print user
#print passwrd
#print 'import successful'

#there should be a section here to read the Vyatta details from a config file - for now these will be hardcoded

vyattaID = 75847
vyattaname = 'jbsampsortr02'
 


#this section should grab the vlan assigned to a Vyatta and the networks
#object_mask = 
raw_vlan = client['SoftLayer_Network_Gateway'].getInsideVlans(id=vyattaID, mask='networkVlanId')
#print raw_vlan

SL_gateways = []
for i in range(0, len(raw_vlan)):
	y = raw_vlan[i]
	print y
	x = client['SoftLayer_Network_Vlan'].getSubnets(id=y['networkVlanId'], mask='gateway')
	print x
	SL_gateways.append(x)

print SL_gateways
print len(SL_gateways)

#everything works to this pointm, this section cleans up the output to get a list of just the addresses
#test = SL_gateways[0]
#test2 = test[0]
#print type(test2)
#print len(test2)
#print test2
#for i in range(0, len(SL_gateways)):
#	temp = SL_gateways[i]
#	temp2 = temp[0]
#	x = temp2['gateway']
#	cleanslgateway.append(x)




#this section access the firewall API -


# this should come from a config file - update this
firewall_url = "https://169.57.11.151/rest/conf"


# this works and returns a location value in the header along with the response code.  the output needs a get to the returned location

#------------temp disabled 
#r = requests.post (firewall_url, auth=(user, passwrd), verify=False )

#print r.headers

#session = r.headers['location']

# --------------------------------------

#debug line to make sure I capture the information I expect to
#print loc


# print r.json()

# combine the location information from the first call with the host information for a valid URL 


#--------------------------------temp disabled
#show_string = "https://169.57.11.151/" + session + "/show/vpn/ipsec/site-to-site/peer/192.168.100.1/tunnel" 

#print show_string


#t = requests.post (show_string, auth=(user, passwrd), verify=False)
#print(t.text)

#--------------------------------------------------------------------------
 
#close the configuration session

#-----------------------------temp disable
#requests.delete ("https://169.57.11.151/" + session, auth=(user, passwrd), verify=False)

#make sure the sessions are cleaned up
#------------------------------temp disable
#v = requests.get ("https://169.57.11.151/rest/conf", auth=(user, passwrd), verify=False)
#print v.text
# sym link verifiy
