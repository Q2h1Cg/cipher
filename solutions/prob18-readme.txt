Implement CTR, the stream cipher mode

The string:
L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==

用下边的参数，解密在CTR模式（这是一种AES分组加密模式，把AES转换成流密码）下类似的英文明文
key=YELLOW SUBMARINE
nonce=0
format=64 bit unsigned little endian nonce,
       64 bit little endian block count (byte count / 16)
CTR模式是非常简单的
代替加密一个明文，CTR模式加密一个计数器，产生一个16字符块的keystream
例如：
用上边参数产生的3个16字节
keystream = AES("YELLOW SUBMARINE",
                "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
keystream = AES("YELLOW SUBMARINE",
                "\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00")
keystream = AES("YELLOW SUBMARINE",
                "\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00")
CTR模式不需要padding，当你加密明文，你只要停止异或和产生keystream
解密和加密相同的，产生相同的keystream，异或和覆盖明文
函数开头就解密那个字符（一开始给的string），然后使用CTR函数去加密和解密其他的字符
绝大多数的现代密码学依赖于CTR模式去转化分组密码为流密码，因为比起用分组序列加密，我们更趋向于用加密流密码。