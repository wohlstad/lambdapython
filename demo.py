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