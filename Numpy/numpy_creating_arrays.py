import numpy as np

numbers_list_array =np.array([10,20,30,40,50])
print(numbers_list_array)
print(type(numbers_list_array))

#tuple
number_tuple_array =np.array((10,20,30,40,50))
print(number_tuple_array)

#0-d
student_scores_array =np.array(99)
print(student_scores_array)

#1-d
student_scores_array =np.array((80,85,90,95,100))
print(student_scores_array)

#2-D array
matrix_table_array=np.array([[1,2,3,],[4,5,6,]])
print(matrix_table_array)

print(matrix_table_array.shape)

#3-D array
cube_data_array=np.array([[[1,2,3,],[4,5,6,]],
                             [[7,8,9,],[10,11,12,]]])
print(cube_data_array)




