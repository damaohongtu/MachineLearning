import math
from nltk.metrics import distance
def ComputeEuclideanDistance(x1,y1,x2,y2):
    d=math.sqrt(math.pow((x1-x2), 2)+math.pow((y1-y2),2))
    return d
print ComputeEuclideanDistance(3, 104, 18, 90)