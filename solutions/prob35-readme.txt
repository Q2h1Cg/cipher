 Implement DH with negotiated groups, and break with malicious "g" parameters
��Ŀ������
ͨ������Ԫ��������
ԭʼЭ�飺
A->B
Send "p","g"
B->A
Send ACK
A->B
Send "A"
B->A
Send "B"
A->B
Send AES-CBC(SHA1(s)[0:16],iv=random(16),msg)+iv
B->A
Send AES-CBC(SHA1(s)[0:16],iv=random(16),A's msg)+iv
 
�м��˹�����
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

ֻ������Э����g��Ϊ1��������p����p-1
