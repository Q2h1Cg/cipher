Implement and break HMAC-SHA1 with an artificial timing leak
题目大意：
	实现利用人为时间漏洞打破HMAC-SHA1。
	自己编写Web框架，写一个小应用程序,包含文件参数和签名参数。并用在服务器端产生的密钥，用人为扩大比对时间的早退出函数对其进行验证。
	题目的目的是编写应用程序，为所有的文件找到所有可用的MAC。