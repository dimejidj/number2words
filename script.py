def number2words(n):
    """ works for numbers between 0 and 999999 """
    numbers = {
        '0' : 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        '20': 'twenty',
        '30': 'thirty',
        '40': 'forty',
        '50': 'fifty',
        '60': 'sixty',
        '70': 'seventy',
        '80' : 'eighty',
        '90' : 'ninety',
        '00' : 'hundred',
        '000' : 'thousand'
        }
    
    str_num = str(n)
    def check_tens(string, ind):
        tens = string[ind] + '0'
        tens_int = int(tens)
        if int(string) < 20:
            return numbers[string]
        elif string[ind + 1] == '0':
            return f'{numbers[tens]}'
        elif tens_int < 10:
            return f'{numbers[tens]} {numbers[string[ind + 1]]}'
        else:
            return f'{numbers[tens]}-{numbers[string[ind + 1]]}'
            
    def check_hund(string, ind):
        string_last_two = string[ind -2] + string[ind -1]
        last_two = int(string_last_two)
        if last_two < 10:
            if string_last_two == '00':
                return '{} {}'.format(numbers[string[ind]],numbers['00'])
                
            else:
                return '{} {}'.format(numbers[string[ind]],check_tens(string, 1))
                
        elif last_two < 20 and last_two >= 10:
            return '{} {} {}'.format(numbers[string[ind]], numbers['00'], numbers[string_last_two])
        else: 
            return '{} {} {}'.format(numbers[string[ind]],numbers['00'],check_tens(string_last_two, ind))
   
    def check_thou(string, ind):
        string_last_three = string[ind - 3] + string[ind -2] + string[ind -1]
        last_three = int(string_last_three)
        last_two = string[ind -2] + string[ind -1]
        last_two_int = int(last_two)
        last_one = string[ind -1]
        last_one_int = int(last_one)
        if string[ind -3] == '0' and string[ind -2] == '0' and string[ind -1] == '0' :
            return '{} {}'.format(numbers[string[ind]], numbers['000'])
        elif string[ind -3] != '0' and string[ind -2] == '0' and string[ind -1] == '0':
            return '{} {} {} {}'.format(numbers[string[ind]], numbers['000'], numbers[string[ind -3]], numbers['00'])
        elif 0 < last_two_int < 20 and string[ind -3] == '0':
            if last_two[ind -2] == '0':
                return '{} {} {}'.format(numbers[string[ind]], numbers['000'], check_tens(string[ind -1], 0))
            else:    
                return '{} {} {}'.format(numbers[string[ind]], numbers['000'], check_tens(last_two, 0))
        elif last_three < 100:
            return '{} {} {}'.format(numbers[string[ind]], numbers['000'], check_tens(last_two, 0))
        else :
            return '{} {} {}'.format(numbers[string[ind]], numbers['000'], check_hund(string_last_three, 0))
   
   
    def check_tenthou(string, ind):
        first_two_str = string[ind] + string[ind+ 1]
        last_three_str = string[ind -3] + string[ind -2] + string[ind -1] 
        last_three = int(last_three_str)
        last_two_str = string[ind -2] + string[ind -1]
        last_two = int(last_two_str)
        if string[ind -1] == '0' and string[ind -2] == '0' and string[ind -3] == '0':
            return '{} {}'.format(check_tens(first_two_str, 0), numbers['000'])
        elif string[ind -3] != '0' and string[ind -2] == '0' and string[ind -1] == '0':
            return '{} {} {}'.format(check_tens(first_two_str, 0), numbers['000'], check_hund(last_three_str, ind))
        elif 0 < last_two < 20 and string[ind -3] == '0':
            if last_two_str[ind - 2] == '0':
                return '{} {} {}'.format(check_tens(first_two_str, ind), numbers['000'], check_tens(string[ind -1], ind))
            else:    
                return '{} {} {}'.format(check_tens(first_two_str, ind), numbers['000'], check_tens(last_two_str, ind))
        elif last_three < 100:
            return '{} {} {}'.format(check_tens(first_two_str, ind), numbers['000'], check_tens(last_two_str, ind))
        else:
            return '{} {} {}'.format(check_tens(first_two_str, ind), numbers['000'], check_hund(last_three_str, ind))
        
   
    def check_hundthou(string, ind):
        first_two_str = string[ind] + string[ind+ 1]
        first_three_str = string[ind] + string[ind + 1] + string[ind + 2]
        last_three_str = string[ind -3] + string[ind -2] + string[ind -1] 
        last_three = int(last_three_str)
        last_two_str = string[ind -2] + string[ind -1]
        last_two = int(last_two_str)
        if string[ind -1] == '0' and string[ind -2] == '0' and string[ind -3] == '0':
            return '{} {}'.format(check_hund(first_three_str, 0), numbers['000'])
        elif string[ind -3] != '0' and string[ind -2] == '0' and string[ind -1] == '0':
            return '{} {} {}'.format(check_hund(first_three_str, ind), numbers['000'], check_hund(last_three_str, ind))
        elif 0 < last_two < 20 and string[ind -3] == '0':
            print('three')
            if last_two_str[ind - 2] == '0':
                return '{} {} {}'.format(check_hund(first_three_str, ind), numbers['000'], check_tens(string[ind -1], ind))
            else:
                return '{} {} {}'.format(check_hund(first_three_str, ind), numbers['000'], check_tens(last_two_str, ind))
        elif last_three < 100:
            return '{} {} {}'.format(check_hund(first_three_str, ind), numbers['000'], check_tens(last_two_str, ind))
        else:
            return '{} {} {}'.format(check_hund(first_three_str, ind), numbers['000'], check_hund(last_three_str, ind))
   
    if len(str_num) <= 2:
        return check_tens(str_num, 0)
    elif len(str_num) == 3:
        return check_hund(str_num, 0)
    elif len(str_num) == 4:
        return check_thou(str_num, 0)
    elif len(str_num) == 5:
        return check_tenthou(str_num, 0)
    elif len(str_num) == 6:
        return check_hundthou(str_num, 0)
