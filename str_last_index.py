def last_index_of(org_str, sub_str): 
    last_idx = -1
    for i in range(len(org_str)):
        f = False
        for j in range(len(sub_str)):
            if (i+j) < len(org_str) and sub_str[j] == org_str[i]:
                f = True
                if sub_str[j] != org_str[i+j]:
                    f = False
                    break
        if f == True:
            last_idx = i;
    return last_idx
    
def main():
    org_str = "Hello World,Hello Reader!"
    sub_str = "Hello"
    print("Last index of {0} in {1} is: {2}".format(sub_str,org_str,last_index_of(org_str,sub_str)))

if __name__ == "__main__":
    main()

