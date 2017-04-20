# Function for getting of regions list

brains=context.portal_catalog.searchResults({'portal_type' : ('region',) })

print "["

for o in context.objectValues():
 if o.portal_type == 'region':
  url = o.absolute_url()
  print "{"
  print 
  print '"id":"%s",' % url
  print '"title":"%s",' % o.title
  print '"desription":"%s",' % o.description
  print '"geometry":"%s' % url + '/@@geo-json.json''"'
  print "},"

return printed[:-2] + '\n' + "]"