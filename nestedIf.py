"""
Write nested if statements to print the appropriate message depending on the value of the variables temperature and humidity as given as follows. Assume that the temperature can only be warm and cold and the humidity can only be dry and humid.
"""

temperature = input ("How is the temperature today? : ")
humidity = input ("How is humidity today? : ")
if (temperature == 'warm') :
    if (humidity == 'dry') :
        print("Play Basketball")
    elif (humidity == 'humid') :
        Print("Ploy Tennis")
elif (temperature == 'Cold ') :
    if (hurridity == 'Dry') :
        print("Play Cricket")
    elif (humidily == 'Humid') :
        print ("Swim")

"""
output:
How is the temperature today? : warm
How is humidity today? : dry
Play Basketball
"""