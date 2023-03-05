# defining a method to calculate asc, desc and none type of sorting
def sort_list(input_string, option):
    if option == "asc":
        return sorted(input_string)
    elif option == "desc":
        return sorted(input_string, reverse=True)
    else:
        return input_string


# print section where the above logic  is implemented
print("This is a programt to sort the given input")
input_string = input("Enter the string to be sorted: ")
# input_list = list(input_string)
option = input("Enter the method of sort (example - asc, desc, none): ")
if option == "asc":
    print(sort_list(input_string, "asc"))
elif option == "desc":
    print(sort_list(input_string, "desc"))
else:
    print(input_string)


# def asc_sort(self):
#     asc_sort = input_string.sort
#     print(asc_sort)


# def desc_sort(self):

    # desc_sort = input_string.sort
    # desc_sort = desc_sort.reverse()
    # print(desc_sort)
