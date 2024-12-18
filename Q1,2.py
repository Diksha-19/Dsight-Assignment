
Q1. def combine_lists(L1, L2):
   
    if len(L1) != len(L2):
        raise ValueError("Lists must have the same length")
 
    
    L3 = []

    
    for i in range(len(L1)):
        
        combined_element = {
            "tuple": L1[i],
            "string": L2[i]
        }

      L3.append(combined_element)

    return L3
 #test case to check
L1 = [(2, 3), (4, 5), (6, 7), (90, 91)]
L2 = ["a", "b", "c", "d"]
result = combine_lists(L1, L2)
print(result)

Q2.def reverse_dictionary(input_dict):

    output_dict = {}
    for key, value in input_dict.items():
        string, integer = value
        output_dict[string] = (key, integer)

    return output_dict

#test case to check
input_dict = {"a": (23, "X"), "b": (24, "Y"), "c": (89, "Z")}
output_dict = reverse_dictionary(input_dict)
print(output_dict)  # Output: {'X': ('a', 23), 'Y': ('b', 24), 'Z': ('c', 89)}