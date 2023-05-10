import pandas as pd
from io import StringIO
import streamlit as st
import streamlit.components.v1 as components
import tableauserverclient as TSC

class ScriptRunContext:
    def __init__(self):
        self.args = None

    # Load the Tableau JavaScript API
    components.html(
        """
        <script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
        """,
        height=800,
    )
st._ScriptrunContext = ScriptRunContext()

def run_query():

    tableau_auth = TSC.PersonalAccessTokenAuth(
            st.secrets["tableau"]["token_name"],
            st.secrets["tableau"]["personal_access_token"],
            st.secrets["tableau"]["site_id"],
        )
    server = TSC.Server(st.secrets["tableau"]["server_url"], use_server_version=True)
    
    try:
        with server.auth.sign_in(tableau_auth):
            # Set up the embedded Tableau dashboard URL
            tableau_url = "https://prod-useast-b.online.tableau.com/t/biworkspace/views/ExecutiveOverview/ExecutiveOverview?:origin=card_share_link&:embed=n"
            tableau_options = {
                "onFirstInteractive": "function () { workbook = viz.getWorkbook(); activeSheet = workbook.getActiveSheet(); }"
            }

            # Embed the Tableau dashboard
            dash = components.html(
                f"""
                <div class='tableauPlaceholder' id='tableauViz'></div>
                <script>
                var placeholderDiv = document.getElementById('tableauViz');
                var url = '{tableau_url}';
                var options = {tableau_options};
                var viz = new tableau.Viz(placeholderDiv, url, options);
                </script>
                """,
                height=800,
            )
            return dash
    except TSC.ServerResponseError as e:
        st.error(f"Tableau server error: {e}")
        return None
        
def display_header() -> None:
    st.image("img/logo.jpg")
    st.title("Welcome to Tableau Visualizer")

def main():

    display_header()
    run_query()

if __name__ == '__main__':
    main()
