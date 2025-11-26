def convert(seconds):

    hours = seconds // 60 // 60
    minutes = (seconds % 3600) // 60
    second = (time % seconds) % 60 

    print(f"{hours, minutes, second}")
    
seconds = int(input("Please enter the time to be converted, in sec: "))
convert(seconds)

