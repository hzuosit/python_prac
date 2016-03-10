def QuickSort(l):
		if len(l)>2:
				i = 1;j =-1
				pivot = l[0] 
				temp = []
				while l[i]>pivot and l[j]<pivot and i-j > len(l):
						temp = l[i]
						l[i] = l[j]
						l[j] = temp
						i = i+1
						j = j-1
				left = l[:j]
				right = l[1+j:]
				QuickSort(left)
				QuickSort(right)
				return l


def main():
		l = [5,4,3,2,1]
		print QuickSort(l)

if __name__ == '__main__':
		main()
