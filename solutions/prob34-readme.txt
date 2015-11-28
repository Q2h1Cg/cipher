Implement a MITM key-fixing attack on Diffie-Hellman with parameter injection
题目描述：
通过参数注入实现确定密钥的对于Diffie-Hellman的中间人攻击
正常的协议：
A->B
Send "p","g","A"
B->A
Send "B"
A->B
Send AES-CBC(SHA1(s)[0:16],iv=random(16),msg)+iv
B->A
Send AES-CBC(SHA1(s)[0:16],iv=random(16),A's msg)+iv

 
下面是中间人攻击的过程：
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
 
A和B的公共密钥在协议中被替换为p
现在就是需要编写代码实现中间人攻击这个过程。
