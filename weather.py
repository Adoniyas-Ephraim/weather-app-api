import requests
import pygame
import time as t
import sys

pygame.init()

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "city": response.get("city"),
    }
    return location_data['city']


location = (get_location())

api_key = '30d4741c779ba94c470ca1f63045390a'

def data(): 
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        print("No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])

        print(f"\nThe weather in {location} is: {weather}")
        print(f"\nThe temperature in {location} is: {temp}ºF\n")




    #DISPLAY IT ON THE SCREEN
    X = 612
    Y = 408

    scrn = pygame.display.set_mode((X, Y))


    pygame.display.set_caption(f'{weather}')

    if weather == 'Clear':
        imp = pygame.image.load("/Users/10309067/Desktop/test/weather/clear.png").convert()
    elif weather == 'Rain' or weather =='Drizzle':
        imp = pygame.image.load("/Users/10309067/Desktop/test/weather/rain.png").convert()
    elif weather == 'Drizzle':
        imp = pygame.image.load("/Users/10309067/Desktop/test/weather/rain.png").convert()
    elif weather == 'Clouds':
        imp = pygame.image.load("/Users/10309067/Desktop/test/weather/cloud.png").convert()
    elif weather == 'Thunderstorm':
        imp = pygame.image.load("/Users/10309067/Desktop/test/weather/tunderstorm.png").convert()
    elif weather == 'Snow':
        imp = pygame.image.load("/Users/10309067/Desktop/test/weather/snow.png").convert()
    elif weather == 'Mist' or weather =='Smoke' or weather =='Haze' or weather =='Dust' or weather =='Fog' or weather =='Sand' or weather =='Dust' or weather =='Ash' or weather =='Squall':
        imp = pygame.image.load("/Users/10309067/Desktop/test/weather/mist.png").convert()
    elif weather == 'Tornado':
        imp = pygame.image.load("/Users/10309067/Desktop/test/weather/tornado.png").convert()
    else:
        imp = pygame.image.load("/Users/10309067/Desktop/test/weather/clear.png").convert()

    scrn.blit(imp, (0, 1))

    pygame.display.flip()

    green = (0, 255, 0)
    blue = (0, 0, 128)

    font = pygame.font.Font('freesansbold.ttf', 32)
    degree = font.render(f'{temp}ºF', True, green, blue)
    degreeRect = degree.get_rect()
    degreeRect.center = (X-50, Y-30)

    font2 = pygame.font.Font('freesansbold.ttf', 22)
    loc = font2.render(f'{location}', True, blue, green)
    locRect = loc.get_rect()
    locRect.center = (X//2-250, Y-32)

    status = True
    while (status):
        scrn.blit(degree, degreeRect)
        scrn.blit(loc, locRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                data()

        pygame.display.update()

    pygame.quit()

data()