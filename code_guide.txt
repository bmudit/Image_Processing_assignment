
This text document aims to explain what code/algorithms have been used to complete this assinment.
A set of same functions have been used with different parameters for different background and threat combination depending upon the suitability for that particular set. 
This assignment was done using jupyter notebook.

##################################################################################################################

Libraries Used :

1)	matplotlib : pyplot has been used to display the resultant image time to time in order to make the necessary changes through trail and error.

2)	PIL : PIL has been used as the image processing library. Almost everything is done using two of its objects - Image and ImageEnhance

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Functions and objects used :

1) 	Image.open('directory') : used to open background (b1,b2,b3,b4,b5) and threat (t1,t2,t3,t4,t5) images.

2)	t_image_var.crop(size) : used to crop out the threat image. ( this functions has been use twice per threat image, because otherwise, the rotation was causing the threat element getting cropped out )

3)	t_image_var.rotate(value) : used to rotate the threat image. ( as the assignment mentions, by 45 degrees )

4) 	t_image_var.putalpha(127) : used to make the threat image translucent and blend with the background.

5) 	ImageEnhance.Color(t_image_var).enhance(value) ,
	ImageEnhance.Contrast(t_image_var).enhance(value), 
	ImageEnhance.Sharpness(t_image_var).enhance(value), 
	ImageEnhance.Brightness(t_image_var).enhance(value),
	
	(These enhacement functions have been used to change the color,contrast,sharpness and brightness of the threat objects. Through trail and error, they were used them to match those objects with the background image.)

6)	t_image_var = t_image_var.convert("RGBA")
	datas = t_image_var.getdata()

	newData = []
	for item in datas:
    		if (item[0] == 255 and item[1] == 255 and item[2] == 255) or (item[0] == 0 and item[1] == 0 and item[2] == 0):
        			newData.append((255, 255, 255, 0))
    		else:
        			newData.append(item)

	t_image_var.putdata(newData)

	( This code snippet has been used to remove the white and black background of the threat image to get the exact shape of the element )

7)	t_image.resize(size) : used to resize the threat image.

8)	bag1.paste(t_image_var , coordinates,  t_image_var.convert = 'RGBA') : used to paste the threat image over background image, giving its precise location and removing black background.

9)	plt.imshow() : used to display the output on jupyter notebook using matplotlib.

10)	bag_image_var.save() : used to save and export the final output image.

##################################################################################################################
