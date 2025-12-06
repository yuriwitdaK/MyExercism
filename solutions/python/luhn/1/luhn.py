class Luhn:
    def __init__(self, card_num):
        self.clean_number = card_num.replace(" ", "") #cleans up number

    def valid(self):
        if len(self.clean_number) <= 1: # if less than 1  false
            return False
        if not self.clean_number.isdigit(): #if not a number false
            return False

        digits = [int(d) for d in self.clean_number]#turn value into int number
        digits.reverse() #reverse

        for i in range(1, len(digits), 2):# start stop step
            digits[i] *= 2  # multiply with 2
            if digits[i] > 9: #if greater than 9
                digits[i] -= 9 #substract 9

        return sum(digits) % 10 == 0 # divide by 10 evenly