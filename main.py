import api

def printMenu():
    print("\n1.Get country information" +
    "\n2.Get state-wise information" +
    "\n3.Get district-wise information" +
    "\n4.Show states \n5.Show districts" +
    "\n6.Exit")

def main():
    cont = True
    while cont:
        print("\nHi! This is a COVID-19 information app that answers your queries")
        print("What would you like to know?")
        printMenu()
        choice = int(input("\nChoose option: "))

        if (choice == 6):
            cont = False

        elif (choice == 1):
            print("\nIndia has {} confirmed cases".format(api.getAllConfirmed()))
            print("\nIndia has {} active cases".format(api.getAllActive()))
            print("\nIndia has {} recovered cases".format(api.getAllRecovered()))
            print("\nIndia has {} deaths".format(api.getAllDeaths()))

        elif (choice == 2):
            state = input("\nEnter state: ")

            if api.isState(state):
                print("\n{} has {} confirmed cases".format(state, api.getAllConfirmed()))
                print("\n{} has {} active cases".format(state, api.getAllActive()))
                print("\n{} has {} recovered cases".format(state, api.getAllRecovered()))
                print("\n{} has {} deaths".format(state, api.getAllDeaths()))

            else:
                print("Invalid input")

        elif (choice == 3):
            state = input("\nEnter state: ")

            if api.isState(state):
                district = input("Enter district: ")

                if api.isDistrict(state, district):
                    print("\n{}, {} has {} confirmed cases".format(district, state, api.getAllConfirmed()))
                    print("\n{}, {} has {} active cases".format(district, state, api.getAllActive()))
                    print("\n{}, {} has {} recovered cases".format(district, state, api.getAllRecovered()))
                    print("\n{}, {} has {} deaths".format(district, state, api.getAllDeaths()))

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

if __name__ == "__main__":
    main()
