#GEARING UP FOR DESTRUCTION
def answer(ls):
        if len(ls) < 2:
                return [-1, -1]
	ls2=[ls[i+1]-ls[i] for i in range(len(ls)-1)]
	su,val=0,1
	for i in reversed(ls2):
		su+=val*i

		val*=-1
	if(len(ls2)%2==0):
		x=-2*su
		if x>=1:
			return [x,1]
		return [-1,-1]
	else:
		x=2*su
		if x>=3:
			if x%3==0:
				return [int(x/3),1]
			else:
				return [int(x),3]
		return [-1,-1]
