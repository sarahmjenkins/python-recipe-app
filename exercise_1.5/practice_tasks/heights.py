class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
    
    def __str__(self):
        output = str(self.feet) + ' feet, ' + str(self.inches) + ' inches'
        return output
    
    def __sub__(self, other):
        height_a_inches = self.feet*12 + self.inches
        height_b_inches = other.feet*12 + other.inches

        height_difference_inches = height_a_inches - height_b_inches

        output_feet = height_difference_inches // 12
        output_inches = height_difference_inches % 12

        return Height(output_feet, output_inches)

person_a = Height(5, 10)
person_b = Height(3, 9)
height_difference = person_a - person_b

print('Height difference:', height_difference)
