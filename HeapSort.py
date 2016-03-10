def heapify(alist,i,n):
		l = 2*i
		r = 2*i + 1
		if alist[l]>alist[i]:
				largest = l
		else:
				largest = i
		if alist[r] > alist[i]:
				largest = r
		if largest != i:
				alist[largest],alist[i] = alist[i],alist[largest]
		heapify(alist,largest,n)

def Build_heap(alist):
		n = len(alist)-1
		for i in range(n/2,0,-1):
				heapify(alist,i,n)

def heap_sort(alist):
		Build_heap(alist)
		h_size = len(alist)-1
		for i in range(h_size,1,-1):
				alist[i],alist[1] = alist[1],alist[i]
				h_size -=1
				heapify(alist,1,h_size)

def main():
		l = [9,8,7,6,5,4,3,23,2,1]
		print heap_sort(l)

if __name__ == '__main__':
		main()
