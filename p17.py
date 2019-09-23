class NumberToWords():
    def __init__(self, num=0):
        self.num = num
        self.switcher = {
            0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety"
        }
        
    
    def set_num(self, num):
        self.num = num


    def increase_num(self):
        self.num += 1


    def dozens(self, num):
        doz = int(str(num)[0] + '0')
        return self.switcher[doz]


    def to_words(self, num):
        if num in self.switcher:
            return self.switcher[num]

        s = str(num)
        n = len(s)

        if n == 2:
            res = self.dozens(num)
            dig = int(s[1])
            if dig:
                res += '-' + self.to_words(dig)
            return res

        elif n == 3:
            res = self.to_words(int(s[0]))
            res += ' hundred '
            tmp = int(s[1:])
            if tmp:
                res += 'and ' + self.to_words(tmp)
            return res

        else:
            return 'one thousand'
        
    def get_result(self):
        return self.to_words(self.num)


def clean(s):
    s = s.replace(' ', '')
    s = s.replace('-', '')
    return s


cnt = 0

ntw = NumberToWords(1)

for i in range(1000):
    s = ntw.get_result()
    s = clean(s)
    cnt += len(s)
    ntw.increase_num()
    
print(cnt)