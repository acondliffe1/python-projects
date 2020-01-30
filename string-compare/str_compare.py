def str_compare(S, T):

    def replace_with_q(string):
        output = ""
        number = ""
        for char in string:
            if not char.isdigit():
                if len(number) != 0:
                    output += '?' * int(number)
                    number = ""
                output += char
            else:
                number += char
                # replace at this point onwa
        return output

    S = replace_with_q(S)
    T = replace_with_q(T)

    print(S, T)

    if len(S) != len(T):
        return False

    for s, t in zip(S, T):
        if (s == '?' or t == '?') or s == t:
            continue
        else:
            return False
    return True
