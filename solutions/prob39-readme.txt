Implement RSA
��Ŀ������
1.n=p*q
2.et=(p-1)*(q-1)
3.e=3
4.d=invmod(e,et)(invmod��ģ�棬����invmod(17,3120)=2753)
5.pk->[e,n],sk->[d,n]
6.encrypt:c=m**e%n   ddecrypt:m=c**d%n
7.�ô��������ظ�������ʹ��e=3��
��д�������һ���ַ���