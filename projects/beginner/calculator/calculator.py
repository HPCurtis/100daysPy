from calculatorart import calc_logo
from utility import *

def main():
    while True:
        #Print the Calculator ASCI art.
        print(calc_logo())
        num1, op, num2 = user_input()
        result, result_string = operator_eval(num1, op, num2)
        print(result_string)
        cont = continue_f(result)
        
        # While loop  to loop continue the calculation.
        while True:
            if cont == 'y':
                op = pick_an_operator()
                nn = next_num()
                result, result_string = operator_eval(result, op, nn)

                # Print the result of thec calculation.
                print(result_string)
                cont = continue_f(result)
            elif cont == 'n':
                clear_screen()
                break

if __name__ == "__main__":
    main()