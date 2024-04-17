import streamlit as st

# Function to define custom styles
def set_custom_style():
    # Section headers
    st.markdown(
        """
        <style>
        .section-header {
            color: #1565C0;
            font-size: 24px;
            font-weight: bold;
            padding-top: 10px;
            padding-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Text color
    st.markdown(
        """
        <style>
        .text {
            color: #424242;
            font-size: 18px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    set_custom_style()
    title_html = "<h1 style='font-size: 45px;'>Welcome to <span style='color: #4CAF50;'>GUVI</span> AWS Cloud 'Learner to Leader' Crash Course</h1>"
    st.markdown(title_html, unsafe_allow_html=True)
    st.title("")

    st.markdown("<p class='section-header'>What is Cloud Computing?</p>", unsafe_allow_html=True)
    st.markdown("""
    <p class='text'>Cloud computing is the delivery of computing services—including servers, storage, databases, networking, software, analytics, and intelligence—over the Internet ("the cloud") to offer faster innovation, flexible resources, and economies of scale. Typically, you only pay for cloud services you use, helping you lower your operating costs, run your infrastructure more efficiently, and scale as your business needs change.</p>
    """, unsafe_allow_html=True)

    st.markdown("<p class='section-header'>Why Cloud Computing?</p>", unsafe_allow_html=True)
    st.markdown("""
    <p class='text'>Cloud computing provides numerous benefits, including:</p>
    <ul class='text'>
        <li>Scalability: Easily scale your infrastructure up or down based on demand.</li>
        <li>Cost-Effectiveness: Pay only for the resources you use, avoiding upfront infrastructure costs.</li>
        <li>Flexibility and Agility: Quickly deploy resources and adapt to changing business needs.</li>
        <li>Reliability: Cloud providers typically offer high levels of uptime and redundancy.</li>
        <li>Security: Cloud providers invest heavily in securing their infrastructure and offer various security features.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("<p class='section-header'>Amazon Web Services (AWS)</p>", unsafe_allow_html=True)
    st.markdown("""
    <p class='text'>Amazon Web Services (AWS) is one of the leading cloud computing platforms, offering a wide range of services including computing power, storage options, networking, databases, machine learning, analytics, and more. Some of the popular AWS services include Amazon EC2 (Elastic Compute Cloud), Amazon S3 (Simple Storage Service), Amazon RDS (Relational Database Service), and Amazon Lambda.</p>
    """, unsafe_allow_html=True)

    st.markdown("<p class='section-header'>Learn More</p>", unsafe_allow_html=True)
    st.markdown("""
    <p class='text'>To learn more about AWS Cloud Computing, visit the <a href='https://aws.amazon.com/' target='_blank' style='color: #1565C0; text-decoration: none;'>AWS website</a>.</p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()