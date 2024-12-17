# FoodieBuddy_AI
이 레포지토리는 앱 서비스 FoodieBuddy의 AI기술 구현을 위한 코드입니다.<br/>
로컬 환경에서 구현할 수 있는 코드를 포함하고 있습니다.<br/>

gpt-4o api를 활용해 채팅의 전반적인 틀을 잡았으며, 이에 더하여 stable diffsuion 이미지 생성모델, mysql 데이터베이스, 농촌진흥청 식재료 api를 활용하여 채팅 기능을 완성하였습니다.<br/>
실제 코드를 실행하기 위해서는 api key와 DB 접근을 위한 password가 필요합니다.<br/>

각각의 키는 아래에서 발급받을 수 있습니다.<br/>
gpt-4o api key 발급: https://platform.openai.com/docs/api-reference/introduction<br/>
stability diffusion key 발급: https://platform.stability.ai/docs/api-reference#tag/Generate<br/>
농촌 진흥청 식재료 api key 발급: https://www.data.go.kr/index.do<br/>
(교수님께는 DB를 위한 password와 함께 메일로 따로 전달 드렸습니다.)

이 레포지토리는 아래의 두 개의 디렉토리로 구성되어 있습니다.
### Directory 1. functions
: 채팅 기능에 부가적인 기능에 대한 기본 코드입니다.
- finetuned_diff.py<br/>
  : 특정 음식 이미지 생성을 위해 활용하는 코드입니다.<br/>
    CPU에서 실행되는 환경인 경우 10번째 행에서 오류가 발생할 수 있습니다. 오류가 나는 경우 .to("cuda")를 지우면 정상적으로 실행할 수 있습니다.<br/>
    그러나 CPU환경에서는 이미지 생성에 시간이 매우 오래걸리기에 되도록이면 GPU를 사용하는 것을 추천합니다.
- db_collborative filtering.py<br/>
  : 한식 메뉴 추천 기능을 위해 Collaborative filtering을 위해 활용하는 코드입니다.<br/>
    이 코드에서는 44번쨰 행에서 DB접근을 위한 password를 입력해야 합니다.
- db_user_dr.py<br/>
  : 채팅 기능을 위한 프롬프팅에 사용자의 dietary restrictions를 반영하기 위해 이를 데이터베이스로부터 조회하는 코드입니다.<br/>
    이 코드에서는 44번쨰 행에서 DB접근을 위한 password를 입력해야 합니다.
- ingredientsapi.py<br/>
  : 채팅 기능을 위한 프롬프팅에 식재료 정보를 반영하기 위해 활용하는 코드입니다.
    이 코드에서는 5번째 행에서 농촌진흥청 식재료 데이터 요청을 위한 API key를 입력해야 합니다.

### Directory 2. service_flow
: 위의 기능들을 gpt-4o와의 채팅과 결합하여, 각 채팅 기능별로 통합한 코드들의 디렉토리입니다. '로컬' 환경에서 구현하는 코드이므로, 아래의 코드에서 사용된 stability diffusion는 api를 활용하는 버전의 코드입니다. 
- recommendation.py<br/>
  : 한식 메뉴 추천 채팅을 구현한 코드입니다.
- askdish.py<br/>
  : 밑반찬 사진 설명 채팅을 구현한 코드입니다.
- askmenu.py<br/>
  : 메뉴판 사진 설명 추천 채팅을 구현한 코드입니다.


실행 방법은 google colab을 기반으로 설명을 작성하였습니다.
## How to build
1. 이 레포지토리를 아래와 같이 clone합니다.
```bash
!git clone https://github.com/JihooChung/FoodieBuddy_AI.git
!cd FoodieBuddy_AI
```
2. 아래의 코드를 통해 파일을 하나씩 실행해볼 수 있습니다. 이떄 위의 디렉토리 설명에서 제시한 api key, password를 입력해야 정상적으로 실행됩니다.
```bash
!python 파일경로
```

## How to install
1. Python 3.8이상이 설치되어 있어야 합니다.
2. 라이브러리 설치가 필요한 경우 아래의 코드를 활용하여 설치하면 됩니다.
```bash
!pip install 라이브러리_이름
```

## Description of used open source
1. Gpt-4o api 활용
: 사용자와 실시간 대화를 통해 질문을 이해하고 적절한 응답을 생성하며, 사용자의 음식 관련 요구사항(예: 메뉴 추천, 식재료 설명 등)을 반영한 자연스러운 대화를 제공합니다.<br/>
아래의 링크에서 제시된 코드를 확장하여 채팅 코드를 작성하였습니다.<br/>
https://platform.openai.com/docs/api-reference/chat
3. Stable diffusion api 활용
: 사용자에게 메뉴를 추천 하거나 설명할 떄 사용자 이해를 돕기 위해 이미지를 생성합니다.<br/>
아래의 링크에서 제시된 코드를 활용하여 이미지 생성 코드를 작성하였습니다.<br/>
https://platform.openai.com/docs/api-reference/chat
