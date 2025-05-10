
import streamlit as st
import json
from datetime import datetime
from lunarcalendar import Converter, Lunar

# 读取成员数据
with open("family_members.json", "r", encoding="utf-8") as f:
    members = json.load(f)["members"]

def get_birthday_countdown(lunar_birthday):
    today = datetime.now()
    year, month, day = map(int, lunar_birthday.split('-'))
    lunar_date = Lunar(year, month, day)
    solar_date = Converter.Lunar2Solar(lunar_date)
    birthday_this_year = datetime(today.year, solar_date.month, solar_date.day)
    if birthday_this_year < today:
        lunar_next_year = Lunar(year, month, day)
        solar_next_year = Converter.Lunar2Solar(lunar_next_year)
        birthday_this_year = datetime(today.year + 1, solar_next_year.month, solar_next_year.day)
    delta = birthday_this_year - today
    return delta.days

st.title("家庭成员生日倒计时")
st.write("当前时间：", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if not members:
    st.write("当前没有家庭成员")
else:
    st.table([
        {
            "姓名": m["name"],
            "农历生日": m["lunar_birthday"],
            "剩余天数": f"{get_birthday_countdown(m['lunar_birthday'])} 天"
        }
        for m in members
    ])