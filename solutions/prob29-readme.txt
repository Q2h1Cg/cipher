Break a SHA-1 keyed MAC using length extension
题目描述：
SHA-1的长度拓展攻击。
得到一段SHA-1加密的数据后，使用填充字节填充，再插入自己经过SHA-1认证的数据，达到伪造信息的目的。