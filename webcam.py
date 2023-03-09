import streamlit as st
from PIL import Image, UnidentifiedImageError

with st.expander('Start Camera'):
    camera_image = st.camera_input('Camera')

    if camera_image:
        # create pillow image
        img = Image.open(camera_image)

        # convert to grayscale
        gray_img = img.convert('L')
        st.image(gray_img)

with st.expander('Upload file'):
    file_img = st.file_uploader('Upload image')

    try:
        if file_img:
            img = Image.open(file_img)
            gray_img = img.convert('L')
            st.image(gray_img)
    except UnidentifiedImageError:
        st.info('Not an image file')
