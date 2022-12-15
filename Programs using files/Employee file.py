
# Employee file
employees = ['1)EId:10','2)EName:john','3)ESalary:100k','4)EAddress:Laos']
with open('a.txt','w') as f:
    for employee in employees:
        f.write(employee)
        f.write('\n')