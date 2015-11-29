Offline dictionary attack on simplified SRP
协议过程：
S		x=SHA256(salt|password),v=g**x%n

C->S		I,A=g**a%n		


S->C		salt,B=g**b%n,u=128nit random number


C		x=SHA256(salt|password)
		S=B**(a+ux)%n
		K=SHA256(s)

S		S=(A*v**u)**b%n 
		K=SHA256(S)


C->S		Send HMAC-SHA256(K,salt)
S->C		Send"ok" if HMAC-SHA256(K,salt)validates


在这个协议中服务器的“B”不取决于password
确保协议在输入有效密码是可以运行
作为一个中间人攻击者伪装成服务器，使用任意的b, B, u, and salt
从A's HMAC-SHA256(K, salt)中破解密码
