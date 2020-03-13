import re

# url = "https://www.pexels.com/search/girl/"
#
# driver = webdriver.Chrome()
# driver.get(url)
# # for i in range(1, 2):
# #     js = "var q=document.documentElement.scrollTop=100000"
# #     driver.execute_script(js)
# #     time.sleep(10)
# b = driver.page_source
# # print(driver.page_source)
# # time.sleep(10)
# # driver.save_screenshot("girl.png")
# # time.sleep(2)
# driver.close()
# soup = BeautifulSoup(b, "xml")
# imgs = soup.find_all("img", attrs={"class": "photo-item__img"})
# # for img in imgs:
# #     imga = str(img).split(">")[0].split(" ")[-2]
# #     print(type(imga), imga)
#
#
# """
# <img alt="Woman Sitting on Chair Holding Abook" class="photo-item__img" data-big-src="https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;h=750&amp;w=1260" data-image-height="2048" data-image-width="1365" data-large-src="https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;h=650&amp;w=940" data-tiny-src="https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=1&amp;w=500" data-tiny-srcset="https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=1&amp;w=500 1x, https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;w=500 2x" src="https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=1&amp;w=500" srcset="https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=1&amp;w=500 1x, https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;w=500 2x">
# <div class="badge-container">
# <span class="favorite-badge" data-tooltip="This photo was uploaded by one of the photographers you follow." data-tooltip-align="left">
# <img class="favorite-badge__icon" height="14" src="https://www.pexels.com/assets/favorite-f721c3d387889d5c3a9e0943c1836840a2954b9bebab846ca963877afee48f21.svg" width="14">
# </img>
# <span class="featured-badge" data-tooltip="This photo is featured and can be found through search." data-tooltip-align="left">
# <img class="featured-badge__icon" height="14" src="https://www.pexels.com/assets/star-1bf7ee8c305832829a0a1e0b5c5d901e34e6732cd67c90715cd9b554a785877b.svg" width="14">
# </img>
# </span>
# </span><a class="photo-item__photographer" data-overview-tooltip-initiated="true" data-overview-tooltip-user-id="112747" href="/@hyentrag123" style="cursor: pointer;"><img class="photo-item__avatar" data-overview-tooltip-pointer-element="true" height="30" src="https://www.gravatar.com/avatar/89216fec1e5bee385eefab0edf77a344?s=60&amp;d=mm" width="30">
# <span class="photo-item__name">Huyen Trang Nguyen</span>
# </img><a download="true" href="/photo/889096/download/"/>
# <div class="photo-item__info">
# <button class="js-like js-like-889096 rd__button rd__button--like rd__button--no-padding rd__button--text-white rd__button--with-icon" data-initialized="true" data-photo-id="889096">
# <i class="rd__button--like--not-active--icon rd__svg-icon"><svg height="24" viewBox="0 0 24 24" width="24" xmlns:="http://www.w3.org/2000/svg"><path d="M16.5 3c-1.74 0-3.41.81-4.5 2.09C10.91 3.81 9.24 3 7.5 3 4.42 3 2 5.42 2 8.5c0 3.78 3.4 6.86 8.55 11.54L12 21.35l1.45-1.32C18.6 15.36 22 12.28 22 8.5 22 5.42 19.58 3 16.5 3zm-4.4 15.55l-.1.1-.1-.1C7.14 14.24 4 11.39 4 8.5 4 6.5 5.5 5 7.5 5c1.54 0 3.04.99 3.57 2.36h1.87C13.46 5.99 14.96 5 16.5 5c2 0 3.5 1.5 3.5 3.5 0 2.89-3.14 5.74-7.9 10.05z"/></svg>
# </i>
# <i class="rd__button--like--active--icon rd__svg-icon" style="display: none"><svg height="24" viewBox="0 0 24 24" width="24" xmlns:="http://www.w3.org/2000/svg"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
# </i>
# </button>
# <button class="js-collect js-collect-889096 rd__button rd__button--collect rd__button--no-padding rd__button--text-white rd__button--with-icon" data-initialized="true" data-photo-id="889096">
# <i class="rd__button--collect--not-active--icon rd__svg-icon"><svg height="24" viewBox="0 0 24 24" width="24" xmlns:="http://www.w3.org/2000/svg"><path d="M13 7h-2v4H7v2h4v4h2v-4h4v-2h-4V7zm-1-5C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/></svg>
# </i>
# <i class="rd__button--collect--active--icon rd__svg-icon" style="display: none"><svg height="24" viewBox="0 0 24 24" width="24" xmlns:="http://www.w3.org/2000/svg"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
# </i>
# </button>
# </div>
# </a>
# </div></img>
# """
# img_lists = []
# for img_list in imgs:
#     img_2 = re.findall("^<img .* srcset=(.*)>", str(img_list))
#     img_1 = str(img_2).strip("[(' srcset=')").strip("')]").strip('"').split(", ").split("/")[4]
#     img_lists.append(img_1)
# print(img_lists, len(img_lists))

img_list = '<img alt="Woman Sitting on Chair Holding Abook" class="photo-item__img" data-big-src="https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;h=750&amp;w=1260" data-image-height="2048" data-image-width="1365" data-large-src="https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;h=650&amp;w=940" data-tiny-src="https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=1&amp;w=500" data-tiny-srcset="https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=1&amp;w=500 1x, https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;w=500 2x" src="https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=1&amp;w=500" srcset="https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=1&amp;w=500 1x, https://images.pexels.com/photos/889096/pexels-photo-889096.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;w=500 2x">'
img = re.findall("<img .* srcset=(.*)>", str(img_list))
img = str(img).strip("[(' srcset=')").strip("')]").strip('"').split(", ")[0].split("/")[4]
print(img, len(img))