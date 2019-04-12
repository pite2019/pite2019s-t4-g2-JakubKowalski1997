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