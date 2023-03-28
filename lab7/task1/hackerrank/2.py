#Task
#Given an integer, n , and  space-separated 
#integers as input, create a tuple, t , of those  integers. Then compute and print the result of hash(t)
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(integer_list))