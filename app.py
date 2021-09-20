import streamlit as st
from PIL import Image
def rsize(uf,x,y):
            image = Image.open(uf)
            new_image = image.resize((x, y),resample=Image.ANTIALIAS)
            new_image.save('image_400.jpg')
def main():
    menu=["Document Maker","About"]
    st.CURRENT_THEME = "light"
    IS_DARK_THEME = False
    
    at = st.sidebar.selectbox("Menu",menu)
    if(at=="Document Maker"):
        st.title("Welcome to Document Maker .")
        st.write("This tool has been designed to format documents for various competetive exams:")
        page = st.selectbox("Choose your exam", ["NEET", "JEE","NIFT","CUSTOM"])
        if page =="NEET":
            choice=st.radio("Select Document You Want To Process :- ",["Passport Size Photo","Post Card Size Photo","Signature","Thumb Print"])
            if choice=="Passport Size Photo" :
                uf = st.file_uploader("Choose an image...", type="jpg")
                if (uf !=None):
                    st.success('Success : File Resized click download')
                    rsize(uf,500,700)
                    with open("image_400.jpg", "rb") as fp:
                        btn = st.download_button(
                            label="Download IMAGE",
                            data=fp,
                            file_name="MY_NEET_PASSPORT_PHOTO.jpg",
                            mime="image/jpeg"
                        )
            elif choice=="Post Card Size Photo":
                    uf = st.file_uploader("Choose an image...", type="jpg")
                    if (uf !=None):
                        rsize(uf,800,1200)
                        st.write("File Resizeing Succesfull Press Download Button Below To Download ")
                        with open("image_400.jpg", "rb") as fp:
                            btn = st.download_button(
                                label="Download IMAGE",
                                data=fp,
                                file_name="MY_NEET_POSTCARD_PHOTO.jpg",
                                mime="image/jpeg"
                            )

            elif choice=="Signature":
                uf = st.file_uploader("Choose an image...", type="jpg")
                if (uf !=None):
                    rsize(uf,250,350)
                    with open("image_400.jpg", "rb") as fp:
                        btn = st.download_button(
                            label="Download IMAGE",
                            data=fp,
                            file_name=choice+".jpg",
                            mime="image/jpeg"
                        )
                
            elif choice=="Thumb Print":
                uf = st.file_uploader("Choose an image...", type="jpg")
                if (uf !=None):
                    rsize(uf,250,350)
                    with open("image_400.jpg", "rb") as fp:
                        btn = st.download_button(
                            label="Download IMAGE",
                            data=fp,
                            file_name=choice+".jpg",
                            mime="image/jpeg")
        if  (page=="JEE"):
             choice=st.radio("Select Document You Want To Process :- ",["Passport Size Photo","Signature"])
             if choice=="Passport Size Photo" :
                uf = st.file_uploader("Choose an image...", type="jpg")
                if (uf !=None):
                    st.success('Success : File Resized click download')
                    rsize(uf,500,700)
                    with open("image_400.jpg", "rb") as fp:
                        btn = st.download_button(
                            label="Download IMAGE",
                            data=fp,
                            file_name="MY_NEET_PASSPORT_PHOTO.jpg",
                            mime="image/jpeg"
                        )
             elif choice=="Signature":
                uf = st.file_uploader("Choose an image...", type="jpg")
                if (uf !=None):
                    rsize(uf,250,350)
                    with open("image_400.jpg", "rb") as fp:
                        btn = st.download_button(
                                label="Download IMAGE",
                                data=fp,
                                file_name=choice+".jpg",
                                mime="image/jpeg"
                        )
        if  (page=="NIFT"):
             choice=st.radio("Select Document You Want To Process :- ",["Passport Size Photo","Signature"])
             if choice=="Passport Size Photo" :
                uf = st.file_uploader("Choose an image...", type="jpg")
                if (uf !=None):
                    st.success('Success : File Resized click download')
                    rsize(uf,500,700)
                    with open("image_400.jpg", "rb") as fp:
                        btn = st.download_button(
                            label="Download IMAGE",
                            data=fp,
                            file_name="MY_NEET_PASSPORT_PHOTO.jpg",
                            mime="image/jpeg"
                        )
             elif choice=="Signature":
                uf = st.file_uploader("Choose an image...", type="jpg")
                if (uf !=None):
                    rsize(uf,250,350)
                    with open("image_400.jpg", "rb") as fp:
                        btn = st.download_button(
                                label="Download IMAGE",
                                data=fp,
                                file_name=choice+".jpg",
                                mime="image/jpeg"
                        )
        if  (page=="CUSTOM"):
            xx = int(st.text_input("Enter width in pixels", 500))
            yy= int(st.text_input("Enter height in pixels", 700))
            uf = st.file_uploader("Choose an image...", type="jpg")
            if (uf !=None):
                    st.success('Success : File Resized click download')
                    rsize(uf,xx,yy)
                    with open("image_400.jpg", "rb") as fp:
                        btn = st.download_button(
                            label="Download IMAGE",
                            data=fp,
                            file_name="MY_NEET_PASSPORT_PHOTO.jpg",
                            mime="image/jpeg"
                        )
                
main()