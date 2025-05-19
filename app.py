import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import pandas_bokeh

def main():
    # 글 쓰기(링크 삽입)
    st.title('경희대 인근 가성비 좋은 맛집 늘어 ... 건강식은 "글쎄"')

    st.header('대학생 대상 저렴하고 맛있는 음식점 인기')
    st.subheader('분식, 중식, 한식에 일식까지 다양한 음식 싸게 제공')
    st.subheader('축제 행사에 햄버거-핫도그 푸드트럭도 등장')
    st.write(
        '''경희대 인근에는 최근 가성비 좋은 맛집들이 속속 들어서며 학생들 사이에서 인기를 끌고 있다. 한정된 대학생 지갑사정에 맞는 저렴한 가격과 다양하고 퀄리티 높은 메뉴로 입소문이 나면서 성업 중인 것이다.
    이처럼 경희대 주변에는 학생들 사이에서 입소문이 자자한 가성비 맛집들이 많다. 뿐만 아니라 대학 축제 때면 다양한 [푸드트럭](https://namu.wiki/w/%ED%91%B8%EB%93%9C%20%ED%8A%B8%EB%9F%AD)들도 찾아와 저렴하고 맛있는 메뉴를 선보이며 큰 인기를 끈다.
    최근 물가상승으로 인해 외식비 부담이 큰 대학생들에게 이런 가성비 높은 맛집과 푸드트럭은 환영받을 만하다.''' )

    # 사진 삽입
    st.image('/content/drive/MyDrive/2024_1_class/data_jour/photo1.jpg', caption='지난 4월20일 경희대 교내에서 학생들이 푸드트럭에서 음식을 구매하고 있다')
    st.image('/content/drive/MyDrive/2024_1_class/data_jour/photo2.jpg', caption='경희대 근처 맛집 지도(--- 제공)')

    # 데이터 보여주기
    df_blogs = pd.read_excel('/content/drive/MyDrive/2024_1_class/data_jour/data_blogs.xlsx', index_col=0)
    st.write('취재팀은 네이버 블로그에서 "경희대 맛집"을 검색해 글 300개를 수집했다', df_blogs)

    df_keywords = pd.read_excel('/content/drive/MyDrive/2024_1_class/data_jour/data_keywords.xlsx', index_col=0)
    st.write('블로그 글에서 가장 많이 출현한 단어는 ~~~ 설명~~~', df_keywords)

    # 워드클라우드
    st.write('주요  단어들을 워드클라우드로 보여주면 다음과 같다')
    st.image('/content/drive/MyDrive/2024_1_class/data_jour/wordcloud.png')

    # 연결망 분석
    st.write(
        '''취재팀은 주요  단어들 간에 공동출현하는 관계를 바탕으로 의미연결망을 그려보았다.
                분석결과, ~~설명~~''' )
    st.image('/content/drive/MyDrive/2024_1_class/data_jour/network.png')

    # 교통사고 데이터
    df_accident = pd.read_excel('/content/drive/MyDrive/2024_1_class/data_jour/data_traffic_accidents.xlsx', index_col=0)
    st.write('다음 데이터는 전국의 교통사고를 지역별로 집계한 것이다', df_accident)

    # 검색어 입력 받아 출력
    query = st.text_input('이 곳에 지역명(시군구동읍면)을 입력하면 관련 데이터만 검색해 보여줍니다', key='region1_input')
    if query:
        df_accident['select1'] = df_accident['사고지역위치명'].apply(lambda x: 1 if query in x else 0)
        st.write('검색 결과:', df_accident[df_accident['select1'] == 1])

    # 교통사고 유형과 연도에 따른 pivot table
    df_pivot = df_accident.pivot_table(index='사고유형구분', columns='사고연도', values='사고건수', aggfunc='sum')
    st.write('다음 표는 교통사고 건수를 유형과 연도에 따라 구분한 것이다', df_pivot)

    # 검색어 입력 받아 pivot table 출력
    query_pivot = st.text_input('이 곳에 지역명(시군구)을 입력하면 관련 데이터만 검색해 보여줍니다', key='region2_input')
    if query_pivot:
        df_accident['select2'] = df_accident['사고지역위치명'].apply(lambda x: 1 if query_pivot in x else 0)
        df_pivot_sel = df_accident[df_accident['select2'] == 1].pivot_table(
            index='사고유형구분', columns='사고연도', values='사고건수', aggfunc='sum')
        st.write('검색 결과:', df_pivot_sel)

    # pandas_bokeh 그래프 (pandas_bokeh import 필요)
    # st.write('전국 교통사고 데이터에 따르면, 사고건수와 중상자수는 밀접한 관련을 맺고 있다.')
    # p_scatter = df_accident.plot_bokeh.scatter(
    #     x="사고건수",
    #     y="중상자수",
    #     title="사고건수와 중상자수",
    #     size=10,
    #     hovertool_string="""<h6>위치:@{사고지역위치명}</h6>"""
    # )
    # st.bokeh_chart(p_scatter, use_container_width=True)

    # 선택한 조건에 따라 그래프 보여주기
    option = st.selectbox(
        '연도를 선택하면 해당 시기의 그래프를 보여줍니다',
        sorted(df_accident['사고연도'].unique()), key='year_input')
    df_sel = df_accident[df_accident['사고연도'] == option]
    # p_scatter_sel = df_sel.plot_bokeh.scatter(
    #     x="사고건수",
    #     y="중상자수",
    #     title=f"{option}년 사고건수와 중상자수",
    #     size=10,
    #     hovertool_string="""<h6>위치:@{사고지역위치명}</h6>"""
    # )
    # st.write('검색 결과:')
    # st.bokeh_chart(p_scatter_sel, use_container_width=True)


if __name__ == '__main__':
    main()
