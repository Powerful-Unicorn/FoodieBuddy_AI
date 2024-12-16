# FoodieBuddy_AI
이 레포지토리는 앱 서비스 FoodieBuddy의 AI기술 구현을 위한 코드입니다.
로컬 환경에서 구현할 수 있는 코드를 포함하고 있습니다.

아래 두개의 디렉토리로 구성되어 있습니다.
### functions: 외부 모델을 활용하기 위한 기본적인 연결만을 구현한 코드들의 디렉토리입니다.
- gpt 4o (with RAG)
- fine tuned stable diffusion with LoRA
- db colloborative filtering

### service_flow: 위의 모델을 서비스에 맞추어 기능별로 통합한 코드들의 디렉토리입니다.
- recommendation
- askdish
- askmenu
