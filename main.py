def calculate(weight,height):
   bmi = weight / (height ** 2)
   return bmi


def interpret(bmi):
      if bmi < 16:
         print("You are Severely underweight")
      elif bmi < 18.5:
         print("You are Underweight")
      elif bmi < 25:
         print("You are Normal (healthy weight)")
      elif bmi < 30:
         print("You are Overweight")
      elif bmi < 35:
         print("You are Moderately obese")
      else:
         print("You are Severely obese")


def main():
   while True:
     try:
        print("BMI Calculator! Find Your Health range")
        print("Enter your weight in kg")
        weight=float(input())
        print("Enter your Height in m")
        height=float(input())
     except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
        return

     if weight <= 0 or height <= 0 or weight > 500 or height > 3:
        print("Invalid input. Weight and height must be positive values within reasonable ranges.")
        return
     bmi = calculate(weight, height)
     print(f"Your BMI is: {bmi:.2f}")
     interpretation = interpret(bmi)
     print(interpretation)
     
     repeat = input("Do you want to calculate BMI again? (yes/no): ").lower()
     if repeat != "yes":
         break

if __name__ == "__main__":
    main()
