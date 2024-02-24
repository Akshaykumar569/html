# # # d={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# # # def get__winner():
# # # 	if d['1']==d['2']==d['3']=='x'or d['4']==d['5']==d['6']=='x'or d['7']==d['8']==d['9']=='x'or d['1']==d['4']==d['7']=='x'or d['2']==d['5']==d['8']=='x'or d['3']==d['6']==d['9']=='x':
# # # 		return 'p1 winner'
# # # 	elif d['1']==d['2']==d['3']=='o'or d['4']==d['5']==d['6']=='o'or d['7']==d['8']==d['9']=='o'or d['1']==d['4']==d['7']=='o'or d['2']==d['5']==d['8']=='o'or d['3']==d['6']==d['9']=='o':
# # # 		return 'p2 winner'
# # # 	else:
# # # 		a=d.values()
# # # 		for i in a:
# # # 			if type(int)!=(str):
# # # 				return 'none'
# # # 		print(a('tie...'))
# # # def get__akshay():
# # # 	print(d['1'],d['2'],d['3'])
# # # 	print(d['4'],d['5'],d['6'])
# # # 	print(d['7'],d['8'],d['9'])
# # # get__akshay()	
# # # while True:
# # # 	p1=input('enter the player1:')
# # # 	d[p1]='x'
# # # 	get__akshay()
# # # 	get__winner()

# # # 	p2=input('enter the player2:')
# # # 	d[p2]='o'
# # # 	get__akshay()
# # # 	get__winner()

# # '''s='welcom to python'
# # d=list(s)
# # print(d)
# # d.split()
# # print(d)''' 
# # # d=[1,3,3,4,6,7,85,9,78,465,335,3,2,4,]
# # # for i in d:
# # # 	s=d.count(i)
# # # 	if s>1:
# # # 		d.remove(i)
# # # print(d)
# # # nums = [0,1,0,3,12]------>(7)

# # # for i in nums:
# # # 	if i==0:
# # # 		nums.remove(i)
# # # 		nums.append(i)
# # # print(nums)

# # # a = [1,2,3,2]
# # # b=[]
# # # for i in a:
# # #     if i not in a:
# # #         a.append(i)
# # # print(a)
# # # num=[1,2,3,[4,5],6,[7,8,9,10]]
# # # name=[]
# # # for i in num:
# # # 	if isinstance(i,int):
# # # 		name.append(i)
# # # 	else:
# # # 		name.extend(i)
# # # print(name)
# # l=[1,2,3,4,5,6,7,8,9,10]
# # lis=[]
# # for i in l:
# # 	if i%2==0:
# # 		lis.append(f'{i} is even')
		
# # 	else:
# # 		lis.append(f'{i} is odd')
# # print(lis)
		

# # gani=[1,2,3]


# # if 3 not in gani:
# # 	print(True)
# # else:
# # 	print(False)


# # a = 10
# # print(isinstance(a, int))

# # print(True if type(a)==int else False)
		
# data = ["Akshay", "Kumar", "Harish", "Ganesh"]	
# # print "They are available in the list" if Akshay and Harish exists in the list using ternary operator
# print(True if 'Akshay'and 'Haris' in data else False)
		
# l = [1,2,3,4,5,6,7,8,9,10]

# print([x for x in l if x%2==0]) #list comprehension

# name = ''
# name = None
# print(not name)
# print(name is not None)
# print(name)
# l=[1,2,3,4,5,6,7,8,9,10]
# s=l[0]
# for i in l:
# 	if i<s:
# 		s=i
# print(s)
l=[1,2,3,4,5,6,7,8,9,10,11,12,52]
s=0
for i in l:
	s=s+1
print(s)












  		