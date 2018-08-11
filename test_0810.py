# coding = utf-8
import requests,time,re,os,time
import pdb
from lxml import etree

count = 1
def download(i):
	global count
	headers = {'content-type': 'application/json',
	           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
	url = 'https://ke.qq.com/course/list/%E5%8F%A3%E8%85%94%E5%8C%BB%E5%AD%A6'
	url1 = 'https://ke.qq.com/course/list?mt=1004&st=2039&task_filter=0000000&&page={}'.format(i)
	req = requests.get(url1)
	selector = etree.HTML(req.content)

	xp0 = selector.xpath('//a[@cors-name="course"]/img/@title')
	xp1 = selector.xpath('//a[@cors-name="course"]/img/@src')
	xp3 = selector.xpath('//a[@cors-name="course"]')

	'''with open('text1.txt','w+') as f:
		for i in xp0:
			f.write(i+'\n')
	'''
	print(len(xp1))
	for j in range(1,len(xp1)):
		
		u = xp1[j]
		u = re.sub('//','http://',u)
		name = xp0[j]
		print(name+'\t'+u)
		print(name+'\t'+re.sub(r'[0-9]{3}', '510', u))
		# 
		
		
		
		#if(requests.get(re.sub(r'[0-9]{3}', '510', u),headers=headers).content):
		img = requests.get(re.sub(r'[0-9]{3}', '510', u),headers=headers).content
		print(len(str(img)+'\n'+'success')	)
			

		# pdb.set_trace()		
		
		dir = time.strftime("%Y%m%d")
		if not os.path.exists((dir)):
			os.makedirs((dir))
		try:
			with open(r'%s/%s.jpg' % (dir,  re.sub(r'[/|\v，]+','_',name)), 'wb') as f:
			#with open(str(j)+'.png','wb+') as f:
				f.write(img)	
				# pdb.set_trace()

			
			print("第 %d 个下载成功  "%count)
			count +=1
				#print(i)
		except:
			print('下载失败')
		
		
		
	print("第 %s 页  "%i)
	time.sleep(1)
	##http://10.url.cn/qqcourse_logo_ng/ajNVdqHZLLBsiadlyUgak8bicMdqiaCmqdX7tPAuBwX0a3ceT7hNhibV8Kr5ukCeDU8edZkMFfFq76I/510
if __name__ == '__main__':
	for i in range(1,20):
		download(i)
