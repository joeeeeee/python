# 写文件
# f = open('./test.txt', 'w')
# f.write('test')
# f.close()
# 读文件
# f = open('./test.txt')
# content = f.readlines()
# print(type(content))
# print(content)

# 读文件
oldFileName = input('请输入需要复制的文件：\n')
oldFile = open(oldFileName, 'r')
if oldFile:
    # 分割点
    split = oldFileName.rfind('.')
    # 后缀名
    extension = oldFileName[split:]
    # 新建文件名
    newFileName = oldFileName[:split] + '_copy' + extension
    # 新建文件
    newFile = open(newFileName, 'w')
    # 读文件
    content = oldFile.readlines()
    # 写文件
    for i in content:
        newFile.write(i)
    # 关闭文件
    newFile.close()
    oldFile.close()

    print('success')





