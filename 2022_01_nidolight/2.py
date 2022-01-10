def solution(s):
    numbers = []
    tmp_s = ""

    for c in s:
        if c.isdigit():
            numbers.append(c)
        else:
            tmp_s += c
            if tmp_s == "zero":
                numbers.append('0')
                tmp_s = ""
            elif tmp_s == "one":
                numbers.append('1')
                tmp_s = ""
            elif tmp_s == "two":
                numbers.append('2')
                tmp_s = ""
            elif tmp_s == "three":
                numbers.append('3')
                tmp_s = ""
            elif tmp_s == "four":
                numbers.append('4')
                tmp_s = ""
            elif tmp_s == "five":
                numbers.append('5')
                tmp_s = ""
            elif tmp_s == "six":
                numbers.append('6')
                tmp_s = ""
            elif tmp_s == "seven":
                numbers.append('7')
                tmp_s = ""
            elif tmp_s == "eight":
                numbers.append('8')
                tmp_s = ""
            elif tmp_s == "nine":
                numbers.append('9')
                tmp_s = ""
            
    answer = "".join(numbers)
    return int(answer)


    # nums = {
    #     'zero' : '0',
    #     'one' : '1',
    #     'two' : '2',
    #     'three' : '3',
    #     'four' : '4',
    #     'five' : '5',
    #     'six' : '6',
    #     'seven' : '7',
    #     'eight' : '8',
    #     'nine' : '9'
    # }
    # for key, value in nums.items():
    #     s = s.replace(key,value)