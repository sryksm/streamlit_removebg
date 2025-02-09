import streamlit as st
from io import BytesIO
from PIL import Image
from rembg import remove
from cartooner import cartoonize
import cv2

st.set_page_config(page_title="Image Background remover", 
                   page_icon=":scissors:", 
                   layout='centered',
                   menu_items={'Get Help': 'mailto:suryakusumasae@gmail.com', 
                               'Report a bug': 'mailto:suryakusumasae@gmail.com', 
                               'About': '''This is a simple web app to remove background from images.
                                It uses the `rembg` library to remove the background. The `rembg` library is a Python wrapper for the `remove.bg` API.
                                The `remove.bg` API is a paid service, but the `rembg` library is free to use.
                                You can also cartoonize the image using the `cartooner` library.

                                AUTHOR: KHALID AS'''})

st.title("Image Background Remover")
st.write("This is a simple web app to remove background from images. It uses the `rembg` library to remove the background. The `rembg` library is a Python wrapper for the `remove.bg` API. The `remove.bg` API is a paid service, but the `rembg` library is free to use. You can also cartoonize the image using the `cartooner` library.")

st.sidebar.title('Upload and download :gear:')
my_upload = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
alpha_matting = st.sidebar.checkbox('Alpha Matting', value=False)
threshold = st.sidebar.slider('background threshold', 0, 100, value=50, step=5)

def convert_bytes_to_image(bytes_data):
    buf = BytesIO()
    bytes_data.save(buf, format="PNG")
    byte_in = buf.getvalue()
    return byte_in

def remove_bg(my_upload, alpha_matting, threshold):
    image = Image.open(my_upload)
    col1, col2 = st.columns(2)
    with col1:
        st.write("Original Image :camera:")
        st.image(image, caption="Original Image :camera:", use_container_width=True)
    with col2:
        st.write("Removing background :scissors:")
        with st.spinner('Processing...'):
            img = cv2.cvtColor(cv2.imread(my_upload), cv2.COLOR_BGR2RGB)
            img = remove(img, alpha_matting=alpha_matting, threshold=threshold)
            img = Image.fromarray(img)
            st.image(img, caption="Background Removed Image :scissors:", use_container_width=True)

    cartoon = cartoonize(image)
    imgg = Image.fromarray(cartoon)
    st.write("Cartoonized Image :art:", use_container_width=True)
    st.image(imgg, caption="Cartoonized Image :art:", use_container_width=True)

    st.sidebar.download_button("Download removed-bg Image", convert_bytes_to_image(img), f'pict_no_bg.png', 'png')
    st.sidebar.download_button("Download cartoonize Image", convert_bytes_to_image(imgg), f'pict_cartoon.png', 'png')

    

if my_upload:
    remove_bg(my_upload, threshold, alpha_matting)
else:
    remove_bg('./Images/cutie cat.jpg', threshold, alpha_matting)


