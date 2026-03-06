# Given a list of topics and the questions belonging to each topic in an English exam question bank.
#
# The questions of each topic are separated by a blank line.
# Each question is written on a separate line.
#
# Your task is to count the number of questions for each topic.
# The order of topics in the output must remain the same as their order of appearance in the input.
#
# Input:
# - The first line contains the total number of input lines.
# - The following lines contain the list of topics and their questions.
#
# Output:
# - Print the statistics (number of questions) for each topic as required.

# For example:
#     Input:
#         9
#         Home/accommodation
#         What kind of housing/accommodation do you live in?
#         Who do you live with?
#         How long have you lived there?
        
#         Study
#         Describe your education
#         What is your area of specialization?
#         Why did you choose to study that major?
#     Output:
#         Home/accommodation: 3
#         Study: 3

line = int(input())
di = {}
a = []
for i in range(line):
    x = input()
    if x.strip() != "":
        a.append(x);
    else:
        di[a[0]] = len(a) - 1
        a.clear()
di[a[0]] = len(a) - 1

for k, v in di.items():
    print(f"{k}: {v}")