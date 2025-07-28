import streamlit as st
from PyPDF2 import PdfReader

# إعداد الواجهة
st.set_page_config(page_title="مساعد سُدي الذكي", page_icon="🤖", layout="centered")

st.title("🤖 مساعد سُدي الذكي")
st.markdown("مرحبًا بك في مساعد سُدي لقراءة ملفات PDF والإجابة عن أسئلتك 📄💬")

# اختيار اللغة
language = st.selectbox("🌐 اختر لغة الواجهة", ["العربية", "English"])

# رفع الملف
uploaded_file = st.file_uploader("📁 ارفع ملف PDF", type="pdf")

# إدخال السؤال
question = st.text_area("❓ اكتب سؤالك عن الملف", placeholder="مثال: ما الموضوع الرئيسي في الملف؟")

# زر الإرسال
if st.button("🚀 أرسل"):
    if uploaded_file is not None and question.strip() != "":
        # قراءة محتوى PDF
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # طباعة نص وهمي بدل الاتصال بـ OpenAI
        st.success("✅ تم استقبال سؤالك!")
        st.info("⚠️ حالياً الاتصال بالنموذج الذكي غير مفعل. هذه واجهة تجريبية بانتظار تفعيل الـ API.")

        # ممكن تظهري جزء من محتوى الملف للتأكيد
        with st.expander("📄 عرض محتوى الملف (أول 1000 حرف)"):
            st.write(text[:1000])
    else:
        st.warning("يرجى رفع ملف PDF وكتابة سؤال قبل الإرسال.")
