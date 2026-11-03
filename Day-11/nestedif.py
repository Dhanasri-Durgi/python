data={
    'praveen':{'status':True,'python':96,'mysql':95,'fastapi':93},
    'krishna':{'status':True,'python':86,'mysql':75,'fastapi':73},
    'eswar':{'status':True,'python':56,'mysql':65,'fastapi':63},
    'surya':{'status':True,'python':46,'mysql':45,'fastapi':43},
    'raghu':{'status':True,'python':26,'mysql':25,'fastapi':33},
    'abdul':{'status':False,'python':None,'mysql':None,'fastapi':None}, 

}

name=input("Enter the name:")

if name in data:
    if data[name]['status']:
        total=data[name]['python']+data[name]['mysql']+data[name]['fastapi']
        avg=total/3
        if avg>80:
            print(f"{name}, congrats you got the first grade")
        elif avg>60:
            print(f"{name}, good! work hard to get the first grade")
        elif avg>40:
            print(f"{name},better luck next time, work hard")
        elif avg>=35:
            print(f"{name},you are just passed, but need to work hard")
        else:
            print(f"{name},you are failed, work hard to pass next time")
    else:
        print(f"{name}, did not attend the exam, so no marks are available")

else:
    print(f"{name} is not found in the data")    