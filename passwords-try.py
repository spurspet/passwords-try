# 输入密码的程序

password = 'a123456'
j = 3
while j >= 0:
    pwd = input('请输入密码： ')
    j = j - 1
    if pwd != password:
        if j > 0:
            print('密码输错，还有 %d 次机会' %(j))
        else:
            print('输入次数已满')
            break
    elif pwd == password:
        print('密码输入正确')
        break