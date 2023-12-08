import streamlit as st
import joblib
import time

st.set_page_config(
    page_title='SMS-SPAM-DETECTION',
    page_icon='💬',
)
# main-code of sms-spam-detections starts
# Load your pre-trained model and TF-IDF vectorizer
st.write("Loading model and vectorizer...")
try:
    baseline_model = joblib.load('model.pkl', "rb")
    tfidf_vec = joblib.load('vectorizer.pkl', 'rb')
    st.write(f"Model type: {type(baseline_model)}")
    st.success("Loading Completed✅...")
except Exception as e:
    st.error(f"Error loading model or vectorizer: {e}")
    st.stop()


# Streamlit app
def main():
    st.header('SMS-SPAM-DETECTION')
    st.subheader('A Machine learning approach to identify Spam messages')

    # Input text box
    text = st.text_area("Enter SMS Text:", "")

    # Predict button
    if st.button("Predict"):
        if text:
            # Vectorize the input text using the TF-IDF vectorizer
            text_vec = tfidf_vec.transform([text])

            # Make a prediction using the trained model
            with  st.spinner("Making prediction..."):
                time.sleep(2)

            try:
                # Check if the loaded model is a valid scikit-learn model
                if hasattr(baseline_model, 'predict') and callable(getattr(baseline_model, 'predict')):
                    prediction = baseline_model.predict(text_vec)[0]
                    st.write("Prediction completed.")

                    # Convert the prediction to a human-readable label
                    result = 'spam' if prediction == 1 else 'ham'

                    # Display the result
                    st.success(f"Prediction Result: {result}")
                else:
                    st.error("The loaded object is not a valid scikit-learn model.")
            except Exception as e:
                st.error(f"Error making prediction: {e}")
            finally:
                st.write('Done')
        else:
            st.warning("Please enter some text to predict.")


if __name__ == "__main__":
    main()

st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
            background-image: url('back.jpg');
            background-size:cover;
            background-position:center;
        }

        .stApp {
            max-width: 1700px;
            # max-height:1000px
            margin: 0 auto;
        }

        .st-title {
            color: #4285f4;
        }

        .stTextInput {
            width: 100%;
            padding: 10px;
            box-sizing: border-box;
            margin-bottom: 20px;
        }

        .stButton {
            # background-color:#4285f4
            color: #fff;
            padding: 10px 15px;
            font-size: 1rem;
            font-weight:700;
            border: none;
            cursor: pointer;
            border-radius: 10px;

        }
        .stSuccess {
            color: #4caf50;
        }

        .stError {
            color: #f44336;
        }

        .stWarning {
            color: #ff9800;
        }
        .image{
          width:100px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
