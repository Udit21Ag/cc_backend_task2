from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create your views here.

def scraping(request):
    gpus={}
    driver=webdriver.Chrome()
    
    driver.get("https://www.nvidia.com/en-in/geforce/buy/")
    try:
        elements = driver.find_elements(By.CLASS_NAME,"nv-container")[1:11]
        for elem in elements:
            name=elem.find_elements(By.CLASS_NAME,"nv-title")[0].text
            try:
                price=elem.find_elements(By.CLASS_NAME,"nv-title")[1].text
                p=price.lstrip("Starting at Rs. ")
                d=int(p.replace(",",""))
                
            except:
                d="N/A"
            gpus[name]=d
    finally:
        driver.quit()
    
    response = JsonResponse(gpus)
    response["Access-Control-Allow-Origin"] = "http://localhost:8080"  
    return response