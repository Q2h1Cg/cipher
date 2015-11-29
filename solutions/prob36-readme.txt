Implement Secure Remote Password (SRP)
��Ŀ������
ʵ�ְ�ȫ��Զ������
Э����̣���N=[NIST Prime], g=2, k=3, I (email), P (password)��
��������1.����һ���������salt
	    2.�����ַ�����xH=SHA256(salt|password)
        3.ͨ����xHǰ�����0x��xHת����һ������
        4.ͨ����ʽv=g**x % N����v
        5.�����ݱ���
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
����ͨ����д����ʵ��������֤���̡�
