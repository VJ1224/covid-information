import api, os, time, msvcrt

def printMenu():
    print("\n1.Get total information" +
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
        print("\nChoose option:")
        choice = msvcrt.getch()

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
                print("\n{} has {} confirmed cases".format(state, api.getStateConfirmed(state)))
                print("{} has {} active cases".format(state, api.getStateActive(state)))
                print("{} has {} recovered cases".format(state, api.getStateRecovered(state)))
                print("{} has {} deaths".format(state, api.getStateDeaths(state)))
                print("\n{} has conducted {} tests".format(state, api.getStateTests(state)))

            else:
                print("Invalid input")

        elif (choice == 3):
            state = input("\nEnter state: ").capitalize()

            if api.isState(state):
                district = input("Enter district: ").capitalize()

                if api.isDistrict(state, district):
                    print("\n{}, {} has {} confirmed cases".format(district, state, api.getDistrictConfirmed(state,district)))
                    print("{}, {} has {} active cases".format(district, state, api.getDistrictActive(state,district)))
                    print("{}, {} has {} recovered cases".format(district, state, api.getDistrictRecovered(state,district)))
                    print("{}, {} has {} deaths".format(district, state, api.getDistrictDeaths(state,district)))
                    print("\n{}, {} is a {} zone".format(district,state,api.getDistrictZone(district)))
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
