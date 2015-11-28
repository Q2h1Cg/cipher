PKCS#7 padding validation
题目描述：
编写函数判断给出的明文是否是有效的PKCS#7填充，并且把填充的数据去除。如果不是正确的填充，返回错误信息。
例如：
The string:

"ICE ICE BABY"

... has valid padding
"ICE ICE BABY\x04\x04\x04\x04"

... does not have valid padding
"ICE ICE BABY\x05\x05\x05\x05"

... nor does:
"ICE ICE BABY\x01\x02\x03\x04"