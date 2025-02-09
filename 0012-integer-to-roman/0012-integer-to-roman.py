class Solution:
    def intToRoman(self, num: int) -> str:
        to_roman_dict = {1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
        my_str = ""
        for integer,roman in reversed(to_roman_dict.items()):
            num1 = num//integer
            num = num % integer
            my_str += roman * num1
        return my_str
