from bisect import bisect

grades=[0,21,41,61,91,100]
grade=int(input('Enter grade: '))

print(bisect(grades,grade))