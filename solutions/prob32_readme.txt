Break HMAC-SHA1 with a slightly less artificial timing leak
题目大意：
	攻破时间漏洞较小的HMAC-SHA1
	减小上一题中“insecure_compare”函数中延时的时间，直到上一题中的方法失效。（从5ms开始）