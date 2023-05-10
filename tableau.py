import tableauserverclient as TSC
import streamlit as st

def embed_dashboard(tableau_url: str, tableau_options: dict) -> str:
    tableau_auth = TSC.PersonalAccessTokenAuth(
        st.secrets["tableau"]["token_name"],
        st.secrets["tableau"]["personal_access_token"],
        st.secrets["tableau"]["site_id"],
    )
    server = TSC.Server(st.secrets["tableau"]["server_url"], use_server_version=True)
    
    with server.auth.sign_in(tableau_auth):
        dashboard = f"""
            <div class='tableauPlaceholder' id='tableauViz'></div>
            <script>
            var placeholderDiv = document.getElementById('tableauViz');
            var url = '{tableau_url}';
            var options = {tableau_options};
            var viz = new tableau.Viz(placeholderDiv, url, options);
            </script>
        """
        return dashboard