"""
	https://dmoj.ca/problem/ccc06s3
"""
import sys; input = sys.stdin.readline

inp = list(map(int, input().split()))
a,b = [inp[0],inp[1]],[inp[2],inp[3]]
flip = False

if b[0] == a[0]:  #reflects the graph if the gradient is infinite
    flip = True
    m0 = 0
else:
    m0 = (b[1]-a[1])/(b[0]-a[0])
c0 = a[1]-(m0*a[0])

#y=mx+c
counter = 0

def infiniteFix(p0,p1): # handles the case where m1 is infinite
    y = m0*p1[0]+c0
    if y <= max(p0[1],p1[1]) and y >= min(p0[1],p1[1]):
        return True
    return False

for times in range(int(input())):
    inp = list(map(int, input().split()))
    length = inp[0];del inp[0]
    intersection = False
    for i in range(length):
        p0,p1 = [inp[i*2],inp[i*2+1]],[inp[(i*2+2)%(2*length)],inp[(i*2+3)%(2*length)]]

        if flip:
            p0[0],p0[1] = p0[1],p0[0]
            p1[0],p1[1] = p1[1],p1[0]

        if p1[0] != p0[0]:
            m1 = (p1[1]-p0[1])/(p1[0]-p0[0])
        else:
            intersection = infiniteFix(p0,p1)
            if intersection: break
            else: continue
        
        c1 = p0[1]-(m1*p0[0])

        if m1 == m0:
            continue
        """
            y0 = m0x0+c0
            y1 = m1x1+c1
            when finding the point of intersection y0 = y1 and x0 = x1
            therefore, m0x0+c0 = m1x1+c1
            x(m0-m1) = c1-c0
            x=(c1-c0)/(m0-m1)
        """
        
        x = (c1-c0)/(m0-m1)
        #x is where the lines intersect if infinite, checks if the intersection is contained in both line segments
        if (x <= max(a[0],b[0]) and x >= min(a[0],b[0]) and x <= max(p0[0],p1[0]) and x >= min(p0[0],p1[0])):
           intersection = True
           break
        
    if intersection:
        counter += 1
        
print(counter)
