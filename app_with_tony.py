import streamlit as st
from join_pdf import view_join_pdf
from remove_background import view_remove_background


def main_page():
    st.title("Apps con Tony")
    st.subheader("Esta es la pagina principal de la app.")
    st.write("Usa la barra lateral izquierda para navegar por la aplicacion")


if __name__ == "__main__":
    st.sidebar.title("Aplicaciones")
    page = st.sidebar.selectbox(
        "Choose a page",
        ["Pagina Principal", "Unir pdf's", "Quitar fondo de imagen"],
    )
    if page == "Pagina Principal":
        main_page()
    elif page == "Unir pdf's":
        view_join_pdf()
    elif page == "Quitar fondo de imagen":
        view_remove_background()
