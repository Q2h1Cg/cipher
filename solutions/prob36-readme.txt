Implement Secure Remote Password (SRP)
题目描述：
实现安全的远程密码
协议过程：（N=[NIST Prime], g=2, k=3, I (email), P (password)）
服务器：1.生成一个随机整数salt
	    2.生成字符串：xH=SHA256(salt|password)
        3.通过在xH前面添加0x将xH转换成一个整数
        4.通过公式v=g**x % N生成v
        5.将数据保存
C->S
Send I, A=g**a % N (a la Diffie Hellman)
S->C
Send salt, B=kv + g**b % N
S, C
Compute string uH = SHA256(A|B), u = integer of uH
C
Generate string xH=SHA256(salt|password)
Convert xH to integer x somehow (put 0x on hexdigest)
Generate S = (B - k * g**x)**(a + u * x) % N
Generate K = SHA256(S)
S
Generate S = (A * v**u) ** b % N
Generate K = SHA256(S)
C->S
Send HMAC-SHA256(K, salt)
S->C
Send "OK" if HMAC-SHA256(K, salt) validates
就是通过编写代码实现上述认证过程。
