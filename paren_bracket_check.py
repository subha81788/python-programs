def check_parenthesis_balance(str):
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    stack = []

    for i in str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            # find corresponding open element
            open_element = open_list[pos]

            # open element is at the top of stack
            if len(stack) > 0 and stack[len(stack)-1] == open_element:
                stack.pop()
            else:
                return "unbalanced"
                break
    if len(stack) == 0:
        return "balanced"

def main():
    expression = "{[]{()}}"
    print("{0} is {1}".format(expression,check_parenthesis_balance(expression)))

    expression = "[{}{})(]"
    print("{0} is {1}".format(expression,check_parenthesis_balance(expression)))

if __name__ == "__main__":
    main()
