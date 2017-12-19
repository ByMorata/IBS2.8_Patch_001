index_00 = 1
index_01 = 2

print(index_00 / index_01)
print(index_00 // index_01)

g_00 = (index_00 * index_00 for index_00 in range(0, 10) if index_00 % 2 == 0)
for index_01 in g_00:
    print(index_01)

def get_good_abs(index_00, index_02):
    print(index_02(index_00))

index_03 = abs
index_04 = -4
index_05 = -10
get_good_abs(index_04, index_03)

list_00 = [-12, 1231, 41, 231, -1, 0]

# list_01 = sorted(list_00, key=abs)

def app(index_00):
    if index_00 == 0:
        index_00 = 1000
        print("Hello World!")
        return 1000
    return index_00

list_02 = sorted(list_00, key=app)
print(list_02)
