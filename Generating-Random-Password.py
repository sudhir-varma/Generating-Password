import random 

cap_let="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_let="abcdefghijklmnopqrstuvwxyz"
num="0123456789"
sym="!@#$%^&*(){}[]/*-+"

string=cap_let+small_let+num+sym
string_len=16

password="".join(random.sample(string,string_len))

print(password)
