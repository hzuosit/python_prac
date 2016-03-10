import sys,ast,profile,random
##Frist we have merge sort in iteration version
def merge_sort(l):
		if len(l)<=1:
				return l
		mid = len(l)/2
		left = merge_sort(l[:mid])
		right = merge_sort(l[mid:])
		return merge(left,right)

def merge(left,right):
		if not left:
				return right
		if not right:
				return left
		if left[0]<right[0]:
				return [left[0]] + merge(left[1:],right)
		return [right[0]] + merge(right[1:],left)

##Then we have merge sort recursive version
def MergeSort(l):
		if len(l)<=1:
				return l
		elif len(l)>1:
				mid = len(l)/2
				left = MergeSort(l[:mid])
				right = MergeSort(l[mid:])
				i = 0
				j = 0
				k = 0
				while i<len(left) and  j<len(right):
						if left[i]<right[j]:
								l[k] = left[i]
								i = i+1
						else:
								l[k] = right[j]
								j = j+1
						k = k+1
				while i<len(left):
						l[k] = left[i]
						i = i+1
						k = k+1
				while j<len(right):
						l[k] = right[j]
						j = j+1
						k = k+1
		return l
		        
def main():
		args = sys.argv[1:]
		try:
				a = ast.literal_eval(args[1])
				if args[0] == '--recursion':
						print  merge_sort(a)
				elif args[0] == '--iteration':
						print MergeSort(a)
		except:
				print 'Usage [--iteration] --recursion list'
if __name__ == '__main__':
		profile.run('main')
		main()
