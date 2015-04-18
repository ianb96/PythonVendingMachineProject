
def singleMove(source, dest, diskNum):
	print("Disk "+str(diskNum)+" moved from "+str(source)+" to "+str(dest))

def multiMove(source, dest, numDisks):
	if numDisks==0:
		return
	if source==1:
		if dest==2:
			other=3
		elif dest==3:
			other=2
	elif source==2:
		if dest==1:
			other=3
		elif dest==3:
			other=1
	elif source==3:
		if dest==1:
			other=2
		elif dest==2:
			other=1

	multiMove(source,other,numDisks-1)
	singleMove(source,dest, numDisks)
	multiMove(other,dest,numDisks-1)

def main():
	diskNum=int(input("how many discs are there? "))
	multiMove(1,2,diskNum)

main()
