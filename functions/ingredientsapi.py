import requests
import xml.etree.ElementTree as ET

url = 'http://apis.data.go.kr/1390802/AgriFood/FdFood/getKoreanFoodFdFoodList'
myKey = 'APIkey'
response = input("음식 이름 입력(한글):")
params ={'serviceKey' : myKey, 'service_Type' : 'xml', 'Page_No' : '1', 'Page_Size' : '20', 'food_Name' : response}

ingredients_response = requests.get(url, params=params)

xml_data = ingredients_response.content
root = ET.fromstring(xml_data)

result_msg_element = root.find('.//result_Msg')

if result_msg_element is None or result_msg_element.text == '요청 데이터 없음':
  print("No information")
else:
  item = root.find('body/items').findall('item')[0]
  food_List = item.find('food_List').findall('food')
  
  ingredients = ""
  
  for food in food_List:
    fd_Eng_Nm = food.find('fd_Eng_Nm').text
    ingredient = fd_Eng_Nm.split(',')[0]
  
  
    if ingredients == "":
      ingredients = ingredient
    else :
      ingredients = ingredients +  ", " + ingredient
  
  print(f"Ingredients of {dish_name} are "+ingredients)
