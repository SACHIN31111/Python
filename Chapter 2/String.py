#String is a sequence of character enclosed within the quotes
# we can write string in 3 ways in python 
a="Crore"
b='Crore'
c='''Crore'''
print(a,b,c)  #String is immutable

name="NAME"
nameShort=name[1]
print(nameShort)


# String Slicing
name2=name[1:3]  #string[strat_idx:ending_idx]
print(name2)

#negative Slicing
# Name=[S  A  D   D   D]
#      -5 -4  -3  -2  -1
print(name[-3:-1])

# Slicing with skip value
name3="Aamazing"
                     # [strat : end : skipped _value]
print(name3[1:6:2])  #$nmae3[1 :  6  : 2 ]


