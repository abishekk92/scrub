from scrapely import Scraper
import sys
import json
try:
	scrape_site=sys.argv[1]
except:
	print 'Invalid arguements. Usage python scrape.py <site-name>'
	sys.exit(2)
print 'Training the scraper with existing data-set'
s=Scraper()
result={}
train_data=json.loads(open(scrape_site+'_train.json','r').read())
for data in train_data:
	s.train( data['url'],{'name':data['title']})
test_data=json.loads(open(scrape_site+'_tests.json','r').read())
for data in test_data:
	result.update(s.scrape(data['url']))
open(scrape_site+'_result.json','w').write(json.dumps(result))

