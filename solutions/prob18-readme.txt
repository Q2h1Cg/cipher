Implement CTR, the stream cipher mode

The string:
L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==

���±ߵĲ�����������CTRģʽ������һ��AES�������ģʽ����AESת���������룩�����Ƶ�Ӣ������
key=YELLOW SUBMARINE
nonce=0
format=64 bit unsigned little endian nonce,
       64 bit little endian block count (byte count / 16)
CTRģʽ�Ƿǳ��򵥵�
�������һ�����ģ�CTRģʽ����һ��������������һ��16�ַ����keystream
���磺
���ϱ߲���������3��16�ֽ�
keystream = AES("YELLOW SUBMARINE",
                "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
keystream = AES("YELLOW SUBMARINE",
                "\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00")
keystream = AES("YELLOW SUBMARINE",
                "\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00")
CTRģʽ����Ҫpadding������������ģ���ֻҪֹͣ���Ͳ���keystream
���ܺͼ�����ͬ�ģ�������ͬ��keystream�����͸�������
������ͷ�ͽ����Ǹ��ַ���һ��ʼ����string����Ȼ��ʹ��CTR����ȥ���ܺͽ����������ַ�
����������ִ�����ѧ������CTRģʽȥת����������Ϊ�����룬��Ϊ�����÷������м��ܣ����Ǹ��������ü��������롣