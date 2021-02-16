from event_manager import EventManager

def facade_main():

    print("Client: I want to have a big party for my wife's birthday.\n")


    em = EventManager()
    em.arrange()



if __name__ == "__main__":
    facade_main()
