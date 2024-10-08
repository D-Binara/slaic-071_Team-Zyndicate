import os
import streamlit as st
from utils.utils import save_pdf_txt_on_temp_dir, load_into_vector_store, stream_text
from utils.manifestomatchmaker import get_relevant_policies
from utils.alignpolicy import get_align_candidate, draw_pie_plot

selected_policies=[]
list_of_policies=[]

# App title
st.set_page_config(page_title="🤗💬 Election-Insight-App ")

#app side bar
with st.sidebar:
    st.subheader("Upload the manifesto of the candidate.")
    
    uploaded_files = st.file_uploader(
    "Choose a PDF, TXT files", accept_multiple_files=True)
    
    
    for uploaded_file in uploaded_files:
        st.write("filename:", uploaded_file.name)
        save_pdf_txt_on_temp_dir(uploaded_file=uploaded_file)
        
    if uploaded_files:
        with st.spinner("Processing..."):
            st.button("Upload to vector store.", on_click=load_into_vector_store())

st.title("💡 Manifesto Matchmaker")
st.write("-----------------------------------------------------------------------------------------------------------") 

selected_themes=st.multiselect(label="Select Your Themes", 
                               options=["Infrastructure", "Social Protection", "Trade and Export", "Labour", "Governance", "Law and Order", "Corruption", "Agriculture", "Health", "Taxation", "Education", "Supplementary", "Economic Growth", "IMF Programme", "Reconciliation"], 
                               help="Every promise has an associated topic. In this section, select which topics you wish to focus on, under each of your chosen themes. A topic is a distinct subject area that classifies individual promises. Each theme has multiple topics, though not all topics are represented under every theme."
                               )

if selected_themes:
    with st.spinner("Processing..."):
        list_of_policies=[]
        for selected_theme in selected_themes:
            list_of_policies.append(get_relevant_policies(selected_theme))


if list_of_policies:
    for list_of_policy in list_of_policies:
        selected_policies.append(st.multiselect(label="Select Policies", 
                                options=list_of_policy
                                )
        )
        

t=st.text_input("enter")

if t:
    #st.write(get_align_candidate(t))
    
    st.pyplot(draw_pie_plot(["a", "b"], [0.5, 0.5])
)




