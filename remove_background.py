import streamlit as st
from PIL import Image
from rembg import remove
import io
import os


def process_image(uploded_image):
    image = Image.open(uploded_image)
    processed_image = remove_background(image)
    return processed_image


def remove_background(image):
    image_byte = io.BytesIO()
    image.save(image_byte, format="PNG")
    image_byte.seek(0)

    processed_image_bytes = remove(image_byte.read())
    return Image.open(io.BytesIO(processed_image_bytes))


def view_remove_background():
    st.image("assets/remove_bg.jpg", use_container_width=True)
    st.title("Remover Fondo de Imagen")
    st.write("Por favor, sube una imagen para remover el fondo")
    image = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

    if image is not None:
        # print(image.name)

        name_without_extension = os.path.splitext(image.name)[0]
        new_file_name = f"remove-{name_without_extension}.png"

        st.image(image, caption="Imagen Original", use_container_width=True)
        remove_button = st.button("Quitar Fondo")

        if remove_button:
            processed_image = process_image(image)
            st.image(
                processed_image, caption="Imagen Procesada", use_container_width=True
            )
            processed_image.save(new_file_name)

            with open(new_file_name, "rb") as f:
                image = f.read()

            st.download_button(
                "Descargar Imagen Procesada",
                image,
                file_name=new_file_name,
                mime="image/png",
            )

            os.remove(new_file_name)
