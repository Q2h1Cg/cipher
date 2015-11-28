ECB cut-and-paste
题目描述：
写一个分析例程，格式如下：
输入：profile_for("foo@bar.com")
产生：{
  email: 'foo@bar.com',
  uid: 10,
  role: 'user'
	}
然后再将其编码为：email=foo@bar.com&uid=10&role=user
要求输入中不能包含&和=，也就是说不能允许用户输入含有&和=的信息,而且用户输入的email不能是"foo@bar.com&role=admin"
A.将编码后的信息以ECB模式加密，密钥为："provide" that to the "attacker"
B.代码也需要有解密的功能
