import api

def printMenu():
    print("\n1.Get state-wise information" +
    "\n2.Get district-wise information" +
    "\n3.Show states \n4.Show districts" +
    "\n5.Exit")

def printCases():
    print("\n1.Confirmed cases" +
    "\n2.Active cases" +
    "\n3.Recovered" +
    "\n4.Deaths"
    )

def main():
    cont = True
    while cont:

        print("\nHi! This is a COVID-19 information app that answers your queries")
        print("What would you like to know?")
        printMenu()
        choice = input("\nChoose your option: ")

        try:
            choice = int(choice)
        except:
            print("Invalid input")

        if (choice == 5):
            cont = False
        elif (choice == 1):
            state = input("\nEnter state: ")
            if api.isState(state):
                printCases()
                cases = int(input("\nChoose: "))

                if (cases == 1):
                    type = "confirmed"
                    num = api.getConfirmed(state)
                elif (cases == 2):
                    type = "active"
                    num = api.getActive(state)
                elif (cases == 3):
                    type = "recovered"
                    num = api.getRecovered(state)
                elif (cases == 4):
                    type = "dead"
                    num = api.getDeaths(state)

                print("\nThe number of {} cases in {} is {}".format(type,state,num))
            else:
                print("Invalid input")
        elif (choice == 2):
            state = input("\nEnter state: ")
            if api.isState(state):
                district = input("Enter district: ")
                if api.isDistrict(state, district):
                    printCases()
                    cases = int(input("\nChoose: "))

                    if (cases == 1):
                        type = "confirmed"
                        num = api.getConfirmed(state,district)
                    elif (cases == 2):
                        type = "active"
                        num = api.getActive(state,district)
                    elif (cases == 3):
                        type = "recovered"
                        num = api.getRecovered(state,district)
                    elif (cases == 4):
                        type = "dead"
                        num = api.getDeaths(state,district)

                    print("The number of {} cases in {} in {} is {}".format(type,district,state,num))
                else:
                    print("Invalid input")
            else:
                print("Invalid input")
        elif (choice == 3):
            print("")
            api.printStates()
        elif (choice == 4):
            state = input("\nEnter state: ")
            if api.isState(state):
                print("")
                api.printDistricts(state)
            else:
                print("Invalid input")

if __name__ == "__main__":
    main()
