Offline dictionary attack on simplified SRP
Э����̣�
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


�����Э���з������ġ�B����ȡ����password
ȷ��Э����������Ч�����ǿ�������
��Ϊһ���м��˹�����αװ�ɷ�������ʹ�������b, B, u, and salt
��A's HMAC-SHA256(K, salt)���ƽ�����
