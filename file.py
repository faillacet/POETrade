# FILE STUFF
def updateFiles(typeList, priceDict):
    # Create Files
    index = 0
    for type in typeList:
        # Create Files
        file = open((type + ".txt"), "w")

        # Populate Files
        for item in priceDict[type]:
            if (type == "Currency" or type == "Fragment"):
                file.write(item['currencyTypeName'] + ": " + str(item['chaosEquivalent']) + "\n")
            else:
                file.write(item['name'] + ": " + str(item['chaosValue']) + " --- " + str(item['divineValue']) + "\n")

        # Close File + Incriment Counter
        file.close()
        index = index + 1