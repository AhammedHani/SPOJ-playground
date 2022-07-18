def room(value, last_index):
    result = int(value) / int(last_index)
    if int(value) % int(last_index) != 0:
        result = int(value) // int(last_index)
        result = result + 1
        return result
    else:
        return int(result)


N = int(input())
values = []
for i in range(N):
    value = ((input()).split())
    values.append(value)

for i in values:
    last_index = i[-1]
    Boy = room(i[0], last_index)
    girl = room(i[1], last_index)
    print(int(Boy) + int(girl))