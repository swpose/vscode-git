dic_lower = 'abcdefghijklmnopqrstuvwxyz'
dic_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
input_data = raw_input("input your data : ")
n  = int(raw_input("input your number : "))

result = ""

for i in range(len(input_data)):
    if input_data[i] in dic_lower:
        position = dic_lower.find(input_data[i])
        result += dic_lower[position + n]

    if input_data[i] in dic_upper:
        position = dic_upper.find(input_data[i])
        result += dic_upper[position + n]

print "result is : {}".format(result)
