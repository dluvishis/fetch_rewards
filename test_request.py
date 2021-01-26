import requests


#use word1 and word2

def post_data():
    url = "http://127.0.0.1:1234/main_findScore"
    word1="The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
    word2="easiest way "
   

    payload = {'word1': word1, 'word2': word2}
    response = requests.post(url, data=payload)

    return response.json()

def main():
    result = post_data()
    print(result)


if __name__ == "__main__":
    main()