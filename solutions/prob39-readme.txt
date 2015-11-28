Implement RSA
题目描述：
1.n=p*q
2.et=(p-1)*(q-1)
3.e=3
4.d=invmod(e,et)(invmod是模逆，例如invmod(17,3120)=2753)
5.pk->[e,n],sk->[d,n]
6.encrypt:c=m**e%n   ddecrypt:m=c**d%n
7.用大数素数重复（还是使用e=3）
编写代码加密一个字符串