user1 = st.number_input("請輸入：剪刀：（0）、石頭（1）、布（2）->"))
import random
computer = random.randint(0,2)
if user1 == computer:
    if user1==0:
        st.write("你的輸入為：剪刀（0）")
        ![image]https://github.com/Benson911214/test/blob/main/%E4%B8%8B%E8%BC%89.png?raw=true
        st.write("隨機生成數字為：0")
        ![image]https://github.com/Benson911214/test/blob/main/%E4%B8%8B%E8%BC%89.png?raw=true
    elif user1==1:
        st.write("你的輸入為：石頭（1）");
        ![image]
        st.write("隨機生成數字為：1");
        ![image]
    else:
        st.write("你的輸入為：布（2）");
        ![image]https://github.com/Benson911214/test/blob/main/%E4%B8%8B%E8%BC%89%20(1).png?raw=true
        st.write("隨機生成數字為：2");
        ![image]https://github.com/Benson911214/test/blob/main/%E4%B8%8B%E8%BC%89%20(1).png?raw=true
    st.write("啊哈，是平局！");
elif user1 == 0 and computer == 1:
    st.write("你的輸入為：剪刀（0）");
    ![image]https://github.com/Benson911214/test/blob/main/%E4%B8%8B%E8%BC%89.png?raw=true
    st.write("隨機生成數字為：1");
    ![image]
    st.write(("哈哈，你輸了"));
elif user1 == 0 and computer == 2:
    st.write("你的輸入為：剪刀（0）");
    ![image]https://github.com/Benson911214/test/blob/main/%E4%B8%8B%E8%BC%89.png?raw=true
    st.write("隨機生成數字為：2");
    ![image]https://github.com/Benson911214/test/blob/main/%E4%B8%8B%E8%BC%89%20(1).png?raw=true
    st.write(("恭喜你贏啦！"));
elif user1 == 1 and computer == 0:
    st.write("你的輸入為：石頭（1）");
    ![image]
    st.write("隨機生成數字為：0");
    ![image]https://github.com/Benson911214/test/blob/main/%E4%B8%8B%E8%BC%89.png?raw=true
    st.write(("恭喜你贏啦！"));
elif user1 == 1 and computer == 2:
    st.write("你的輸入為：石頭（1）");
    ![image]
    st.write("隨機生成數字為：2");
    ![image]https://github.com/Benson911214/test/blob/main/%E4%B8%8B%E8%BC%89%20(1).png?raw=true
    st.write(("哈哈，你輸了"));
elif user1 == 2 and computer == 0:
    st.write("你的輸入為：布（2）");
    ![image]https://github.com/Benson911214/test/blob/main/%E4%B8%8B%E8%BC%89%20(1).png?raw=true
    st.write("隨機生成數字為：0");
    ![image]https://github.com/Benson911214/test/blob/main/%E4%B8%8B%E8%BC%89.png?raw=true
    st.write(("哈哈，你輸了"));
elif user1 == 2 and computer == 1:
    st.write("你的輸入為：布（2）");
    ![image]https://github.com/Benson911214/test/blob/main/%E4%B8%8B%E8%BC%89%20(1).png?raw=true
    st.write("隨機生成數字為：1");
    ![image]
    st.write(("恭喜你贏啦"))
