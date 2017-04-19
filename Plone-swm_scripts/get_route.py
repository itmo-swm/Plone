# Function for getting of route list
import string

brains=context.portal_catalog.searchResults({'portal_type' : 'route', 'Subject' : region})

print "[" + ' ' 

for b in brains:
 print "{"
 o=b.getObject()
 print '"id":"%s",' % b.getURL()
 print '"title":"%s",' % o.title
 print '"desription":"%s",' % o.description
 print '"geometry":"%s' %b.getURL() + '/@@geo-json.json''",'
 print '"max_time_4_garbage_collection":"%s",' % o.max_time_4_garbage_collection
 print '"region":"%s"' % o.region

 print "},"

return printed[:-2] + '\n' + "]"