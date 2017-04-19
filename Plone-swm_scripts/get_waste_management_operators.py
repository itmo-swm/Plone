# Function for getting of  waste management operators list
import string

brains=context.portal_catalog.searchResults({'portal_type' : ('waste_management_operator',)})

print "[" + ' ' 

for b in brains:
 print "{"
 o=b.getObject()
 print '"id":"%s",' % b.getURL()
 print '"title":"%s",' % o.title
 print '"desription":"%s"' % o.description
 print "},"

return printed[:-2] + '\n' + "]"
