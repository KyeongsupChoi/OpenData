## 📶 OpenData

> Data Analysis/Data Visualization web project  
> 
> Hosted on https://kayronfalanor.pythonanywhere.com/
> 
> Calls and visualizes data from the Korean Government's OpenData portal: https://www.data.go.kr/

## 📂 Code-base structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- CSVFiles/                            # Holds csv files
   |
   |-- templates/                           # Holds html template files
   |    |
   |    |-- bar.html                        # Graph and plotly html file
   |
   |-- nhis.py                              # Define Wendler forms
   |-- main.py                              # Calls OpenData Weather API
   |
   |-- README.md                            # Standard readme documentation
   |
   |-- ************************************************************************
```

<br />

## 📚 Libraries Used

- `Plotly` - High-level, Declarative charting python library
- `Flask` - Basic Web Framework used for backend
- `Pandas` - Reading and working with CSV files
- `Requests` - Calling APIs

## 📶 오픈데이터

> 데이터 분석/ 데이터 시각화 프로젝트
>
> 라이브 사이트 https://kayronfalanor.pythonanywhere.com/
>
> 한국 정부의 OpenData 공공데이터포털에서 데이터 호출 및 시각화: https://www.data.go.kr/

## 📂 코드 기반 구조

이 프로젝트는 아래에 제시된 간단하고 직관적인 구조를 사용하여 코딩됩니다.

```bash
<프로젝트 루트>
   |
   |-- CSVFiles/                           # csv 파일 보유
   |
   |-- templates/                          # html 템플릿 파일 보유
   |    |
   |    |-- bar.html                       # 그래프 및 plotly HTML 파일
   |
   |-- nhis.py                             # 인덱스 경로에서 plotly 요소 생성
   |-- main.py                             # 날씨 공공데이터 api를 호출합니다.
   |
   |-- README.md                           # 표준 readme 문서
   |
   |-- ************************************************************************
```

<br />

## 📚 사용된 라이브러리

- `Plotly` - 상위수준, 선언적인 차트 작성을 위한 파이썬 라이브러리
- `Flask` - 백엔드에 사용되는 기본 웹 프레임워크
- `Pandas` - CSV 파일 읽기 및 작업
- `Requests` - API 호출
