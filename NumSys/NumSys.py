class NumSystem :
    def binary2int(num): 
        num = str(num)
        n = 0
        result = []
        count = len(num)
        long = count - 1 

        while count > 0 : 

            if '1' in num[n] :
                result.append( 2**(long) )

            elif '0' in num[n] :
                pass

            n += 1
            count -= 1
            long -= 1 

        return (sum(result))   

    def int2binary(q):
        result  = [] 
        while q != 0 :
            r = q % 2
            result.insert( 0 ,str( r ) )
            q = int(q/2)
        return print(*result , sep='')

    def int2hex (num) :

        result_list = []

        remainder = 1

        if num in range (1,10):
            return print(num)

        while num / 16 != 0 :
            remainder = int(num % 16)
            if remainder >= 10:
                match remainder :
                    case 10 :
                        result_list.insert(0 ,'A')
                    
                    case 11 :
                        result_list.insert(0 ,'B')
                    
                    case 12 :
                        result_list.insert(0 ,'C')
                    
                    case 13 :
                        result_list.insert(0 , 'D')
                    
                    case 14 :
                        result_list.insert( 0 ,'E')
                    
                    case 15 :
                        result_list.insert( 0 ,'F')
            elif remainder > 0 : 
                result_list.insert(0 ,remainder)
            else:
                break
            num = num / 16

        return print(*result_list, sep='')

    def hex2int (input_hex) :

        result_list = []
        char_index = 0
        for i in reversed(range(len(input_hex))) :

            char = str(input_hex[char_index])

            match char :
                case 'A' :
                    if len(input_hex) == 1:
                        return 10
                    result_list.append((10*16**i))
                
                case 'B' :
                    if len(input_hex) == 1:
                        return 11
                    result_list.append((11*16**i))
                
                case 'C' :
                    if len(input_hex) == 1:
                        return 12
                    result_list.append((12*16**i))
                
                case 'D' :
                    if len(input_hex) == 1:
                        return 13
                    result_list.append((13*16**i))
                
                case 'E' :
                    if len(input_hex) == 1:
                        return 14
                    result_list.append((14*16**i))
                
                case 'F' :
                    if len(input_hex) == 1:
                        return 15
                    result_list.append((15*16**i))
                    
            if char in '1' '2' '3' '4' '5' '6' '7' '8' '9' '0' and  int(char) < 10 :
                result_list.append((int(char)*16**i))

            char_index += 1
        return sum(result_list)

    def octal2int(num) :
        result_list = []
        char_index = 0
        num = str(num)
        for i in reversed(range(len(num))) :
            char = int(num[char_index])

            result_list.append((char*8**i))

            char_index += 1
        return sum(result_list)


    def int2octal(num) :

        result_list = []

        while num / 8 > 0:
            
            remainder = int(num % 8) 
            num = num / 8
            if float(remainder) <1:
                break
            result_list.insert(0 ,remainder)
        return print(*result_list , sep='')

class Main:
    def NumConvert(num , out , inp):
        out , inp = int(input('Из какой системы: ')) , int(input('В какую систему: '))
        if out == 16 :
            num = str(num)
        else:
            num = int(num)
        match (out):
            case 2:
                if inp == 8:
                    NumSystem.int2octal(NumSystem.binary2int(num))
                elif inp == 10 :
                    print( NumSystem.binary2int(num))
                elif inp == 16 :
                    NumSystem.int2hex(NumSystem.binary2int(num))
            case 8:
                if inp == 2:
                    NumSystem.int2binary(NumSystem.octal2int(num))
                elif inp == 10:
                    print( NumSystem.octal2int(num))
                elif inp == 16:
                    NumSystem.int2hex(NumSystem.octal2int(num))
            case 10:
                if inp == 2:
                    NumSystem.int2binary(num)
                elif inp == 8:
                    NumSystem.int2octal(num)
                elif inp == 16:
                    NumSystem.int2hex(num)
            case 16:
                if inp == 2:
                    NumSystem.int2binary(NumSystem.hex2int(num))
                elif inp == 10:
                    print(NumSystem.hex2int(num))
                elif inp == 8:
                    NumSystem.int2octal(NumSystem.hex2int(num))