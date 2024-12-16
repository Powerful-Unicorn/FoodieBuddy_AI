# FoodieBuddy_AI
이 레포지토리는 앱 서비스 FoodieBuddy의 AI기술 구현을 위한 코드입니다.
로컬 환경에서 구현할 수 있는 코드를 포함하고 있습니다.

gpt-4o api를 활용해 채팅의 전반적인 틀을 잡았으며, 이에 더하여 stable diffsuion 이미지 생성모델, mysql 데이터베이스, 농촌진흥청 식재료 api를 활용하여 채팅 기능을 완성하였습니다.
gpt-4o와 농촌 진흥청 식재료 api를 활용하기 위해서는 api key가 필요합니다.

각각의 키는 아래에서 발급받을 수 있습니다.
gpt-4o api key 발급: https://platform.openai.com/docs/api-reference/introduction
농촌 진흥청 식재료 api key 발급: https://www.data.go.kr/index.do

아래 두 개의 디렉토리로 구성되어 있습니다.
### functions
: 채팅 기능에 부가적인 기능에 대한 기본 코드입니다.
- finetuned_diff.py
  : 특정 음식 이미지 생성을 위해 활용하는 코드입니다.
- db_collborative filtering.py
  : 한식 메뉴 추천 기능을 위해 Collaborative filtering을 위해 활용하는 코드입니다.
- db_user_dr.py
  : 채팅 기능을 위한 프롬프팅에 사용자의 dietary restrictions를 반영하기 위해 이를 데이터베이스로부터 조회하는 코드입니다.
- ingredientsapi.py

### service_flow
: 위의 모델을 서비스에 맞추어 기능별로 통합한 코드들의 디렉토리입니다.
- recommendation.py
  : 한식 메뉴 추천 채팅을 구현한 코드입니다.
- askdish.py
  : 밑반찬 사진 설명 채팅을 구현한 코드입니다.
- askmenu.py
  : 메뉴판 사진 설명 추천 채팅을 구현한 코드입니다.
