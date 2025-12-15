import streamlit as st
import pandas as pd
import os

def user_ai_response(review, rating):
    return f"Thank you for rating us {rating} stars!"

def admin_summary(review):
    if review.strip() == "":
        return "No review given"
    return review[:50] + "..."

def admin_recommendation(review):
    text = review.lower()
    if "bad" in text:
        return "Immediate action required"
    elif "good" in text:
        return "Maintain quality"
    else:
        return "Monitor feedback"

st.title("⭐ User Feedback Dashboard")

rating = st.slider("Select Rating", 1, 5, 3)
review = st.text_area("Write your review")

if st.button("Submit"):
    ai_reply = user_ai_response(review, rating)
    summary = admin_summary(review)
    action = admin_recommendation(review)

    data = {
        "Rating": rating,
        "Review": review,
        "AI_Response": ai_reply,
        "AI_Summary": summary,
        "AI_Action": action
    }

    if os.path.exists("feedback.csv"):
        df = pd.read_csv("feedback.csv")
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    else:
        df = pd.DataFrame([data])

    df.to_csv("feedback.csv", index=False)

    st.success("Feedback submitted successfully!")
    st.info(ai_reply)
