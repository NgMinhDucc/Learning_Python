# Given a string of characters that range from 'a' to 'z' and numbers that range from 0 to 9.
# Return the smallest number appears in the string.
# For example: S = 12ab34cd56 -> Output: 12 (since 12 is the smallest number among [12, 34, 56]).

test = int(input())
for _ in range(test):
    s = input()
    cur = ""
    minn = None
    
    for ch in s:
        if ch.isdigit():
            cur += ch
        else:
            if cur: # this line means if cur has any value other than "" (a truthy value)
                val = int(cur)
                minn = val if minn is None else min(minn, val)
                cur = ""
            
    if cur:
        val = int(cur)
        minn = val if minn is None else min(minn, val)
        
    print(minn)