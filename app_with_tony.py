import streamlit as st
from join_pdf import view_join_pdf
from remove_background import view_remove_background
from extract_audio_from_video import view_extract_audio_from_video


def main_page():
    st.title("Apps con Tony")
    st.subheader("Esta es la pagina principal de la app.")
    st.write("Usa la barra lateral izquierda para navegar por la aplicacion")


if __name__ == "__main__":
    st.sidebar.title("Aplicaciones")
    page = st.sidebar.selectbox(
        "Elige una aplicacion",
        [
            "Pagina Principal",
            "Unir pdf's",
            "Quitar fondo de imagen",
            "Extraer audio de video",
        ],
    )
    if page == "Pagina Principal":
        main_page()
    elif page == "Unir pdf's":
        view_join_pdf()
    elif page == "Quitar fondo de imagen":
        view_remove_background()
    elif page == "Extraer audio de video":
        view_extract_audio_from_video()

    # st.sidebar.title("Audio / Video")

    # page2 = st.sidebar.selectbox(
    #     "Seleccionar",
    #     ["Extraer audio de video"],
    # )
    # if page2 == "Extraer audio de video":
    #     view_extract_audio_from_video()
