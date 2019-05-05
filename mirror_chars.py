def getMirrorAlphabet(c):
    chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    mirrs="ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"
    idx=0
    for ch in chars:
        if ch == c:
            return mirrs[idx]
        idx+=1

def getMirrorStr(s,n):
    if n > len(s):
        print("Input number should be less than string length")
        return s
    prefix=s[0:n-1]
    suffix=s[n-1:]
    mirror=""
    for c in suffix:
        mirror += getMirrorAlphabet(c)
    return prefix+mirror

print(getMirrorStr("AxbpQEmyZ",5))
