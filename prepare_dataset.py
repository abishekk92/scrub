

import json
import re
import sys

def clean_url(url):
	return re.sub(r'^.*\n','',url)
try:
	input_file_name=sys.argv[1]
except:
	print 'Commandline arguement expected. Usage: python prepare_dataset.py <text-file-name>'
	sys.exit(2)
input=open(input_file_name,'r')
file_content=input.read().split('\t')
dataset=[]
dataset_test=[]
i=0
while i<len(file_content)/8:
	dic={}
	dic.update({'url':clean_url(file_content[4*i])})
	dic.update({'title':file_content[4*i+1]})
	dataset.append(dic)
	i=i+4
dataset_json=json.dumps(dataset)
open(input_file_name+'_train.json','w').write(dataset_json)
while i<len(file_content)/4:
	dic={}
	dic.update({'url':clean_url(file_content[4*i])})
	dataset_test.append(dic)
	i=i+4
dataset_json=json.dumps(dataset_test)
open(input_file_name+'_test.json','w').write(dataset_json)



	



