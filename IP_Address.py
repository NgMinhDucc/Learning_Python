# Given a list of strings, check whether each string is a valid IPv4 address.
#
# Input:
# - The first line contains an integer T, the number of test cases.
# - The next T lines each contain a string of arbitrary characters, with length less than 1000.
#
# Output: Print the result for each test case on a separate line.
# For example:
# Input:
# 2
# 192.168.1.1
# 256.255.255.255
# Output:
# YES
# NO

def check_IP(ip):
    arr = ip.split(".")
    
    if len(arr) != 4:
        return "NO"
    for i in arr:
        if i == "":
            return "NO"
        if not i.isdigit():
            return "NO"
        if int(i) < 0 or int(i) > 255:
            return "NO"
    return "YES"

for test in range(int(input())):
    ip = input()
    print(check_IP(ip))