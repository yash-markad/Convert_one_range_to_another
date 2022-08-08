OldMax = 32512
OldMin = 0
NewMax =1025
NewMin = 0

OldValue = 10

OldRange = (OldMax - OldMin)  
NewRange = (NewMax - NewMin)  

NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
