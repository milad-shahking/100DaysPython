student_scores = [120,36,52,145,28,185,145,126,16,189,195,85,79,125,84,35,173,94,92,45,159,85]

tolal_exam_score = sum(student_scores)
print(tolal_exam_score)

# _____________ OR

sum = 0
for score in student_scores:
    sum = sum + score
print(f'sum score for function of for loop {sum}')

#================

print(max(student_scores))

# ____________ OR

max_score = 0

for scoreMax in student_scores:
    if scoreMax > max_score:
        max_score = scoreMax


print(max_score)
