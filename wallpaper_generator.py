# import package
from PIL import Image

# The function to crop a image
# and make it fit the iPhone X screen.
def crop_image(img, t_size):
	x = t_size[0]
	y = t_size[1]
	ratio = round(float(x) / float(y), 2)
	curr_size = img.size
	c_x = curr_size[0]
	c_y = curr_size[1]
	curr_ratio = round(float(c_x) / float(c_y), 2)
	# ratio same, resize
	if (curr_ratio == ratio):
		result = img.resize(t_size)
		print("case0")
		return result
	# curr_x >= target_x, curr_y < target_y
	elif (curr_ratio > ratio):
		temp_x = c_y * ratio
		crop_x = c_x - temp_x
		result = img.crop((crop_x/2, 0, crop_x/2+temp_x, c_y))
		result = result.resize(t_size)
		print("case1")
		return result
	# curr_x < target_x, curr_y >= target_y
	elif (curr_ratio < ratio):
		temp_y = c_x / ratio
		crop_y = c_y - temp_y
		result = img.crop((0, crop_y/2, c_x, crop_y/2+temp_y))
		result = result.resize(t_size)
		# result = img.resize(t_size)
		print("case2")
		return result
	else:
		return None
	
def run():
	# setup
	# original
	my_img = Image.open("test00.png") # replace by your image, accept .jpg, .png image
	my_img = my_img.convert("RGBA")

	# mask
	mask = Image.open("mask.png")
	mask = mask.convert("RGBA")
	# get mask size
	mask_size = mask.size
	# crop image
	cropped_img = crop_image(my_img, mask_size)
	# a image cannot be handled.
	if cropped_img == None:
		print("sorry something wrong")
		return ""
	# composite image and mask, save the final image
	result_img = Image.alpha_composite(cropped_img, mask)
	result_img.save("new_wallpaper00.png")

if __name__ == "__main__":
	run()