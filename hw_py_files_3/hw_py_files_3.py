result = {}
with open('1.txt','r', encoding = 'utf-8') as f:
    res = f.readlines()
    result['1.txt'] = ['1.txt','\n',str(len(res)),'\n'] + res + ['\n']
with open('2.txt','r', encoding = 'utf-8') as f:
    res = f.readlines()
    result['2.txt'] = ['2.txt','\n',str(len(res)),'\n'] + res + ['\n']
with open('3.txt','r', encoding = 'utf-8') as f:
    res = f.readlines()
    result['3.txt'] = ['3.txt','\n',str(len(res)),'\n'] + res + ['\n']
result = sorted(result.values(), key=lambda x:x[2], reverse=True)

with open ('final.txt','a', encoding = 'utf-8') as f:
    for file in result:
        for string in file:
            f.write(string)
