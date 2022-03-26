import streamlit as st
from PIL import Image
import imagecaption
import currencycalculator


PAGES = {
    "Image Cation": imagecaption,
    "CURRENCY ": currencycalculator
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

# st.subheader("Image")
# image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])



# def load_image(image_file):
# 	img = Image.open(image_file)
# 	return img

	# To See details
# file_details = {"filename":image_file.name, "filetype":image_file.type,
#                               "filesize":image_file.size}
# st.write(file_details)

#     # To View Uploaded Image
# st.image(load_image(image_file),width=250)