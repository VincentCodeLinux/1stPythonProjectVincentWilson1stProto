numb_credits = input("How many credits are you currently taking?")
numb_credits_prev_semester = input("How many credits did you take before the semester started?")
total_credits_to_grad = 120
credits_taken = numb_credits + numb_credits_prev_semester
major = 'cybersecurity'
credits_to_go = int(total_credits_to_grad - credits_taken)
print("your major is", {major}, "and you have", {credits_to_go}, "to go untill you can graduate" )