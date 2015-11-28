Break repeating-key XOR
题目描述：题目中的文件是经过重复密钥异或加密(Vigenere密码)后Base64加密的文件，将其解密。
步骤：
1.猜测密钥长度
2.对于不同的密钥长度求解该长度下不同分组密文的Hamming距离，其中最小的具有最大可能性是密钥长度。

其中Hamming距离是通过比较二进制字符bit，描述字符间的相似性
例如：
between:
this is a test
and
wokka wokka!!!
Hamming is 37.