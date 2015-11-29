Break fixed-nonce CTR mode using substitions
题目描述：
用你CTR加解密函数和令noun=0.产生一个随机AES key

在连续加密（不是用一个运行的CTR），加密给出base64密文，产生多个独立的密文（这将产生40个短CTR加密的密文）
因为每个CTRnonce不是随机的，用相同的密钥加密，这是很糟糕的

像大多数的流密码（包括RC4和CTR模式下的分组密码），实际上这些“加密”一个字节可以归结为异或操作
CIPHERTEXT-BYTE XOR PLAINTEXT-BYTE = KEYSTREAM-BYTE
那么：
CIPHERTEXT-BYTE XOR KEYSTREAM-BYTE = PLAINTEXT-BYTE (ie, "you don't
say!")

这类型的攻击是零散的：猜字母，用英文字母频率验证猜测
