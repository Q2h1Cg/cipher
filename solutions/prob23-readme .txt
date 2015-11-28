Clone an MT19937 RNG from its output
题目描述：
理解 MT19937 RNG 内部的线性映射方法（temper），实现它的逆算法（untemper）。
在实现untemper算法后重新获取624个输出，用untemper重新设置MT19937 RNG状态，并预测原始值。