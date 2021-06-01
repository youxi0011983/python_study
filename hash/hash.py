# coding:utf-8
# hash()


# print(hash(1))
# print(hash(1.0))    # 相同的数值，不同类型，哈希值是一样的
# print(hash("abc"))
# print(hash("hello world"))

# filename = 'jdk-8u144-windows-x64.exe'
filename = '12.txt'
with open(filename, "rb") as f:
    value = f.read(8096)
    # value = f.readline()
    # while True:
    #     value = f.read(8096)
    #     if not value:
    #         break


print(value)