# Function for getting of sgbs list
import string

brains=context.portal_catalog.searchResults({'portal_type' : 'sgb', 'Subject' : region })

print "[" + ' ' 

for b in brains:
 print "{"
 o=b.getObject()
 print '"id":"%s",' % b.getURL()
 print '"title":"%s",' % o.title
 print '"desription":"%s",' % o.description
 print '"geometry":"%s' %b.getURL() + '/@@geo-json.json''",'
 print '"cleaning_time":"%s",' % o.cleaning_time
 print '"rfid":"%s",' % o.rfid
 print '"state":"%s",' % o.state
 print '"sensor":"%s",' % o.sensor
 print '"max":"%s",' % o.max
 print '"volume":"%s",' % o.volume
 print '"type":"%s"' % o.type
 print "},"

return printed[:-2] + '\n' + "]"
