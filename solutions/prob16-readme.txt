CBC bitflipping attacks
题目描述：写两个函数：

第一个函数

在输入的字符串前面添加：
"comment1=cooking%20MCs;userdata="
在输入的字符串后面添加：
";comment2=%20like%20a%20pound%20of%20bacon"
去除；和=两个符号，然后将字符串填充为16bytes分组长度的AES分组，以一个随机的AES密钥加密。

第二个函数

实现解密的功能，并且判断明文中是否有";admin=true;"字符串，如果有的话返回True，否则返回False.
提示：加密代码如果正确则第二个函数一定会返回False。
