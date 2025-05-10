Clients = {"123456" : ["Ammar Eid",5000],
"132546" : ["Ahmed Nour",10000],
"129783" : ["Abdullah Mohammed",7000],
"369147" : ["Alaa Yousef",70000],
"147825" : ["Habiba Ayman",6500]}

Password = (input("Please, Enter your password\n"))

if Password == "123456" or Password == "132546" or Password == "129783" or Password == "369147" or Password == "147825":
   print("Hello", Clients[Password][0])
else:
    quit()


print("Please, Choose the appropriate language")
print("1- Arabic                                         2- English\n")

try:
    language = int(input("Enter '1' or '2' to choose the language\n"))
except ValueError:
    print("Please, Enter just 1 or 2")

if language == 1:
    print("1- سحب                                 2- أيداع                                 3- استعلام")
    Service = int(input("من فضلك أختر ما تريد\n"))

    if Service == 1:
        Amount = int(input("من فضلك أدخل المبلغ الذي تربد سحبه علما أنه لا يمكن سحب مبلغ أقل من 50 جنية\n"))
        if (Amount % 50) == 0 and ((Clients[Password][1]) >= Amount):
            New = (Clients[Password][1]) - Amount
            Clients[Password][1] = New
            print("رصيدك الحالي " + str(Clients[Password][1]) + " جنية مصري")
            quit()
        elif (Clients[Password][1]) <= Amount:
            print("عفوا ليس لديك رصيد كافي")
            quit()
        else:
            print("عفوا لا يمكن سحب غير الخمسين ومضاعفاتها")
            quit()

    elif Service == 2:
        Amount2 = int(input("من فضلك أدخل المبلغ الذي تربد ايداعه علما أنه لا يمكن ايداع مبلغ أقل من 50 جنية\n"))
        if Amount2 > 50:
            New2 = (Clients[Password][1]) + Amount2
            Clients[Password][1] = New2
            print("رصيدك الحالي " + str(Clients[Password][1]) + " جنية مصري")
            quit()
        else:
            quit("عفوا لا يمكن ايداع مبلغ أقل من 50 جنية")
            quit()
    elif Service == 3:
        print(("رصيدك الحالي " + str(Clients[Password][1]) + " جنية مصري"))
        quit()
    elif Service > 3:
        print("عفوا اختيار خاطئ")
        quit()

elif language == 2:
    print("1- withdraw                                 2-Deposit                                3-Balance inquiry ")
    Service = int(input("Please, Choose the appropriate service\n"))

    if Service == 1:
        Amount = int(input("Please enter the amount you want to withdraw, noting that it is not possible to withdraw an amount less than 50 pounds\n"))
        if (Amount % 50) == 0 and ((Clients[Password][1]) >= Amount):
            New = (Clients[Password][1]) - Amount
            Clients[Password][1] = New
            print("your current balance is " + str(Clients[Password][1]) + "EGP")
            quit()
        elif (Clients[Password][1]) < Amount:
            print("Sorry, You have not enough money")
            quit()
        else:
            print("Sorry, only fifty and its multiples can be withdrawn")
            quit()

    elif Service == 2:
        Amount2 = int(input("Please enter the amount you want to deposit, noting that it is not possible to deposit an amount less than 50 pounds\n"))
        if Amount2 > 50:
            New2 = (Clients[Password][1]) + Amount2
            Clients[Password][1] = New2
            print("your current balance is " + str(Clients[Password][1]) + "EGP")
            quit()
        else:
            quit("Sorry, it is not possible to deposit an amount less than 50 pounds")
            quit()
    elif Service == 3:
        print(("your current budget is " + str(Clients[Password][1]) + "EGP"))
        quit()
    elif Service > 3:
        print("Wrong answer")
        quit()

