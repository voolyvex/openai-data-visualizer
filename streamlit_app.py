
import pandas as pd
from io import StringIO
import streamlit as st
import streamlit.components.v1 as components
import tableauserverclient as TSC

# Load the Tableau JavaScript API
components.html(
    """
    <script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
    """,
    height=0,
)

def display_header() -> None:
    st.image("img/logo.jpg")
    st.title("Welcome to Tableau Visualizer")

def main():
    # Set up connection.
    # tableau_auth = TSC.PersonalAccessTokenAuth(
    #     st.secrets["tableau"]["token_name"],
    #     st.secrets["tableau"]["personal_access_token"],
    #     st.secrets["tableau"]["site_id"],
    # )
    # server = TSC.Server(st.secrets["tableau"]["server_url"], use_server_version=True)

    # display_header()

    # # Get various data.
    # # Explore the tableauserverclient library for more options.
    # # Uses st.cache_data to only rerun when the query changes or after 10 min.
    # @st.cache_data(ttl=600)
    # def run_query():
    #     with server.auth.sign_in(tableau_auth):

    #         # Get all workbooks.
    #         workbooks, pagination_item = server.workbooks.get()
    #         workbooks_names = [w.name for w in workbooks]

    #         # Get views for first workbook.
    #         server.workbooks.populate_views(workbooks[3])
    #         views_names = [v.name for v in workbooks[3].views]

    #         # Get image & CSV for first view of first workbook.
    #         view_item = workbooks[3].views[1]
    #         server.views.populate_image(view_item)
    #         server.views.populate_csv(view_item)
    #         view_name = view_item.name
    #         view_image = view_item.image
    #         # `view_item.csv` is a list of binary objects, convert to str.
    #         view_csv = b"".join(view_item.csv).decode("utf-8")

    #         return workbooks_names, views_names, view_name, view_image, view_csv

    # workbooks_names, views_names, view_name, view_image, view_csv = run_query()


    # # Print results.
    # st.subheader("📓 Workbooks")
    # st.write("Found the following workbooks:", ", ".join(workbooks_names))

    # st.subheader("👁️ Views")
    # st.write(
    #     f"Workbook *{workbooks_names[3]}* has the following views:",
    #     ", ".join(views_names),
    # )

    # st.subheader("🖼️ Image")
    # st.write(f"Here's what view *{view_name}* looks like:")
    # st.image(view_image, width=300)

    # st.subheader("📊 Data")
    # st.write(f"And here's the data for view *{view_name}*:")
    # st.write(pd.read_csv(StringIO(view_csv)))

    # display an embedded interactive dashboard

       # Set up the embedded Tableau dashboard URL
    tableau_url = "https://public.tableau.com/views/WorldIndicators/GDPpercapita"
    tableau_options = {
        "hideTabs": True,
        "hideToolbar": True,
        "onFirstInteractive": "function () { workbook = viz.getWorkbook(); activeSheet = workbook.getActiveSheet(); }"
    }

    # Embed the Tableau dashboard
    components.html(
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

if __name__ == '__main__':
    main()