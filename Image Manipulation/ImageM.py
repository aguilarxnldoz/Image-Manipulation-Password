 
from pickle import APPENDS
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import os

def make_mod():
    while True:
        print('images: duke, hyena, jalenG, kfriedrice, mannyp, militaryblue, mob, sejinming, wtkobe or xqc.')
        picture = input("Select an image to modify: ")
        showing = Image.open(picture + ".jpeg")
        showing.show()
        confirm = input("Confirm Image?: ").lower()
        if confirm == "yes":
            break

        elif confirm == 'no':
            print('Select Wisely.')
        
        else:
            print('Invalid Option.')
            make_mod()


    print("mods: png, rotate, resize, shade, blurry, or smooth")
    mod = input("Select a modification: ")

    if mod == "png":
        image1 = Image.open(picture +".jpeg")
        image1.save('png pics/'+picture+'.png')
        image1.show()
        make_mod()
            

    elif mod == "rotate":
        spin = int(input("The Image shall be rotated by how many degrees?(90,180,270): "))
        if spin == 90 or spin == 180 or spin == 270:
            image = Image.open(picture +".jpeg")
            image.rotate(spin).save('rotate pics/'+picture +'_rotated.jpeg')
            image_r = Image.open('rotate pics/' +picture +'_rotated.jpeg')
            image_r.show()
            make_mod()
        else:
            print('Invalid Option')
            make_mod()

    elif mod == "resize":
        x = int(input('Enter a width.(200, 400, 600.): '))
        y = int(input('Enter a length.(200, 400, 600.): '))
        if x != 200 or x != 400 or x != 600 and y != 200 or y != 400 or y != 600:
            print('Invalid Option')
            make_mod()

        else:
            image1 = Image.open(picture+'.jpeg')
            image1.resize((x,y)).save('resize pics/' + picture+'_resize.jpeg')
            image_s = Image.open('resize pics/' + picture+'_resize.jpeg')
            image_s.show()
            make_mod()
    
    elif mod == 'shade':
        image1 = Image.open(picture+'.jpeg')
        image1.convert('1').save('bw pics/' + picture+'_bw.jpeg')
        image_bw = Image.open('bw pics/' + picture+'_bw.jpeg')
        image_bw.show()
        make_mod()
    
    elif mod == 'blurry':
        blur = int(input("How blurry would you like your image to be?: "))
        image1 = Image.open(picture+'.jpeg')
        image1.filter(ImageFilter.BoxBlur(blur)).save('blurry pics/'+ picture+'_blur.jpeg')
        image_b = Image.open('blurry pics/'+ picture+'_blur.jpeg')
        image_b.show()
        make_mod()
    
    elif mod == "smooth":
        image1 = Image.open(picture+'.jpeg')
        image1.filter(ImageFilter.SMOOTH_MORE).save('smooth pics/' + picture+'_smooth.jpeg')
        image_sm = Image.open('smooth pics/' + picture+'_smooth.jpeg')
        image_sm.show()
        make_mod()




   
make_mod()
