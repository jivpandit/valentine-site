import streamlit as st

st.set_page_config(page_title="For Kirti ❤️", page_icon="❤️")

st.markdown("""
<style>
.big {font-size: 52px; text-align:center; color:#ff4b6e; font-weight:700;}
.sub {font-size: 22px; text-align:center; color:#444;}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big'>Happy Valentine’s Day to My Forever Valentine, Kirti ❤️</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>For Kirti — made with love by Jivishaa 💌</div>", unsafe_allow_html=True)

st.write("")

st.markdown("### A little note for you")
st.write("""
Kirti,

I wanted to make something meaningful for you.
You make my days brighter and my life lighter.
I’m really grateful for you, and every day with you is like Valentine’s Day! 
You deserve all the love and happiness in the world, and I hope this little surprise brings a smile to your face.
I love you so much!! One Valentine's down, forever to go. 

Happy Valentine’s Day.
""")

if st.button("Open your surprise 🎁"):
    st.balloons()
    st.success("I love you so much. Let’s do a cozy dinner and movie date for our first long-distance Valentine’s Day ❤️")
