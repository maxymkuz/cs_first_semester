a = 11
b = 11
# print(id(b))

a = [1, 2, 3, 4, 5]
result = ""
string = "87.65.4321"
while len(string) > 1:
    result += string[3:5] + "/"
    string = string[1:-1:2]
    print(result, string)
