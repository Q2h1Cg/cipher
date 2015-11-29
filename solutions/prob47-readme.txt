Bleichenbacher's PKCS 1.5 Padding Oracle (Simple Case)
题目描述：
一.构造密钥生成器
	生成[N，e,d]密钥对。
二.构造扩展判断预言机
	1.接受访问者输入密文，并对密文用（N,d）进行解密
	2.若解出明文第一字节m[0]==0,第二字节m[1]==2，返回True，否则返回False