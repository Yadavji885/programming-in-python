db = {
    "0" : "00",
    "1" : "01",
    "2" : "10",
    "3" : "11",
    "4" : "100",
    "5" : "101",
    "6" : "110",
    "7" : "111",
    "8" : "1000",
    "9" : "1001",
    "10" : "1010",
    "11" : "1011",
    "12" : "1100",
    "13" : "1101",
    "14" : "1110",
    "15" : "1111",
}

ob = {
    "0" : "00",
    "1" : "01",
    "2" : "10",
    "3" : "11",
    "4" : "100",
    "5" : "101",
    "6" : "110",
    "7" : "111"
}

hb = {
    "0" : "00",
    "1" : "01",
    "2" : "10",
    "3" : "11",
    "4" : "100",
    "5" : "101",
    "6" : "110",
    "7" : "111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111",
}

class Binary_Converter:

    def Decimal_to_Binary(self):
        n = int(input("Enter the number : \n"))
        temp = n
        hans = ""
        d = n//2
        while d != 1:
            d = n//2
            if n%2 != 0:
                n += 1
                r = n//2 - d
                hans = hans + str(r)
                n = d
            else:
                r = n//2 - d
                hans = hans + str(r)
                n = d
            if d == 1:
                hans = hans + str(d)
                ans = ""
                sr = str(hans)
                l = len(sr)
                for i in range(-1,-(l+1),-1):
                    ans = ans + sr[i]
                ans = str(ans)
                print(f"{temp} in Binary is {ans}")
                break

    def Decimal_to_Octal(self):
        n = int(input("Enter the number : \n"))
        temp = n
        hans = ""
        d = n//8
        while n != 1:
            d = n//8
            if n % 8 != 0 and n > 16:
                t = n
                while t % 8 != 0:
                    t -= 1
                r = n - t
                hans += str(r)
            elif n % 8 == 0 and n > 16:
                hans += "0"
            elif n % 8 != 0 and n > 8 and n < 16:
                tm = n
                while tm % 8 != 0:
                    tm -= 1
                r = n - tm
                hans += str(r)
            elif n == 8 or n == 16:
                hans += "01"
                break
            n = d
            if n == 1 or (n > 1 and n <= 7):
                hans += str(n)
                break
        ans = ""
        sr = str(hans)
        l = len(sr)
        for i in range(-1,-(l+1),-1):
            ans = ans + sr[i]
        ans = str(ans)
        print(f"{temp} in Octal is {ans}")
    
    def Decimal_to_Hexadecimal(self):
        n = int(input("Enter the number : \n"))
        temp = n
        hans = ""
        d = n//16
        while n != 1:
            d = n//16
            if n % 16 != 0 and n > 32:
                t = n
                while t % 16 != 0:
                    t -= 1
                r = n - t
                if r >= 10 and r <= 15:
                    print(r)
                    for i in hb.keys():
                        if hb.get(i) == db.get(str(r)):
                            hans += str(i)
                else:
                    hans += str(r)       
            elif n % 16 == 0 and n > 32:
                hans += "0"
            elif n % 16 != 0 and n > 16 and n < 32:
                tm = n
                while tm % 16 != 0:
                    tm -= 1
                r = n - tm
                hans += str(r)
                print(r)
            elif n == 16 or n == 32:
                hans += "01"
                break
            n = d
            if n >= 1 and n <= 15:
                if n >= 10:
                    for i in hb.keys():
                        if hb.get(i) == db.get(str(n)):
                            hans += str(i)
                        else:
                            continue           
                else:
                    hans += str(n)
                break
        ans = ""
        sr = str(hans)
        l = len(sr)
        for i in range(-1,-(l+1),-1):
            ans = ans + sr[i]
        ans = str(ans)
        print(f"{temp} in Octal is {ans}")

    def Binary_to_Decimal(self):
        n = input("Enter the number : \n")
        l = len(n)
        a = l
        ans = 0
        for i in range(0,l):
            ans = ans + (int(n[i]) * 2**(a-1))
            a -= 1
        print(f"{n} in decimal is {ans}")

    def Binary_to_Octal(self):
        n = input("Enter the no. (it should be only 0 and 1) :\n")
        ans = ""
        temp1 = ""
        for a in n:
            temp1 = temp1 + a
        temp2 = ""
        if len(temp1)%3 == 0:
            pass
        else:
            for c in range(2):
                temp1 = "0" + temp1
                if len(temp1)%3 == 0:
                    break
        for d in range(len(temp1)):
            temp2 = temp2 + temp1[d]
            if len(temp2)%3 == 0:
                for e in ob.keys():
                    if temp2.startswith("0"):
                        temp2 = temp2[-2] + temp2[-1]
                        f = ob.get(e)
                        if f == temp2:
                            ans = ans + e
                    else:
                        f = ob.get(e)
                        if f == temp2:
                            ans = ans + e
                temp2 = ""
        print(f"{n} in Octal is {ans}")

    def Binary_to_Hexadecimal(self):
        n = input("Enter the no. (it should be only 0 and 1) :\n")
        ans = ""
        temp1 = ""
        for a in n:
            temp1 = temp1 + a
        temp2 = ""
        if len(temp1)%4 == 0:
            pass
        else:
            for c in range(3):
                temp1 = "0" + temp1
                if len(temp1)%4 == 0:
                    break
        for d in range(len(temp1)):
            temp2 = temp2 + temp1[d]
            if len(temp2)%4 == 0:
                for e in hb.keys():
                    if temp2 == "0000" or temp2 == "0001" or temp2 == "0010" or temp2 == "0011":
                        temp2 = temp2[-2] + temp2[-1]
                        f = hb.get(e)
                        if f == temp2:
                            ans = a + e
                        else:
                            continue
                        temp2 = ""
                    elif temp2 == "0100" or temp2 == "0101" or temp2 == "0110" or temp2 == "0111":
                        temp2 = temp2[-3] + temp2[-2] + temp2[-1]
                        f = hb.get(e)
                        if f == temp2:
                            ans = ans + e
                        elif len(temp2) == 2:
                            temp2 = temp2[-2] + temp2[-1]
                            f = hb.get(e)
                            if f == temp2:
                                ans = ans + e
                    else:
                        f = hb.get(e)
                        if f == temp2:
                            ans = ans + e
                temp2 = ""
        print(f"{n} in Hexadecimal is {ans}")

    def Octal_to_Decimal(self):
        n = input("Enter the number : \n")
        l = len(n)
        a = l
        ans = 0
        for i in range(0,l):
            ans = ans + (int(n[i]) * 8**(a-1))
            a -= 1
        print(f"{n} in decimal is {ans}")

    def Octal_to_Binary(self):
        n = input("Enter the number : \n")
        ans = ""
        for i in n:
            if i == "0" or i == "1" or i == "2" or i == "3":
                ans = ans + ("0" + hb.get(i))
            else:
                ans = ans + hb.get(i)
        print(f"{n} in Binary is {ans}")

    def Octal_to_Hexadecimal(self):
        n = input("Enter the number : \n")
        hans = ""
        for i in n:
            if i == "0" or i == "1" or i == "2" or i == "3":
                hans = hans + ("0" + hb.get(i))
            else:
                hans = hans + hb.get(i)
        hans = int(hans)
        hans = str(hans)    
        if len(hans)%4 == 0:
            pass
        else:
            for c in range(3):
                hans = "0" + hans
                if len(hans)%4 == 0:
                    break
        temp2 = ""
        ans = ""
        for d in range(len(hans)):
            temp2 = temp2 + hans[d]
            if len(temp2)%4 == 0:
                for e in hb.keys():
                    if temp2 == "0100" or temp2 == "0101" or temp2 == "0110" or temp2 == "0111":
                        temp2 = temp2[-3] + temp2[-2] + temp2[-1]
                        f = hb.get(e)
                        if f == temp2:
                            ans = ans + e
                    elif temp2 == "0000" or temp2 == "0001" or temp2 == "0010" or temp2 == "0011":
                        temp2 = temp2[-2] + temp2[-1]
                        f = hb.get(e)
                        if f == temp2:
                            ans = ans + e
                        else:
                            continue
                        temp2 = ""
                    else:
                        f = hb.get(e)
                        if f == temp2:
                            ans = ans + e
                temp2 = ""
        print(f"{n} in Hexadecimal is {ans}")
            
    def Hexadecimal_to_Decimal(self):
        n = input("Enter the number : \n")
        l = len(n)
        a = l
        hans = 0
        for i in range(0,l):
            if n[i] == "A" or n[i] == "B" or n[i] == "C" or n[i] == "D" or n[i] == "E" or n[i] == "F":
                b = hb.get(n[i])
                for j in db.keys():
                    if db.get(j) == b:
                        hans = hans + (int(j) * 16**(a-1))
                    else:
                        continue
            else:
                hans = hans + (int(n[i]) * 16**(a-1))
            a -= 1
        print(f"{n} in decimal is {hans}")

    def Hexadecimal_to_Binary(self):
        n = input("Enter the number : \n")
        ans = ""
        for i in n:
            if i == "0" or i == "1" or i == "2" or i == "3":
                ans = ans + ("00" + hb.get(i))
            elif i == "4" or i == "5" or i == "6" or i == "7":
                ans = ans + ("0" + hb.get(i))
            else:
                ans = ans + hb.get(i)
        print(f"{n} in Binary is {ans}")

    def Hexadecimal_to_Octal(self):
        n = input("Enter the number : \n")
        hans = ""
        for i in n:
            if i == "0" or i == "1" or i == "2" or i == "3":
                hans = hans + ("00" + hb.get(i))
            elif i == "4" or i == "5" or i == "6" or i == "7":
                hans = hans + ("0" + hb.get(i))
            else:
                hans = hans + hb.get(i)
        ans = ""
        temp1 = hans
        temp2 = ""
        if len(temp1)%3 == 0:
            pass
        else:
            for c in range(2):
                temp1 = "0" + temp1
                if len(temp1)%3 == 0:
                    break
        for d in range(len(temp1)):
            temp2 = temp2 + temp1[d]
            if len(temp2)%3 == 0:
                for e in ob.keys():
                    if temp2.startswith("0"):
                        temp2 = temp2[-2] + temp2[-1]
                        f = ob.get(e)
                        if f == temp2:
                            ans = ans + e
                    else:
                        f = ob.get(e)
                        if f == temp2:
                            ans = ans + e
                temp2 = ""
        print(f"{n} in Binary is {ans}")

    def For_Float(self):
        print("1 : Decimal to Binary\n2 : Decimal to Octal\n3 : Decimal to HexaDecimal\n4 : Binary to Decimal\n5 : Binary to Octal\n6 : Binary to HexaDecimal\n7 : Octal to Decimal\n8 : Octal to Binary\n9 : Octal to HexaDecimal\n10 : Hexadecimal to Decimal\n11 : HexaDecimal to Binary\n12 : HexaDecimal to Octal")
        choice = float(input("Enter your choice (The numeric Value) :\n"))
        if choice == 1:
            value = float(input("Enter number : \n"))
            n = value * 2**8
            n = int(n)
            temp = n
            hans = ""
            d = n//2
            while d != 1:
                d = n//2
                if n%2 != 0:
                    n += 1
                    r = n//2 - d
                    hans = hans + str(r)
                    n = d
                else:
                    r = n//2 - d
                    hans = hans + str(r)
                    n = d
                if d == 1:
                    hans = hans + str(d)
                    ans1 = ""
                    sr = str(hans)
                    l = len(sr)
                    for k in range(-1,-(l+1),-1):
                        ans1 = ans1 + sr[k]
                    ansh1 = ""
                    for i in range(-8,-1,+1):
                        ansh1 += ans1[i]
                    ansh2 = ""
                    for j in range(0,(len(ans1))-8):
                        ansh2 += ans1[j]
                    ans = f"{ansh2}.{ansh1}"
                    print(f"{value} in Binary is {ans}")
                    break
            
        if choice == 2 :
            value = float(input("Enter number : \n"))
            n = value*(8**8)
            n = int(n)
            print(n)
            hans = ""
            d = n//8
            while True:
                d = n//8
                if n % 8 != 0 and n > 16:
                    t = n
                    while t % 8 != 0:
                        t -= 1
                    r = n - t
                    hans += str(r)
                elif n % 8 == 0 and n > 16:
                    hans += "0"
                elif n % 8 != 0 and n > 8 and n < 16:
                    tm = n
                    while tm % 8 != 0:
                        tm -= 1
                    r = n - tm
                    hans += str(r)
                elif n == 8 or n == 16:
                    hans += "01"
                    break
                n = d
                if n == 1 or (n > 1 and n <= 7):
                    hans += str(n)
                    break
            ans1 = ""    
            sr = str(hans)
            l = len(sr)
            for k in range(-1,-(l+1),-1):
                ans1 = ans1 + sr[k]
            ansh1 = ""
            for i in range(-8,-1,+1):
                ansh1 += ans1[i]
            ansh2 = ""
            for j in range(0,(len(ans1))-8):
                ansh2 += ans1[j]
            ans = f"{ansh2}.{ansh1}"
            print(f"{value} in Octal is {ans}")
            
        if choice == 3:
            value = float(input("Enter the number : \n"))
            n = value * (16**8)
            n = int(n)
            hans = ""
            d = n//16
            while True:
                d = n//16
                if n % 16 != 0 and n > 32:
                    t = n
                    while t % 16 != 0:
                        t -= 1
                    r = n - t
                    if r >= 10 and r <= 15:
                        for i in hb.keys():
                            if hb.get(i) == db.get(str(r)):
                                hans += str(i)
                    else:
                        hans += str(r)       
                elif n % 16 == 0 and n > 32:
                    hans += "0"
                elif n % 16 != 0 and n > 16 and n < 32:
                    tm = n
                    while tm % 16 != 0:
                        tm -= 1
                    r = n - tm
                    hans += str(r)
                elif n == 16 or n == 32:
                    hans += "01"
                    break
                n = d
                if n >= 1 and n <= 15:
                    if n >= 10:
                        for i in hb.keys():
                            if hb.get(i) == db.get(str(n)):
                                hans += str(i)
                            else:
                                continue           
                    else:
                        hans += str(n)
                    break
            ans1 = ""
            sr = str(hans)
            l = len(sr)
            for i in range(-1,-(l+1),-1):
                ans1 = ans1 + sr[i]
            ans1 = str(ans1)
            ansh1 = ""
            for i in range(-8,-1,+1):
                ansh1 += ans1[i]
            ansh2 = ""
            for j in range(0,(len(ans1))-8):
                ansh2 += ans1[j]
            ans = f"{ansh2}.{ansh1}"
            print(f"{value} in HexaDecimal is {ans}")

        if choice == 4:
            n = float(input("Enter a number :\n"))
            l = len(str(n))
            hans1 = 0
            temp = int(n)
            temp = str(temp)
            a = b = len(temp)
            for i in range(0,b):
                hans1 += int(temp[i]) * 2**(a-1)
                a -= 1
            hans2 = 0
            temp2 = ""
            p = str(n).find(".")
            for j in range(p+1,l):
                temp2 += str(n)[j]
            temp2 = str(temp2)
            for k in range(0,len(temp2)):
                hans2 += int(temp2[k]) * 2**(-(k+1))
            ans = hans1 + hans2
            print(f"{n} in Decimal is {ans}")

        if choice == 5:
            n = float(input("Enter the no. (it should be only 0 and 1) :\n"))
            t = int(n)
            t = str(t)
            hans3 = ""
            temp1 = ""
            for a in t:
                temp1 = temp1 + a
            temp2 = ""
            if len(temp1)%3 == 0:
                pass
            else:
                for c in range(2):
                    temp1 = "0" + temp1
                    if len(temp1)%3 == 0:
                        break
            for d in range(len(temp1)):
                temp2 = temp2 + temp1[d]
                if len(temp2)%3 == 0:
                    for e in ob.keys():
                        if temp2.startswith("0"):
                            temp2 = temp2[-2] + temp2[-1]
                            f = ob.get(e)
                            if f == temp2:
                                hans3 = hans3 + e
                        else:
                            f = ob.get(e)
                            if f == temp2:
                                hans3 = hans3 + e
                    temp2 = ""

            n = str(n)
            p = n.find(".") 
            hans1 = ""       
            for b in range(p+1,len(n)):
                hans1 = hans1 + n[b]
            hans2 = ""
            if len(hans1)%3 == 0:
                pass
            else:
                for c in range(2):
                    hans1 = hans1 + "0"
                    if len(hans1)%3 == 0:
                        break
            hans4 = ""
            for d in range(len(hans1)):
                hans2 = hans2 + hans1[d]
                if len(hans2)%3 == 0:
                    for e in ob.keys():
                        if hans2.startswith("0"):
                            hans2 = hans2[-2] + hans2[-1]
                            f = ob.get(e)
                            if f == hans2:
                                hans4 = hans4 + e
                        else:
                            f = ob.get(e)
                            if f == hans2:
                                hans4 = hans4 + e
                    hans2 = ""
            
            ans = f"{hans3}.{hans4}"
            print(f"{n} in Octal is {ans}")
        
        if choice == 6:
            n = float(input("Enter the no. (it should be only 0 and 1) :\n"))
            t = int(n)
            t = str(t)
            hans1 = ""
            temp1 = ""
            for a in t:
                temp1 = temp1 + a
            temp2 = ""
            if len(temp1)%4 == 0:
                pass
            else:
                for c in range(3):
                    temp1 = "0" + temp1
                    if len(temp1)%4 == 0:
                        break
            for d in range(len(temp1)):
                temp2 = temp2 + temp1[d]
                if len(temp2)%4 == 0:
                    for e in hb.keys():
                        if temp2 == "0000" or temp2 == "0001" or temp2 == "0010" or temp2 == "0011":
                            temp2 = temp2[-2] + temp2[-1]
                            f = hb.get(e)
                            if f == temp2:
                                hans1 = a + e
                            else:
                                continue
                            temp2 = ""
                        elif temp2 == "0100" or temp2 == "0101" or temp2 == "0110" or temp2 == "0111":
                            temp2 = temp2[-3] + temp2[-2] + temp2[-1]
                            f = hb.get(e)
                            if f == temp2:
                                hans1 = hans1 + e
                            elif len(temp2) == 2:
                                temp2 = temp2[-2] + temp2[-1]
                                f = hb.get(e)
                                if f == temp2:
                                    hans1 = hans1 + e
                        else:
                            f = hb.get(e)
                            if f == temp2:
                                hans1 = hans1 + e
                    temp2 = ""
            n = str(n)
            p = n.find(".")
            temp3 = ""
            for b in range(p+1,len(n)):
                temp3 = temp3 + n[b]
            if len(temp3)%4 == 0:
                pass
            else:
                for c in range(3):
                    temp3 = temp3 + "0"
                    if len(temp3)%4 == 0:
                        break
            temp4 = ""
            hans2 = ""
            for d in range(len(temp3)):
                temp4 = temp4 + temp3[d]
                if len(temp4)%4 == 0:
                    for e in hb.keys():
                        if temp4 == "0000" or temp4 == "0001" or temp4 == "0010" or temp4 == "0011":
                            temp4 = temp4[-2] + temp4[-1]
                            f = hb.get(e)
                            if f == temp4:
                                hans2 = a + e
                            else:
                                continue
                            temp4 = ""
                        elif temp4 == "0100" or temp4 == "0101" or temp4 == "0110" or temp4 == "0111":
                            temp4 = temp4[-3] + temp4[-2] + temp4[-1]
                            f = hb.get(e)
                            if f == temp4:
                                hans2 = hans2 + e
                            elif len(temp4) == 2:
                                temp4 = temp4[-2] + temp4[-1]
                                f = hb.get(e)
                                if f == temp4:
                                    hans2 = hans2 + e
                        else:
                            f = hb.get(e)
                            if f == temp4:
                                hans2 = hans2 + e
                    temp4 = ""
            ans = f"{hans1}.{hans2}"
            print(f"{n} in Hexadecimal is {ans}")

        if choice == 7:
            n = float(input("Enter the number : \n"))
            t = int(n)
            t = str(t)
            l = len(t)
            a = l
            ans = 0
            for i in range(0,l):
                ans = ans + (int(t[i]) * 8**(a-1))
                a -= 1
            temp = ""
            n = str(n)
            p = n.find(".")
            for j in range(p+1,len(n)):
                temp = temp + n[j]
            b = len(temp)
            for k in range(0,b):
                ans += (int(temp[k]) * (8**-(k+1)))
            print(f"{n} in decimal is {ans}")

        if choice == 8:
            n = float(input("Enter the number : \n"))
            t1 = int(n)
            t1 = str(t1)
            hans = ""
            for i in t1:
                if i == "0" or i == "1" or i == "2" or i == "3":
                    hans = hans + ("0" + hb.get(i))
                else:
                    hans = hans + hb.get(i)
            n = str(n)
            p = n.find(".")
            temp = ""
            for j in range(p+1,len(n)):
                temp = temp + n[j]
            hans2 = ""
            for j in temp:
                if j == "0" or j == "1" or j == "2" or j == "3":
                    hans2 = hans2 + ("0" + hb.get(j))
                else:
                    hans2 = hans2 + hb.get(j)
            ans = f"{hans}.{hans2}"            
            print(f"{n} in Binary is {ans}")

        if choice == 9:
            value = float(input("Enter the number : \n"))
            n = int(value)
            n = str(n)
            hans1 = ""
            for i in n:
                if i == "0" or i == "1" or i == "2" or i == "3":
                    hans1 = hans1 + ("0" + hb.get(i))
                else:
                    hans1 = hans1 + hb.get(i)
            hans1 = int(hans1)
            hans1 = str(hans1)    
            if len(hans1)%4 == 0:
                pass
            else:
                for c in range(3):
                    hans1 = "0" + hans1
                    if len(hans1)%4 == 0:
                        break
            temp2 = ""
            ans1 = ""
            for d in range(len(hans1)):
                temp2 = temp2 + hans1[d]
                if len(temp2)%4 == 0:
                    for e in hb.keys():
                        if temp2 == "0100" or temp2 == "0101" or temp2 == "0110" or temp2 == "0111":
                            temp2 = temp2[-3] + temp2[-2] + temp2[-1]
                            f = hb.get(e)
                            if f == temp2:
                                ans1 = ans1 + e
                        elif temp2 == "0000" or temp2 == "0001" or temp2 == "0010" or temp2 == "0011":
                            temp2 = temp2[-2] + temp2[-1]
                            f = hb.get(e)
                            if f == temp2:
                                ans1 = ans1 + e
                            else:
                                continue
                            temp2 = ""
                        else:
                            f = hb.get(e)
                            if f == temp2:
                                ans1 = ans1 + e
                    temp2 = ""

            value = str(value)
            p = value.find(".")
            temp3 = ""
            for a in range(p+1,len(value)):
                temp3 = temp3 + value[a]
            hans2 = ""
            for b in temp3:
                if b == "0" or b == "1" or b == "2" or b == "3":
                    hans2 = hans2 + ("0" + hb.get(b))
                else:
                    hans2 = hans2 + hb.get(b)
            hans2 = str(hans2)
            print(hans2)
            if len(hans2)%4 == 0:
                pass
            else:
                for c in range(3):
                    hans2 = hans2 + "0"
                    if len(hans2)%4 == 0:
                        print(hans2)
                        break
            temp4 = ""
            ans2 = ""
            for d in range(len(hans2)):
                temp4 = temp4 + hans2[d]
                if len(temp4)%4 == 0:
                    for g in hb.keys():
                        if temp4 == "0100" or temp4 == "0101" or temp4 == "0110" or temp4 == "0111":
                            temp4 = temp4[-3] + temp4[-2] + temp4[-1]
                            f = hb.get(g)
                            if f == temp4:
                                ans2 = ans2 + g
                        elif temp4 == "0000" or temp4 == "0001" or temp4 == "0010" or temp4 == "0011":
                            temp4 = temp4[-2] + temp4[-1]
                            f = hb.get(g)
                            if f == temp2:
                                ans2 = ans2 + g
                            else:
                                continue
                            temp4 = ""
                        else:
                            f = hb.get(g)
                            if f == temp4:
                                ans2 = ans2 + g
                    temp4 = ""

            ans = f"{ans1}.{ans2}"
            print(f"{value} in Hexadecimal is {ans}")
        
        if choice == 10:
            value = str(input("Enter the number : \n"))
            o = value.find(".")
            n = ""
            for w in range(0,o):
                n = n + value[w]
            l = len(n)
            a = l
            hans1 = 0
            for i in range(0,l):
                if n[i] == "A" or n[i] == "B" or n[i] == "C" or n[i] == "D" or n[i] == "E" or n[i] == "F":
                    b = hb.get(n[i])
                    for p in db.keys():
                        if db.get(p) == b:
                            hans1 = hans1 + (int(p) * 16**(a-1))
                        else:
                            continue
                else:
                    hans1 = hans1 + (int(n[i]) * 16**(a-1))
                a -= 1
            temp = ""
            k = len(value)
            for t in range(o+1,k):
                temp = temp + value[t]
            q = len(temp)
            hans2 = 0
            for j in range(0,q):
                if temp[j] == "A" or temp[j] == "B" or temp[j] == "C" or temp[j] == "D" or temp[j] == "E" or temp[j] == "F":
                    b = hb.get(temp[j])
                    for y in db.keys():
                        if db.get(y) == b:
                            hans2 = hans2 + (int(y) * 16**(-(j+1)))
                        else:
                            continue
                else:
                    hans2 = hans2 + (int(temp[j]) * 16**(-(j+1)))
            ans = hans1 + hans2
            print(f"{value} in decimal is {ans}")

        if choice == 11: 
            v = input("Enter the number : \n")
            n = ""
            p = v.find(".")
            for j in range(0,p):
                n = n + v[j]
            hans1 = ""
            for i in n:
                if i == "0" or i == "1" or i == "2" or i == "3":
                    hans1 = hans1 + ("00" + hb.get(i))
                elif i == "4" or i == "5" or i == "6" or i == "7":
                    hans1 = hans1 + ("0" + hb.get(i))
                else:
                    hans1 = hans1 + hb.get(i)
            n1 = ""
            for l in range(p+1,len(v)):
                n1 = n1 + v[l]
            hans2 = ""
            for m in n1:
                if m == "0" or m == "1" or m == "2" or m == "3":
                    hans2 = hans2 + ("00" + hb.get(m))
                elif m == "4" or m == "5" or m == "6" or m == "7":
                    hans2 = hans2 + ("0" + hb.get(m))
                else:
                    hans2 = hans2 + hb.get(m)
            ans = f"{hans1}.{hans2}"

            print(f"{v} in Binary is {ans}")

        if choice == 12:
            v = input("Enter the number : \n")
            n = ""
            p = v.find(".")
            for j in range(0,p):
                n = n + v[j]
            hans = ""
            for i in n:
                if i == "0" or i == "1" or i == "2" or i == "3":
                    hans = hans + ("00" + hb.get(i))
                elif i == "4" or i == "5" or i == "6" or i == "7":
                    hans = hans + ("0" + hb.get(i))
                else:
                    hans = hans + hb.get(i)
            ans1 = ""
            temp1 = hans
            temp2 = ""
            if len(temp1)%3 == 0:
                pass
            else:
                for c in range(2):
                    temp1 = "0" + temp1
                    if len(temp1)%3 == 0:
                        break
            for d in range(len(temp1)):
                temp2 = temp2 + temp1[d]
                if len(temp2)%3 == 0:
                    for e in ob.keys():
                        if temp2.startswith("0"):
                            temp2 = temp2[-2] + temp2[-1]
                            f = ob.get(e)
                            if f == temp2:
                                ans1 = ans1 + e
                        else:
                            f = ob.get(e)
                            if f == temp2:
                                ans1 = ans1 + e
                    temp2 = ""
            
            n1 = ""
            for a in range(p+1,len(v)):
                n1 = n1 + v[a]
            hans2 = ""
            for b in n1:
                if b == "0" or b == "1" or b == "2" or b == "3":
                    hans2 = hans2 + ("00" + hb.get(b))
                elif b == "4" or b == "5" or b == "6" or b == "7":
                    hans2 = hans2 + ("0" + hb.get(b))
                else:
                    hans2 = hans2 + hb.get(b)
            ans2 = ""
            temp3 = hans2
            temp4 = ""
            if len(temp3)%3 == 0:
                pass
            else:
                for e in range(2):
                    temp3 = temp3 + "0"
                    if len(temp3)%3 == 0:
                        break
            for f in range(len(temp3)):
                temp4 = temp4 + temp3[f]
                if len(temp4)%3 == 0:
                    for g in ob.keys():
                        if temp4.startswith("0"):
                            temp4 = temp4[-2] + temp4[-1]
                            h = ob.get(g)
                            if h == temp4:
                                ans2 = ans2 + g
                        else:
                            h = ob.get(g)
                            if h == temp4:
                                ans2 = ans2 + g
                    temp4 = ""
            ans = f"{ans1}.{ans2}"           
            print(f"{v} in Octal is {ans}")

Bc = Binary_Converter()
print("1 : Decimal to Binary\n2 : Decimal to Octal\n3 : Decimal to HexaDecimal\n4 : Binary to Decimal\n5 : Binary to Octal\n6 : Binary to HexaDecimal\n7 : Octal to Decimal\n8 : Octal to Binary\n9 : Octal to HexaDecimal\n10 : Hexadecimal to Decimal\n11 : HexaDecimal to Binary\n12 : HexaDecimal to Octal\n13 : For any Float type of value")
choice = int(input("Enter your choice (The numeric Value) :\n"))
options = {
    1 : Bc.Decimal_to_Binary,
    2 : Bc.Decimal_to_Octal,
    3 : Bc.Decimal_to_Hexadecimal,
    4 : Bc.Binary_to_Decimal,
    5 : Bc.Binary_to_Octal,
    6 : Bc.Binary_to_Hexadecimal,
    7 : Bc.Octal_to_Decimal,
    8 : Bc.Octal_to_Binary,
    9 : Bc.Octal_to_Hexadecimal,
    10 : Bc.Hexadecimal_to_Decimal,
    11 : Bc.Hexadecimal_to_Binary,
    12 : Bc.Hexadecimal_to_Octal,
    13 : Bc.For_Float
}

options[choice]()