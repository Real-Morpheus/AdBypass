
import random
import streamlit as st
from PyBypass.main import BypasserNotFoundError, UnableToBypassError, UrlConnectionError
import PyBypass as bypasser

st.set_page_config(page_title="URL Bypasser", page_icon='🧊',
                   layout="centered", initial_sidebar_state="auto",    menu_items={
                       'Get Help': 'https://telegram.me/RealMorpheuss',
                       'Report a bug': "https://telegram.me/RealMorpheuss",
                       'About': "This is URL Bypasser for ADLINKFLY based website. (https://github.com/real-morpheus"
                   })


def random_celeb():
    return random.choice([st.balloons()])

st.title("URL Bypasser")
st.text('Devloped By Sanchit Vishwakarma')

tab1, tab2 = st.tabs(["Bypass", "Available Websites", ])

__avl_website__ = ['try2link.com', ' adf.ly', ' bit.ly', ' ouo.io', ' ouo.press', ' shareus.in', ' shortly.xyz', ' tinyurl.com', ' thinfi.com', ' hypershort.com ', 'safeurl.sirigan.my.id', ' gtlinks.me', ' loan.kinemaster.cc', ' theforyou.in', ' linkvertise.com', ' shorte.st', ' earn4link.in', ' tekcrypt.in', ' link.short2url.in', ' go.rocklinks.net', ' rocklinks.net', ' earn.moneykamalo.com', ' m.easysky.in', ' indianshortner.in', ' open.crazyblog.in', ' link.tnvalue.in',' shortingly.me', ' open2get.in', ' dulink.in', ' bindaaslinks.com', ' za.uy', ' pdiskshortener.com', ' mdiskshortner.link', ' go.earnl.xyz', ' g.rewayatcafe.com', ' ser2.crazyblog.in', ' bitshorten.com', ' rocklink.in', ' droplink.co', ' tnlink.in', ' ez4short.com', ' xpshort.com', ' vearnl.in', ' adrinolinks.in', ' techymozo.com', ' linkbnao.com', ' linksxyz.in', ' short-jambo.com', ' ads.droplink.co.in', ' linkpays.in', ' pi-l.ink', ' link.tnlink.in ', ' pkin.me']
