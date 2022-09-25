from captcha.image import ImageCaptcha

def generate_captcha(text): 
    image = ImageCaptcha(width = 280, height = 90)
    
    # Image captcha text
    captcha_text = text 
    
    # generate the image of the given text
    data = image.generate(captcha_text) 
    
    # write the image on the given file and save it
    image.write(captcha_text, 'CAPTCHA.png')

if __name__=="__main__":
    text = "hello world"
    generate_captcha(text)