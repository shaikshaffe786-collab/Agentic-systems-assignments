class StudentScores:
    def __init__(self, scores):
        self.scores = scores

    def highest_last_two(self):
        try:
            highest = max(self.scores[-1], self.scores[-2])
            print(f"Highest score among last two is: {highest}")
        except IndexError:
            print("Not enough scores to find highest value")

# Run it
scores = [ 45, 67, 89, 72]
student = StudentScores(scores)
student.highest_last_two()

#With error handling
# class StudentScores:
#     def __init__(self, scores):
#         self.scores = scores

#     def highest_last_two(self):
#         try:
#             highest = max(self.scores[-1], self.scores[-2])
#             print(f"Highest score among last two is: {highest}")
#         except IndexError:
#             print("Not enough scores to find highest value")

# # Run it
# scores = [72]
# student = StudentScores(scores)
# student.highest_last_two()