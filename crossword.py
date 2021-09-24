a = input()
b = input()
c = int(input())
if len(a) > len(b):
	if len(b + a) == c:
		print(b + a)
	if len(b + a) != c:
		print("False")
else:
	if len(a + b) == c:
		print(a + b)
	if len(a + b) != c:
		print("False")
