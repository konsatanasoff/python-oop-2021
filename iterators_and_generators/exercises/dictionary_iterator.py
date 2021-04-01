class dictionary_iter:
    def __init__(self, dict_object):
        self.dict_object = dict_object
        self.keys = list(self.dict_object)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dict_object):
            raise StopIteration
        key = self.keys[self.index]
        value = self.dict_object[key]
        self.index += 1
        return key, value


# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
