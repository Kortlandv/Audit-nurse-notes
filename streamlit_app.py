import streamlit as st
from transformers import pipeline

# Title of the App
st.title("Nursing Note Audit Tool")

# Input box for nursing notes
nursing_note = st.text_area("Paste your nursing note below:")

if st.button("Analyze"):
    if nursing_note.strip():
        # Mock audit feedback
        feedback = "Identified issues: Clarify patient description and specify interventions."
        revised_note = ("Patient observed pacing in room, stating 'I feel anxious.' Administered lorazepam 1 mg PO at 0900 "
                        "per provider order. Reassessed at 0930: patient calmer, sitting in bed, and states, 'I feel better now.'")
        
        # Display feedback
        st.subheader("Feedback:")
        st.write(feedback)

        # Display revised note
        st.subheader("Revised Note:")
        st.write(revised_note)
    else:
        st.warning("Please paste a nursing note to analyze!")