scores = []

for i in range(1,6):
    scores.append(int(input('enter test score: ' + str(i) + ': ')))
    
def determine_grade(score):
    if score > 89 and score < 101:
        return 'A'
    elif score > 79 and score < 90:
        return 'B'
    elif score > 69 and score < 80:
        return 'C'
    elif score > 59 and score < 70:
        return 'D'
    elif score < 60:
        return 'F'
for score in scores:
    print(determine_grade(score))  

def calc_avarage(scores):
    totaal = 0
    for score in scores:
        totaal += score
    avarage = totaal/5
    return avarage
print(calc_avarage(scores))
