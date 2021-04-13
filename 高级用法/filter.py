list_x = [1,0,1,0,1,0]

#filter的lambda表达式返回的一定是能表达True或False的值，表达True的则保留
r = filter(lambda x: True if x == 1 else False,list_x)
print(list(r))