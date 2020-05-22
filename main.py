import api, os, time

def printMenu():
    print("\n1.Get country information" +
    "\n2.Get state-wise information" +
    "\n3.Get district-wise information" +
    "\n4.Show states \n5.Show districts" +
    "\n6.Exit")

def main():
    cont = True
    while cont:
        os.system('cls')
        print("Hi! This is a COVID-19 information app")
        print("What would you like to know?")
        printMenu()
        choice = input("\nChoose option: ")

        try:
            choice = int(choice)
        except:
            print("Invalid input")
            pass

        if (choice == 6):
            cont = False

        elif (choice == 1):
            print("\nIndia has {} confirmed cases".format(api.getAllConfirmed()))
            print("India has {} active cases".format(api.getAllActive()))
            print("India has {} recovered cases".format(api.getAllRecovered()))
            print("India has {} deaths".format(api.getAllDeaths()))

        elif (choice == 2):
            state = input("\nEnter state: ").capitalize()

            if api.isState(state):
                print("\n{} has {} confirmed cases".format(state, api.getConfirmed(state)))
                print("{} has {} active cases".format(state, api.getActive(state)))
                print("{} has {} recovered cases".format(state, api.getRecovered(state)))
                print("{} has {} deaths".format(state, api.getDeaths(state)))
                print("\n{} has conducted {} tests".format(state, api.getTests(state)))

            else:
                print("Invalid input")

        elif (choice == 3):
            state = input("\nEnter state: ").capitalize()

            if api.isState(state):
                district = input("Enter district: ").capitalize()

                if api.isDistrict(state, district):
                    print("\n{}, {} has {} confirmed cases".format(district, state, api.getConfirmed(state,district)))
                    print("{}, {} has {} active cases".format(district, state, api.getActive(state,district)))
                    print("{}, {} has {} recovered cases".format(district, state, api.getRecovered(state,district)))
                    print("{}, {} has {} deaths".format(district, state, api.getDeaths(state,district)))
                    print("{}, {} is a {} zone".format(district,state,api.getZone(district)))
                else:
                    print("Invalid input")

            else:
                print("Invalid input")

        elif (choice == 4):
            print("")
            api.printStates()

        elif (choice == 5):
            state = input("\nEnter state: ")

            if api.isState(state):
                print("")
                api.printDistricts(state)

            else:
                print("Invalid input")

        if cont:
            input("\nPress enter to restart\n")

if __name__ == "__main__":
    main()
