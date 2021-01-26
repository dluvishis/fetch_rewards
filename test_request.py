import requests


#use word1 and word2

def post_data():
    url = "http://127.0.0.1:1234/main_findScore"
    
    word1="The easiest way to earn points with Fetch Rewards is to just shop for the products you have already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
    word2="The easiest way to earn points with Fetch Rewards is to just shop for the items you've already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
   

    payload = {'word1': word1, 'word2': word2}
    response = requests.post(url, data=payload)

    return response.json()

def main():
    result = post_data()
    print(result)


if __name__ == "__main__":
    main()