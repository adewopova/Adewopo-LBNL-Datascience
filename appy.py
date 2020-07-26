# Imports
import os, flask, dash
from pathlib import Path
from random import randint
import dash_bootstrap_components as dbc

# Plots
from plotly.express import bar
import pandas as pd

# Import iPoster Object Class
from iposter.iposter import iPoster
import iposter.colors as colors

#*** Run Local Flag ***
RUN_LOCAL=True

# ******************Define Your Interactive Poster Here***************
# The following shows a sample interactive poster.
# Images for sections must be saved under the assets/ folder.
# You can import code from your own modules and construct the final dash
# interactive poster here.
def create_poster():

    # Instanitate an iPoster
    my_poster = iPoster(title="Research poster title; state the main topic of your study", # Title of your poster
                        authors_dict={"Inter Name" : "Hood College", # Authors in {student, mentors, PI} order
                                      "Researcher Name" : "Hood College",
                                      "Mentor (Primary Investigator) Name" : "Lawrence Berkeley National Laboratory"},
                        logo = "hood.png", # Home institution logo
                        banner_color=colors.DOE_GREEN, # Color of banner header; colors has preset colors
                        text_color=colors.WHITE)

    # Add sections to first column then add new column
    my_poster.add_section(title="Abstract",
        text="The first cell of your Research Poster must include your research abstract in its entirety. \
        The abstract should fully summarize the contents of your Research Paper in one paragraph. For \
        detailed instructions about how to write the abstract, read Chapter 14 of Scientific Writing\
        and Communication. ")
    my_poster.add_section(title="Background Info",
        text="Begin with the broad background information and significance of\
             your research topic; answer the question “Why should I care?’ \
             This provides the audience with context about how your research \
             relates to the world around them.")
    my_poster.add_section(title="Colors", color=colors.LBNL_BLUE,
        text="Use color to increase the readability of your Research Poster, highlighting important \
        points. Avoid distracting colors. Set section header color with the color parameter.")
    my_poster.next_column()

    # Add sections to second column then add new column
    my_poster.add_section(title="Fonts",
        text="Use the third person. Use concise, not conversational language.\
        .Use bulletpoints whenever possible. Use more images/graphics and less \
        text. Title, up to 90 pt, bold in Arial, Georgia, Palatino or Tahoma font. Headers, \
        50 - 72 pt, bold in Arial, Georgia, Palatino or Tahoma font. Internal text, 24 - 44 \
        pt in Georgia or Palatino font. Spell out acronyms the first time they are ")
    my_poster.add_section(title="Images",
        text="Save your image in the assets directory and set img to the filename.",
        img={"filename":"test.png", "height":"6in", "width":"8in", "caption":"Text for figure caption."})
    my_poster.add_section(title="Other", text="This is some card text.")
    my_poster.next_column()

    # Add sections to third column then add new column
    df = pd.DataFrame([[i,i] for i in range(100)], columns=["x","y"])
    my_plot = bar(df, "x", "y")
    my_poster.add_section(title="Plots",
        text="You can add interactive plots through plotly.",
        plot={"fig": my_plot, "caption": "interactive plot figure caption"})
    my_poster.add_section(title="Other", text="This is some card text.")
    my_poster.add_section(title="Other", text="This is some card text.")
    my_poster.add_section(title="Other", text="This is some card text.")
    my_poster.next_column()

    return my_poster.compile()

# **********************************************************************

# Dash App Configuration
if RUN_LOCAL:
    app = dash.Dash(__name__,
                    assets_folder= str(Path(__file__).parent.absolute())+"/assets",
                    assets_url_path='/',
                    external_stylesheets=[dbc.themes.BOOTSTRAP],
                    suppress_callback_exceptions=True)
else:
    server = flask.Flask(__name__)
    server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
    app = dash.Dash(__name__,
                    server=server,
                    assets_folder= str(Path(__file__).parent.absolute())+"/assets",
                    assets_url_path='/',
                    external_stylesheets=[dbc.themes.BOOTSTRAP],
                    suppress_callback_exceptions=True)
app.layout = create_poster()

# Main Function
if __name__ == "__main__":
    if RUN_LOCAL:
        app.run_server(debug=False, host="0.0.0.0", port="8888")
    else:
        app.server.run(debug=True, threaded=True)