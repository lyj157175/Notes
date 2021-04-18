'''请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
后台会用以下方式调用Insert 和 FirstAppearingOnce 函数
string caseout = "";
1.读入测试用例字符串casein
2.如果对应语言有Init()函数的话，执行Init() 函数
3.循环遍历字符串里的每一个字符ch {
Insert(ch);
caseout += FirstAppearingOnce()
}
2. 输出caseout，进行比较。
返回值描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
'''

class Solution:
    # 返回对应char
    s = ''
    def FirstAppearingOnce(self):
        for i in self.s:
            if self.s.count(i) == 1:
                return i
        return '#'


    def Insert(self, char):
        self.s += char

