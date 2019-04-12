#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

from math import sqrt

class Matrix:

    @staticmethod
    def check_number_of_arguments(number_of_arguments):
        if not sqrt(number_of_arguments).is_integer():
	        raise Error ("Wrong size of array")

    def __init__(self, *list_passsed):
        self.number_of_arguments = len(list_passsed)
        Matrix.check_number_of_arguments(self.number_of_arguments)
        self.dimention = int(sqrt(self.number_of_arguments))
        self.elements = [ [] for i in range(self.dimention)] 
        for i in range(self.dimention):
            self.elements[i] = [j for j in list_passsed[i * self.dimention : (i+1) * self.dimention]]

    def add(self, matrix_to_add):
        temp = []
        for i in range(self.dimention):
            for j in range(self.dimention):
                temp.append(self.elements[i][j] + matrix_to_add.elements[i][j])
        return Matrix(*temp)

    
def main():
    matrix_1 = Matrix(4,5,6,7)
    print(matrix_1.elements)
    matrix_2 = Matrix(2,2,2,1)
    print(matrix_2.elements)
    matrix_3 = matrix_2.add(matrix_1)
    print(matrix_3.elements)

if __name__ == "__main__":
    main()