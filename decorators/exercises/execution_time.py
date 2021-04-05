from timeit import default_timer as dt


def exec_time(func):
    def wrapper(*args):
        start_time = dt()
        func(*args)
        end = dt() - start_time
        return end
    return wrapper


# @exec_time
# def loop(start, end):
#     total = 0
#     for x in range(start, end):
#         total += x
#     return total
#
#
# print(loop(1, 10000000))
#
#
# @exec_time
# def concatenate(strings):
#     result = ""
#     for string in strings:
#         result += string
#     return result
#
#
# print(concatenate(["a" for i in range(1000000)]))
