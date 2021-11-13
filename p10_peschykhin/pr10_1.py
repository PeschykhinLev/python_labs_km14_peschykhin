salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]

print(list(map(lambda x: round(x+(x*0.3),2), salary_list)))
print(list(map(lambda x: round((x*0.3),2), salary_list)))
