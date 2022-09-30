
name = input ("enter ur Name")
email =  input ("enter ur email")
mobile =  input ("enter ur Mobile")
city =  input ("enter City")

# nested if-else
if len(name)> 1:
    if '@' in email and len(email) > 11:
        if len(mobile) == 10 and mobile.isnumeric():
            if city in ['lucknow', 'delhi', 'Noida']:
                print("Your data is  saved , Thankyou") 
            else:
               print("We are not available in ur city") 
        else:
            print("Invalid mobile number⚠") 
    else:
        print("Invalid email address") 
else:
    print("Ye kaisa name h ❓ ") 
                                                             




