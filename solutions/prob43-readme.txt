DSA key recovery from nonce
题目中给出了三个公用的算法参数：
p = 800000000000000089e1855218a0e7dac38136ffafa72eda7
     859f2171e25e65eac698c1702578b07dc2a1076da241c76c6
     2d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebe
     ac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2
     b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc87
     1a584471bb1
 
 q = f4f47f05794b256174bba6e9b396a7707e563c5b
 
 g = 5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119
     458fef538b8fa4046c8db53039db620c094c9fa077ef389b5
     322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a047
     0f5b64c36b625a097f1651fe775323556fe00b3608c887892
     878480e99041be601a62166ca6894bdd41a7054ec89f756ba
     9fc95302291
DSA算法介绍：
公、私钥生成：
1、选取任意整数x， 0 < x < q
2、计算 y = g^x%p
3、公钥为(p, q, g, y)，私钥为x
生成签名：
1、生成随机数k，0 < k < q
2、计算r = g^k%p%q，如果r=0，重新选取k
3、计算s=(H(m)-x*r)*(k^(-1))%q，H为哈希函数，m为待签名数据，如果s=0，重新选取k
4、(r, s)构成签名
该题目的要求就是根据nonce（k）恢复私钥，恢复的算法是：
 
   (s*k)-H(msg)
x=-------------  mod q
        r
