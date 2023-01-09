import requests
from fragments import allSets

# API STUFF
def getAllPrices(typeList, priceDict):
    for type in typeList:
        if (type == "Currency" or type == "Fragment"):
            baseURL = 'https://poe.ninja/api/data/currencyoverview?league=Sanctum&type='
            postURL = '&language=en'
            fullURL = baseURL + type + postURL
        else:
            baseURL = 'https://poe.ninja/api/data/itemoverview?league=Sanctum&type='
            postURL = '&language=en'
            fullURL = baseURL + type + postURL

        response = requests.get(fullURL)
        data = response.json()

        key = type
        value = data['lines']
        priceDict[key] = value



def main():
    typeList = ['Currency', 'Fragment', 'DivinationCard']
    priceDict = {}
    getAllPrices(typeList, priceDict)

    for set in allSets:
        allSets[set].calculateAll(priceDict['Fragment'], priceDict['Currency'])
 
    print("Estimated Profit from purchasing sets and selling in Bulk:")
    for set in allSets:
        print(set + ": " + str(allSets[set].profit))


    

# RUN PROGRAM ON STARTUP
if __name__ == "__main__":
    main()
