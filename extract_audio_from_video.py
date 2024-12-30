import streamlit as st
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import os
import shutil


def view_extract_audio_from_video():
    st.title("Extraer Audio de Video")
    video = st.file_uploader(
        "Sube un video para extraer el audio", type=["mp4", "avi", "mov", "mkv"]
    )

    if video is not None:
        st.write("Video subido")
        save_path = os.path.join("video", video.name)
        # print(save_path)
        with open(save_path, "wb") as f:
            shutil.copyfileobj(video, f)
        with open(save_path, "rb") as folder:
            st.video(folder, format="video/mp4")

        name_without_extension = os.path.splitext(video.name)[0]
        audio_file_name = f"audio-{name_without_extension}.mp3"
        try:
            ffmpeg_extract_audio(save_path, f"audio/{audio_file_name}")
            st.write("Audio extraido")
            with open(f"audio/{audio_file_name}", "rb") as folder:
                st.audio(folder, format="audio/mp3")

            with open(f"audio/{audio_file_name}", "rb") as folder:
                st.download_button(
                    label="Descargar Audio",
                    data=folder,
                    file_name=audio_file_name,
                    mime="audio/mp3",
                )

                os.remove(f"audio/{audio_file_name}")
                os.remove(save_path)

        except Exception as e:
            st.write(e)

        # name_without_extension = os.path.splitext(image.name)[0]
        # new_file_name = f"remove-{name_without_extension}.png"

        # st.image(image, caption="Imagen Original", use_container_width=True)
        # remove_button = st.button("Quitar Fondo")

        # if remove_button:
        #     processed_image = process_image(image)
        #     st.image(
        #         processed_image, caption="Imagen Procesada", use_container_width=True
        #     )
        #     processed_image.save(new_file_name)

        #     with open(new_file_name, "rb") as f:
        #         image = f.read()

        #     st.download_button(
        #         "Descargar Imagen Procesada",
        #         image,
        #         file_name=new_file_name,
        #         mime="image/png",
        #     )

        #     os.remove(new_file_name)
