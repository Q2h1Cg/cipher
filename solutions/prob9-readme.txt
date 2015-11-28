Implement PKCS#7 padding
题目描述：这个问题是一个关于PKCS#7填充的问题，对于不规则分组长度的明文在加密过程中需要进行填充，这个题的任务就是编写以PKCS#7为规则的填充代码
例如：
"YELLOW SUBMARINE"
... padded to bytes would be:
"YELLOW SUBMARINE\x04\x04\x04\x04"

"I am a little teapot short and stout"
... padded to bytes would be:
"I am a little teapot short and stout\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c"