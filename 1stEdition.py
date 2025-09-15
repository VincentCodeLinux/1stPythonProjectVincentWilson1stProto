numb_credits = int(input("How many credits are you currently taking?"))
numb_credits_prev_semester = int(input("How many credits did you take before the semester started?"))
total_credits_to_grad = 120
credits_taken = int(numb_credits + numb_credits_prev_semester)
major = input("What is your major?")
credits_to_go = total_credits_to_grad - credits_taken
print(f"your major is {major} and you have {credits_to_go} to go until you can graduate")