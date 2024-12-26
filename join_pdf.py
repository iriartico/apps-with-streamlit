import streamlit as st
import PyPDF2


output_pdf = "fusionado.pdf"


def join_pdfs(output_pdf, pdfs):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdfs:
        pdf_merger.append(pdf)

    # with open(output_pdf, "wb") as f:
    #     pdf_merger.write(f)
    pdf_merger.write(output_pdf)

    # return output_pdf


def view_join_pdf():
    st.image("assets/fusionar-pdf.jpg", use_container_width=True)
    st.header("Combinar archivos PDF")
    st.subheader("Seleccione los archivos PDF que desea combinar")

    pdfs = st.file_uploader("Upload", type=["pdf"], accept_multiple_files=True)

    join = st.button(label="Combinar PDFs")

    if join:
        if len(pdfs) <= 1:
            st.warning("Por favor, seleccione más de un archivo PDF")
        else:
            join_pdfs(output_pdf, pdfs)
            st.success(f"Felicidades, ya puedes descargar el archivo fusionado")

            with open(output_pdf, "rb") as f:
                pdf = f.read()

            st.download_button(
                label="Descargar archivo fusionado",
                data=pdf,
                file_name=output_pdf,
                mime="application/pdf",
            )
