import streamlit as st
user1 = st.number_input("請輸入：剪刀：（0）、石頭（1）、布（2）->")
confirm_input = st.button('輸入確認')
if confirm_input:
    from Github import Image
    scissors = Image.open(下載 (2).png)
    stone = Image.open(下載 (1).png)
    paper = Image.open(下載.png)
    import random
    computer = random.randint(0,2)
    if user1 == computer:
        if user1==0:
            st.write("你的輸入為：剪刀（0）")
            st.image(scissors)
            st.write("隨機生成數字為：0")
            st.image(scissors)
        elif user1==1:
            st.write("你的輸入為：石頭（1）");
            st.image(stone)
            st.write("隨機生成數字為：1");
            st.image(stone)
        else:
            st.write("你的輸入為：布（2）");
            st.image(paper)
            st.write("隨機生成數字為：2");
            st.image(paper)
        st.write("啊哈，是平局！");
    elif user1 == 0 and computer == 1:
        st.write("你的輸入為：剪刀（0）");
        st.image(scissors)
        st.write("隨機生成數字為：1");
        st.image(stone)
        st.write(("哈哈，你輸了"));
    elif user1 == 0 and computer == 2:
        st.write("你的輸入為：剪刀（0）");
        st.image(scissors)
        st.write("隨機生成數字為：2");
        st.image(paper)
        st.write(("恭喜你贏啦！"));
    elif user1 == 1 and computer == 0:
        st.write("你的輸入為：石頭（1）");
        st.image(stone)
        st.write("隨機生成數字為：0");
        st.image(scissors)
        st.write(("恭喜你贏啦！"));
    elif user1 == 1 and computer == 2:
        st.write("你的輸入為：石頭（1）");
        st.image(stone)
        st.write("隨機生成數字為：2");
        st.image(paper)
        st.write(("哈哈，你輸了"));
    elif user1 == 2 and computer == 0:
        st.write("你的輸入為：布（2）");
        st.image(paper)
        st.write("隨機生成數字為：0");
        st.image(scissors)
        st.write(("哈哈，你輸了"));
    elif user1 == 2 and computer == 1:
        st.write("你的輸入為：布（2）");
        st.image(paper)
        st.write("隨機生成數字為：1");
        st.image(stone)
        st.write(("恭喜你贏啦"))
