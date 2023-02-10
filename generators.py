class topten:
    def __init__(self):
        self.num= 1

    def __iter__(self):
       # ask doubt- self.num=4
        return self
    def __next__(self):
        val=self.num
        if self.num<=10:


            self.num+=1
            return  val
        else:
             raise StopIteration

values= topten()
val=values.__iter__()

print (next(values))
print (next(values))
print (next(values))
for i in values:
    print(i)
'''
1.double underscore method are initializeed automatically
2.return self will return its object itself
3.if not next method is specified programm shows
 class  'topten' object is not an itertor'''


class int:
    def __init__(self):
        pass
    def __iter__(self):
        return self
    def __next__(self):
        pass
ba=int()
#ab=iter(ba)
print(next(ba))