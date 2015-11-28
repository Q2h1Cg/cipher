Implement a MITM key-fixing attack on Diffie-Hellman with parameter injection
��Ŀ������
ͨ������ע��ʵ��ȷ����Կ�Ķ���Diffie-Hellman���м��˹���
������Э�飺
A->B
Send "p","g","A"
B->A
Send "B"
A->B
Send AES-CBC(SHA1(s)[0:16],iv=random(16),msg)+iv
B->A
Send AES-CBC(SHA1(s)[0:16],iv=random(16),A's msg)+iv

 
�������м��˹����Ĺ��̣�
A->M
Send"p","g","A"
M->B
Send"p","g","p"
B->M
Send"B"
M->A
Send"p"
A->M
Send AES-CBC(SHA1(s)[0:16],iv=random(16),msg)+iv
M->B
Relay that to B
B->M
Send AES-CBC(SHA1(s)[0:16],iv=random(16),A's msg)+iv
M->A
Relay that to A
 
A��B�Ĺ�����Կ��Э���б��滻Ϊp
���ھ�����Ҫ��д����ʵ���м��˹���������̡�
