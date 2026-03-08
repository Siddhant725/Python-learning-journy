test_scores=[45,88,62,95,30]
total=0
for h in test_scores:
    if h>=70:
        print(f"pass")
    else:
        print(f"fail")
        
for g in test_scores:
    total=g+total
    
average=total/len(test_scores)
print(f"average score: {average}")