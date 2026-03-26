from PIL import Image, ImageFilter   
kitten = Image.open("scraping\kitten.jpg") 
blurryKitten = kitten.filter(ImageFilter.GaussianBlur) 
blurryKitten.save('kitten_blurred.jpg')
blurryKitten.show()