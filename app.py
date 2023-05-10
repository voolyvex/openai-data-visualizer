import streamlit as st
from tableau import embed_dashboard

def display_header() -> None:
    st.image("img/logo.jpg")
    st.title("Welcome to Tableau Visualizer")

def main() -> None:
    display_header()
    tableau_url = "https://prod-useast-b.online.tableau.com/t/biworkspace/views/ExecutiveOverview/ExecutiveOverview?:origin=card_share_link&:embed=n"
    tableau_options = {
        "onFirstInteractive": "function () { workbook = viz.getWorkbook(); activeSheet = workbook.getActiveSheet(); }"
    }
    dashboard = embed_dashboard(tableau_url, tableau_options)
    st.components.v1.html(dashboard, height=800)

if __name__ == '__main__':
    main()