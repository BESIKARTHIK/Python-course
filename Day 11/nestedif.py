data = {
    'karthik':{'status':True,'python':80,'mysql':80},
    'Tarun':{'status':True,'python':90,'mysql':90},
    'Akhila':{'status': True,'python': 85, 'mysql': 85}
}
name = input("Enter the name: ")
if name in data:
    if data[name]['status']:
        sum = data[name]['python'] + data[name]['mysql']
        avg = sum/2
        print(f"Hello {name}")
        print(f"your average scoreis {avg}")
        if avg>80:
            print("you performance is good in exam ")
        elif avg>70:
            print("your perfomance need to impove")
        else:
            print("you are failed in exam")
    else:
        print(f"{name} did not attend the exam")
else:
    print("name is not found in data")