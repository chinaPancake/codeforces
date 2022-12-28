s = str(input())

def is_magic(s_input):
    for i in range(len(s_input)):
        if s_input[0] != '1' and s_input[i] != '4':
            return False

    if (s_input[0] == '4'):
        return False

    if '444' in s_input:
        return False
    
    if any(s in s_input for s in ('0','2','3','5','6','7','8','9')):
        return False

    return True

ans = is_magic(s_input=s)
if ans == True:
    print('YES')
else:
    print('NO')


