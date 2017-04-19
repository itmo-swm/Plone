# Function for getting of waste points list
import string

brains=context.portal_catalog.searchResults({'portal_type' : 'waste_point', 'Subject' : region })

print "[" + ' ' 

for b in brains:
 print "{"
 #print '"id":"%s",' % b.getPath()
 o=b.getObject()
 print '"id":"%s",' % o.id
 print '"title":"%s",' % o.title
 print '"desription":"%s",' % o.description
 print '"geometry":"%s' %b.getURL() + '/@@geo-json.json''",'
 print "},"


return printed[:-2] + '\n' + "]"
