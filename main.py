# # s = input()
# # print('Hello' + s + '!');
# a, b, c = input().split()
# a, b, c = int(a), int (b), int (c)
# a, b, c = map(int, input().split())
a = list(map(int, input().split()))
print(a)
for x in a:
    if x%2 ==0:
        print(x)