PKCS#7 padding validation
��Ŀ������
��д�����жϸ����������Ƿ�����Ч��PKCS#7��䣬���Ұ���������ȥ�������������ȷ����䣬���ش�����Ϣ��
���磺
The string:

"ICE ICE BABY"

... has valid padding
"ICE ICE BABY\x04\x04\x04\x04"

... does not have valid padding
"ICE ICE BABY\x05\x05\x05\x05"

... nor does:
"ICE ICE BABY\x01\x02\x03\x04"