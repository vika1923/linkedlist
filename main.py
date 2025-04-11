# int, string, float, boolean
from linkedlist import linkedlist

elem3 = linkedlist(data=3, tail=None)
elem2 = linkedlist(data=2, tail=elem3)
elem1 = linkedlist(data=1, tail=elem2)

elem1.getat(2)
