Break fixed-nonce CTR mode using substitions
��Ŀ������
����CTR�ӽ��ܺ�������noun=0.����һ�����AES key

���������ܣ�������һ�����е�CTR�������ܸ���base64���ģ�����������������ģ��⽫����40����CTR���ܵ����ģ�
��Ϊÿ��CTRnonce��������ģ�����ͬ����Կ���ܣ����Ǻ�����

�������������루����RC4��CTRģʽ�µķ������룩��ʵ������Щ�����ܡ�һ���ֽڿ��Թ��Ϊ������
CIPHERTEXT-BYTE XOR PLAINTEXT-BYTE = KEYSTREAM-BYTE
��ô��
CIPHERTEXT-BYTE XOR KEYSTREAM-BYTE = PLAINTEXT-BYTE (ie, "you don't
say!")

�����͵Ĺ�������ɢ�ģ�����ĸ����Ӣ����ĸƵ����֤�²�
