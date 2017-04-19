# Function for getting of trucks list
import string

brains=context.portal_catalog.searchResults({'portal_type' : 'track', 'Subject' : region })

print "[" + ' ' 

for b in brains:
 print "{"
 o=b.getObject()
 print '"id":"%s",' % b.getURL()
 print '"title":"%s",' % o.title
 print '"desription":"%s",' % o.description
 print '"geometry":"%s' %b.getURL() + '/@@geo-json.json''",'

 print '"priority":"%s",' % o.priority
 print '"max":"%s",' % o.max
 print '"volume":"%s",' % o.volume
 print '"type":"%s"' % o.type

 print "},"


return printed[:-2] + '\n' + "]"
