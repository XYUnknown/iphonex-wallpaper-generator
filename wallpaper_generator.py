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
		user_command = input("please choose LEFT, CENTRE or RIGHT:\n")
		user_command = user_command.upper()
		print(user_command)
		temp_x = c_y * ratio
		crop_x = c_x - temp_x
		if user_command == "LEFT":
			result = img.crop((0, 0, temp_x, c_y))
		elif user_command == "RIGHT":
			result = img.crop((crop_x, 0, c_x, c_y))
		else: # default crop centre
			result = img.crop((crop_x/2, 0, crop_x/2+temp_x, c_y))
		result = result.resize(t_size)
		print("case1")
		return result
	# curr_x < target_x, curr_y >= target_y
	elif (curr_ratio < ratio):
		user_command = input("please choose UP, CENTRE or DOWN:\n")
		user_command = user_command.upper()
		temp_y = c_x / ratio
		crop_y = c_y - temp_y
		if user_command == "UP":
			result = img.crop((0, 0, c_x, temp_y))
		elif user_command == "DOWN":
			result = img.crop((0, crop_y, c_x, c_y))
		else: # default crop centre
			result = img.crop((0, crop_y/2, c_x, crop_y/2+temp_y))
		result = result.resize(t_size)
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
	file_name = input("Please enter a name for your new wallpaper: \n")
	file_name = file_name.strip()
	if len(file_name) == 0:
		file_name = "default.png"
	else:
		file_name = file_name + ".png"
	result_img.save(file_name)

if __name__ == "__main__":
	run()