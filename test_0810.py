import re,requests,json,time,os
from lxml import etree

'''
t = "20180809/腾讯课堂大师班 | 尝尝学习的甜头.jpg"
t0 = re.sub(r'[/|]+','_',t)
print(t0)
'''
'''
url = 'http://github.com'
r = requests.get(url)
print(r.status_code)
data = json.dumps(dict(r.headers),indent=4) ##indent=4,separators=(',', ': '),ensure_ascii=False
print(data)
print(r.cookies)
print('##########################################################################')
for cookie in r.cookies.keys():
	print(cookie+':'+r.cookies.get(cookie))
	print('----------------------------------------------------------------------')
'''
##url_login = 'https://ke.qq.com/'

def write_file(text,name):
	dir = time.strftime("%Y%m%d")
	if not os.path.exists((dir)):
		os.makedirs((dir))	
	with open(r'%s/%s.txt' % (dir,  re.sub(r'[/|]+','',name)),'a',encoding='utf-8') as f:
		f.write(text+'\n')


def sub_page(url):
	s = requests.session()
	url = "https://ke.qq.com/course/69943"
	r = s.get(url) 
	# print(str(r.status_code)+'\n'+json.dumps(dict(r.request.headers),indent=4))

	selector = etree.HTML(r.content)
	xp0 = selector.xpath("//div[@class='intro-course']/div/text()")
	for i in xp0:
		name = selector.xpath("//span[@class='title-main']/text()")
		
		#print(re.sub(r'\n','',i))
		write_file(re.sub(r'\n','',i),name[0])
	xp1 = selector.xpath("//div[@class='task-part-list']//h3[@class='part-tt']")
def index_page():
	s = requests.session()


if __name__ == '__main__':
	sub_page()
