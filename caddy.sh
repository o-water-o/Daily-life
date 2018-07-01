#!/bin/bash
path=`pwd`


#下载、安装、修改配置文件
initial(){	
	
	if [ ! -f caddy*.tar.gz ]; then
		#statements	
		echo "开始下载、安装文件"
		wget -c https://github.com/mholt/caddy/releases/download/v0.11.0/caddy_v0.11.0_linux_amd64.tar.gz
		tar -xzf caddy*.tar.gz caddy
		sudo mv ./caddy /usr/local/bin
		mkdir /home/test/bin/caddy
		mkdir /home/test/bin/caddy/www
		mkdir /home/test/bin/caddy/www/spot1.tk
	fi
	echo "修改配置文件"
	cat>/home/test/bin/caddy/Caddyfile<<eof
spot1.tk {
root /home/test/bin/caddy/www/spot1.tk
gzip
log /home/test/bin/caddy/access.log
tls 457331510@qq.com
errors /home/test/bin/caddy/error.log {

rotate_size     100
rotate_age      15
rotate_keep     5
rotate_compress
	}

	}
eof
	chmod +xw /home/test/bin/caddy/Caddyfile
if [ $? -eq 0 ]; then
	echo "##############成功##############"
else
	echo "失败"
fi
	cd $path
}



#判断命令是否执行成功
pd(){
	if [ $? -eq 0 ]; then
		echo "###$1成功###"
	else
		echo "!!!$1失败!!!"
	fi
}

#输出日志判断
rz(){
	if [  -d $1 ]; then
		sudo tail -n -5 $1
	else
		echo "无日志存在"
	fi
}



start(){
	sudo nohup caddy -conf /home/test/bin/caddy/Caddyfile 1>/home/test/bin/caddy/qidongrizhi.log 2>&1 &
	pd "caddy启动" 
	#echo "启动成功"
	sleep 2
	rz /home/test/bin/caddy/access.log
}

stop(){
	a=`ps a -ef |grep caddy|awk '{ print $2}'|grep -v caddy.sh|grep -v grep`
	echo $a
	#4pidof caddy
	sudo kill $a
	pd "caddy停止"
	#echo "停止成功"
	rz /home/test/bin/caddy/access.log
}

change(){
	vi /home/test/bin/caddy/Caddyfile
	sleep 2
	echo "配置文件修改成功"

	sudo tail -n -3 /home/test/bin/caddy/access.log
}




echo "请输入操作序号： 
——————————————————————
1. 下载、安装、配置caddy
2. 启动 caddy
3. 停止 caddy
4. 编辑配置文件
———————————————————————"
read -p "请输入数字： " choice
case $choice in
	1)
	initial;;
	2)
	start;;
	3)
	stop;;
	4)
	change;;

	*)
	exit 1;;
esac
exit 0