class Counter:
    def __init__(self, max_number = None):
        self.var = 0
        self.max_number = max_number

    def __iter__(self):
        self.var = 0
        return self

    def __next__(self):
        self.var += 1
        def symbol(text):
            var = "1"
            while True:
                text1 = str(text)+var
                yield text1
                if len(text1) > 10:
                    return
                var = str(var)+"1"
        ok = symbol("1")
        print(ok)
        
        for _ in ok:
            print(_)
        if self.var > self.max_number:
            raise StopIteration
        return self.var


count = Counter(10)
for elem in count:
    print(elem)