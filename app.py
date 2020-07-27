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
RUN_LOCAL=False

# ******************Define Your Interactive Poster Here***************
# The following shows a sample interactive poster.
# Images for sections must be saved under the assets/ folder.
# You can import code from your own modules and construct the final dash
# interactive poster here.
def create_poster():

    # Instanitate an iPoster
    my_poster = iPoster(title="Applying Machine Learning NLP Techniques to Investigate the Semantic Structure of Clinical Notes for Identifying SDOH", #Title of your poster
                        authors_dict={"Adewopo Victor" :["University of Cincinnati", "Lawrence Berkeley National Laboratory"],
                        "Praneetha Gounipa" : ["University of Cincinnati","Lawrence Berkeley National Laboratory"], # Authors in {student, mentors, PI} order
                                      
                        "Wangia-Anderson Victoria" : ["University of Cincinnati","Lawrence Berkeley National Laboratory"],
                        "Silvia Crivelli" : ["Lawrence Berkeley National Laboratory"]},
                        logo = "UC.png", # Home institution logo
                        banner_color=colors.DOE_GREEN, # Color of banner header; colors has preset colors
                        text_color=colors.WHITE)

    # Add sections to first column then add new column
    my_poster.add_section(title="Abstract",
        text="Electronic health records contain vital information not always fully captured by only analyzing structured data. Mining unstructured clinical notes can provide contextual meaning and complement the analysis of structured data. We explore using MIMIC III unstructured medical notes  to  determine if the notes can be categorized into various key topics using unsupervised classification of documents. Our ultimate goal is to be able to identify documents that are associated with  topics related to homelessness and other social determinants of health (SDOH) including suicide ideation and suicide. The rich context of the words  and sequencing of the words in the notes is maintained by beginning to explore using n-grams for the language model. We utilized unigrams and bigrams together in training the  latent Dirichlet allocation (LDA) model which is a popular topic modeling method. Trigrams and hexagrams were also explored. The LDA  model showed key topics that the notes could be associated with. As expected many of the topics were clinical, however, old is in the results and frequently associated with age when explored using trigrams. The n-gram results show other  social factors such as family and  communication, while Tableau showed marital status as common across notes.")
    my_poster.add_section(title="Background",
        text="The continuous availability of longitudinal clinical records of patients generated by one or more encounters in any healthcare delivery setting prompted the mining and exploration of medical data for sentimental and contextual analysis that can be utilized by healthcare workers in providing prioritized health care and smooth workflow[1].\
        Social determinants of health are environmental conditions in which patients are exposed to which have an adverse effect on their health outcome and are viewed as risk factors. Identifying risk factors is of immense benefit to health care professionals in providing comprehensive care plans, for prevention,  and for concentrated clinical and psychological support. Suicide is a large and growing public health problems.  The Centers for Disease Control and Prevention (CDC) ranks suicide as the 10th leading cause of death and sadly, the rates continue to increase[7]. Though there is no single cause of suicide, research has shown that there are some key contributing risk factors.  Multiple studies have shown a correlation between social determinants of health such as homelessness, and suicide, noting that homelessness triggers ideation and mortality by suicide. The unstructured medical notes of patients contain a wealth of information that can be mined using analytical and natural language processing tools to generate new evidence from existing information.  Topic modeling is a method for unsupervised classification of documents. The n-gram and LDA models can parse through a large set of medical history and predict what topic a medical history belong to and the percentage of the contribution the topic has based on medical history.")
    #my_poster.add_section(title="Goals and Objective", 
    #    text=" Our goal with this project was to develop a model and approach that could identify words and topics from medical notes,  and determine if any of them are SDOH.  Our longer-term goal is to develop a model able to show the frequency of terms and compare across clinical notes to determine if any of the top words in the medical notes are associated with homelessness. With these findings, we can then predict from unstructured medical notes and tagging patients with identified risk factors such as homelessness, in order to intervene early.")
    my_poster.add_section(title="Methodology",
        text="For this study we utilized the MIMIC-III dataset which is an open-source dataset developed by the MIT Lab for Computational Physiology,  comprising of de-identified health data associated with over 46,000 unique patients medical data. We identified features from the unstructured text using controlled vocabularies, rule sets, reference dictionaries that were hand-coded to preserve the contextual meaning of words in the data. This approach comprised of five steps of data selection, pre-processing, transformation, data mining, and interpretation Text mining is a field of data mining that involves the extraction of information from existing data[4]. We focused on the unstructured part of the MIMIC III data set and selected 8,583 patients that have a diagnosis related to diseases of despair[5]. N-gram models are widely used in statistical natural language processing to identify a sequence of words in a given dataset. We utilized unigrams and added bigrams to yield higher accuracy in text categorization. The LDA model was used to understand, search, and summarize topics that the n-grams in the notes could be associated with and has been proven to yield better results in prior research[6]. We identified the top unigram words and sequence of six top words using hexagram.")  
    
    # Add sections to second column then add new column
    my_poster.next_column()
    my_poster.add_section(title="Figures",
        img1={"filename":"50-80trig.png", "height":"5in", "width":"9in", "caption":"The figure shows the top 30 recurring trigrams in order of sequence after processing our dataset."},
        img2={"filename":"word.png", "height":"5in", "width":"9in", "caption":"This figure shows the  word count of dominant words in six topics and the importance of the words within each topic in terms of weights."},
        img3={"filename":"wordcloud.png", "height":"5in", "width":"9in", "caption":"This figure showcase the most common keywords in each topics"})
    my_poster.add_section(title="Findings", text="We have been able to train a model that can classify patient medical history into relevant topics, utilizing unigrams and bigrams together in training the LDA model. The topmost recurring trigrams suggested medical conditions related to patients that are old. Hemodynamics is one of the recurring themes in the trigram, series which are related to hypertension and blood flow. Hexagrams gave more contextual meaning to the top recurring words in order of sequences in the dataset Hexagram.  The dominant topics in the dataset are; Renal failure, Hypertension, Diabetes, Hemodynamic, and Blood organs. The Most recurring Keywords are ‘Assessment’, ‘Respiratory’,‘Failure’, ‘Response’, ‘Plan’, ‘Action’, ‘Acute’, ‘Renal’, ‘Blood’.")
    my_poster.add_section(title="Conclusion", text="Medical information contains a large set of data. The mean word count in a single patient medical history contains about 4,700  words. Our trained model can parse through a large set of medical history and predict what topic a medical history belong too and the percentage of the contribution the topic has based on medical history. This saves health care professionals from reading a large set of patient medical history and can also be utilized in providing prioritized care based on the identified topic.") 
    my_poster.add_section(title="Acknowledgments", text="This work was supported in part by the U.S. Department of Energy, Office of Science, Computational Research Division (CRD) of the Berkeley National Lab. Special thanks to Dr.Wangia-Anderson, Dr. Crivelli, Rafael, Shirley, and all the other team members for contributing to this research and making the summer fellowship memorable")
       # Add sections to third column then add new column
    my_poster.next_column()

    
    my_poster.add_section(title="Interactive LDA Plot",
    	pyLDA2={"filename":"topic.html", "height":"8in", "width":"12in", "caption": "This figure shows the dominant topics the medical history belonging to ten patients is classified to by our model and the percentage of contribution."},
        pyLDA={"filename":"full_lda_html.html", "height":"8in", "width":"12in", "caption": "Hover on the interactive plot to view the 10  topics and the frequency of the topwords.The circles represent different topics and the distance between them. Similar topics appear closer to eachother."},
        pyLDA3={"filename":"DoD-TSNE.html", "height":"8in", "width":"12in", "caption": "This figure shows a 2D cluster of patients medical notes and what topic they have been classified to in the top ten topics from our LDA model."})
             
    my_poster.add_section(title="References", 
        text="1.Atherton, J. (2011, March 1). Development of the Electronic Health Record. Retrieved from \
        https://journalofethics.ama-assn.org/article/development-electronic-health-record/2011-03.    \
        3.https://americanaddictioncenters.org/rehab-guide/addiction-statistics. \
        4.Gonzalez, G. H., Tahsin, T., Goodale, B. C., Greene, A. C., & Greene, C. S. (2016). Recent advances and emerging applications in text and data  \
        mining for biomedical discovery. Briefings in bioinformatics, 17(1), 33-42. \
        5.Zamora-Resendiz, R., Wang, X., Liu, X., & Crivelli, S. Predicting ICU Readmission with Context-Enriched Deep Learning.  \
        6. Bjarnadottir, R. I., & Lucero, R. J. (2018). What can we learn about fall risk factors from EHR nursing notes? A text mining study. eGEMs, 6(1) \
        7. Suicide and Self-Inflicted Injury https://www.cdc.gov/nchs/fastats/suicide.htm Accessed: 2020-07-27.")   
    #my_poster.add_section(title="Other", text="This is some card text.")
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
