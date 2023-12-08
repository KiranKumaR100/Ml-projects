import streamlit as st

# page-configuration
st.set_page_config(
    page_title='Home',
    page_icon='🏠'
)
# home and image
st.title('Home')
st.image('spam.jpeg')

st.title("SMS Spam Detection Hub")

st.write("🛡️**About SMS Spam**")
st.write("SMS spam, also known as unsolicited text messages, can be an annoying intrusion into our daily lives. It "
         "often comes in the form of unwanted advertisements, phishing attempts, or fraudulent schemes")

st.write("🔍 **Model Explanation**")
st.write("Our SMS spam detection model is built using TensorFlow, a powerful machine learning library "
         "tensorflow it analyzes the content of incoming messages, "
         "distinguishing between legitimate and spam messages with accuracy of 98%.")

st.write("💻 **Algorithms used**")
st.write("Naive Bayes Classifier: Utilized for its simplicity and effectiveness in text classification tasks.")

st.write("⚙️ **Techniques Used**")
st.write("Feature Engineering: We extract relevant features from the message content, such as keywords, frequency of "
         "certain terms, and linguistic patterns, to enhance the model's ability to make accurate predictions.",

         "Ensemble Learning: Combining the strengths of multiple models through ensemble techniques helps improve the "
         "overall"
         "performance and robustness of our spam detection system")

st.write("🈸 **StreamLit**")
st.write("Our user interface is powered by Streamlit, providing a user-friendly and interactive platform."
         " With Streamlit, users can easily navigate, customize settings,"
         " and visualize real-time insights into spam detection.")
