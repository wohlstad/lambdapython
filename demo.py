#-------- boolean logic

TRUE = lambda x : lambda y : x
FALSE = lambda x : lambda y : y

NOT = lambda x : x(FALSE)(TRUE)
OR = lambda x : lambda y : x(x)(y)
AND = lambda x : lambda y : x(y)(x)
EQ = lambda x : lambda y : x(y)(NOT(y))
XOR = lambda x : lambda y : NOT(EQ(x)(y))


#-------- boolean logic demo

BOOLS = [TRUE, FALSE]
def bool2Str(b):
    return b("T")("F")
    
print("boolean logic demo:")
print("---")
for b in BOOLS:
    print(bool2Str(b))

print("---")
for b1 in BOOLS:
    not_b1 = NOT(b1)
    print("NOT " + bool2Str(b1) + " == " + bool2Str(not_b1))


print("---")
for b1 in BOOLS:
    for b2 in BOOLS:
        b1_and_b2 = AND(b1)(b2);
        print(bool2Str(b1) + " AND " + bool2Str(b2) + " == " + bool2Str(b1_and_b2))

print("---")
for b1 in BOOLS:
    for b2 in BOOLS:
        b1_or_b2 = OR(b1)(b2);
        print(bool2Str(b1) + " OR " + bool2Str(b2) + " == " + bool2Str(b1_or_b2))

print("---")
for b1 in BOOLS:
    for b2 in BOOLS:
        b1_eq_b2 = EQ(b1)(b2);
        print(bool2Str(b1) + " EQ " + bool2Str(b2) + " == " + bool2Str(b1_eq_b2))

print("---")
for b1 in BOOLS:
    for b2 in BOOLS:
        b1_xor_b2 = XOR(b1)(b2);
        print(bool2Str(b1) + " XOR " + bool2Str(b2) + " == " + bool2Str(b1_xor_b2))        


#-------- numbers

ZERO = lambda f : lambda x : x
#ONE = lambda f : lambda x : f(x)
#TWO = lambda f : lambda x : f(f(x))
SUCC = lambda n : lambda f : lambda x : f(n(f)(x))
ONE = SUCC(ZERO)
TWO = SUCC(ONE)
THREE = SUCC(TWO)
FOUR = SUCC(THREE)

NUMBERS = [ZERO]
for i in range(10):
    last = NUMBERS[len(NUMBERS)-1]
    NUMBERS.append(SUCC(last))

ADD = lambda n : lambda m : n(SUCC)(m);
MUL = lambda n : lambda m : lambda f : lambda x : n(m(f))(x)
#POW = lambda n : lambda m : lambda f: lambda x : (m(n))(f)(x)
POW = lambda n : lambda m : m(n)

#-------- numbers demo

num2Int = lambda n : n(lambda x : x+1)(0)
num2Str = lambda n : str(num2Int(n))

print("\n")
print("numbers demo:")
print("---")

print(num2Str(ONE))
print(num2Str(TWO))
print(num2Str(THREE))
print(num2Str(FOUR))
numbersStr = ""
for n in NUMBERS:
    numbersStr = numbersStr + num2Str(n) + ", "
print(numbersStr)
print("---") 
n1 = NUMBERS[3]
n2 = NUMBERS[4]
print(num2Str(n1) + " + " + num2Str(n2) + " == " + num2Str(ADD(n1)(n2))); 
print(num2Str(n1) + " * " + num2Str(n2) + " == " + num2Str(MUL(n1)(n2))); 
print(num2Str(n1) + " ^ " + num2Str(n2) + " == " + num2Str(POW(n1)(n2))); 
print("---") 

