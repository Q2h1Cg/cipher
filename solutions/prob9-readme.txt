Implement PKCS#7 padding
��Ŀ���������������һ������PKCS#7�������⣬���ڲ�������鳤�ȵ������ڼ��ܹ�������Ҫ������䣬������������Ǳ�д��PKCS#7Ϊ�����������
���磺
"YELLOW SUBMARINE"
... padded to bytes would be:
"YELLOW SUBMARINE\x04\x04\x04\x04"

"I am a little teapot short and stout"
... padded to bytes would be:
"I am a little teapot short and stout\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c"