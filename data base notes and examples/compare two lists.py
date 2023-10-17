a = [1, 1, 2, 3, 5, 8, 13, 30, 55]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 13]

print(set(a) & set(b))


mylist = [1, 1, 2, 3, 5, 8, 13, 21, 21, 55, 21]
unique = set(mylist)
print(unique)



def isPalindrome(s):
    if s.lower() == s[::-1].lower():
        print("Yes")
    else:
        print ("No")

s = "Nitin"
result = isPalindrome(s)


mylist = [2,3,1,22,1]
result = [i for i, x in enumerate(mylist) if x == 1]
print(result)

a = ['a', 'b', 'a', 'aaa', 1, 2, 1, 1]


class CheckCount(object):

    def __init__(self, data_list):
        self.data_list = data_list

    def get_count_keys(self):
        count_dict = {}
        for i in self.data_list:
            if i not in count_dict:
                count_dict[i] = 0
            count_dict[i] = count_dict[i] + 1
        return count_dict

    @staticmethod
    def print_count_values(count_dict):
        for key in count_dict:
            print(key, " - ", count_dict.get(key))


chk_count = CheckCount(a)
new_dict = chk_count.get_count_keys()
chk_count.print_count_values(new_dict)
