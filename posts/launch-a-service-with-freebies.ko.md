<!-- 
.. title: 무료 서비스들로 서비스 하나를 런치할 수 있지 않을까?
.. slug: launch-a-service-with-freebies
.. date: 2015-10-22 00:29:41 UTC+09:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

시중에 생각외로 무료 서비스들이 많이 나와있다. 그걸 조합하면 큰 서비스가 하나 튀어나오지 않을까?
### 무료인 서비스들을 쭉 나열해보자

- [Amazon Web Services](https://aws.amazon.com/ko/free/) (PaaS)
	- 1yr for freetier:
		- EC2(Computing) t2.micro
			- Burst Mode라고 CPU Credit을 관리해 줘야한다
			- 그러니까 찰랑찰랑하게는 오래 쓸 수 있지만, 오버파워하게는 얼마 못가게 쓰라고 하는 것
		- EBS(Computing Storage) 30GiB
		- S3(Object Storage) 5GiB (Get 2만건, Put 2천건)
		- RDS(DB) t2.micro 20GiB + 백업용 20GiB
		- CloudFront(CDN) 50GB, HTTP/S 요청 2백만건 (매월이 아닌 듯)
		- ELB(Load Balancer) 매월 15GiB 처리
		- ElasticCache t2.micro
		- ElasticSearch t2.micro + 10GiB EBS
		- API Gateway 매월 1백만 건
		- IoT 매월 250,000건
			- 설마 이걸 JS에서 쓸 일이 있을까?ㄷㄷ 싶지만 JS가되니 넣어놓음.
		- 매월 15GiB 데이터 전송
			- 이게 어떤식으로 책정되는지가 관건일 듯.
	- freetier coverage:
		- DynamoDB 25GiB, Read/Write 25 units (단위주의)
		- Congnito (BaaS 인듯) 무제한 사용자처리,  클라우드 10GiB, 동기화(?) 월별 1백만번
			- 얘도 Javascript됨ㅋㅋㅋㅋ
		- CloudWatch (Log Alarm)
		- SES (Email) 월별 6.2만건 수신, 1천건 송신
			- 송신도 자동화하게?ㄷㄷ
		- SWF (Workflow) 워크플로우실행 1천건, ... (알아봐야함)
		- SQS/SNS (Queue/Push) 1백만건
		- Lambda (Func) 월별 1백만건
		- CodePipeline (?) 월별 1개
	- CloudFormation 를 통해 json형식으로 관리할 수 있음.

- [Azure](https://azure.microsoft.com/ko-kr/pricing/free-trial/) (PaaS)
	- $200 30days

- [Google Cloud Platform](https://cloud.google.com/free-trial/) (PaaS)
	- $300 60days

- [Github](https://github.com) (Source Repositories)
	- Max 1GiB per Repository (아마 --depth 1을 기준으로 하지 않을까?)
	- Organizations
	- Pages
		 - username.github.io 도메인 제공
		 	- 다른 CNAME 지정 가능
		 - https (wildcard) 인증서
		 - 무제한 트래픽
		 - 404 페이지 트윅 가능
		 
- [Gitlab](https://about.gitlab.com/gitlab-com) (Source Repositories)
	- Max 10GiB per Project(?)
	
- [CloudFlare](https://cloudflare.com/plans) (CDN)
	- DDoS 방어와 CDN
	- SSL 적용에 하루의 시간이 걸린다고 알고 있음, 대부분의 브라우저에 됨
	- Weekly 크롤링한 정보를 기반으로 서버가 죽어도 돌아갈 수 있도록 해줌
	- Max 100MiB (컨텐츠 총량을 말하는건가)
	- 엣지 지역을 못 정한다고 알고있음 (런던이라던지..)

- [Parse](https://parse.com/plans) (BaaS)
	- 초당 30리퀘스트
	- 1개의 백그라운드 작업 (매달? 동시에?)
	- 20GiB 파일 저장소
	- 20GiB DB
	- 매달 2TiB 파일 전송
	- 매달 1백개의 푸시

- [Travis CI](https://travis-ci.com/plans) (Continuous Integration)
	- 오픈소스의 경우, Fair하게 실행한다고. (그러니까 Pool이 있고, 어느정도는 이용할 수 있음)

- [Mongolab](https://mongolab.com/plans) (MongoDB)
	- 500MiB Single DB, 지역이 아마 미국이나 유럽이었던 기억이.

- [Google Analytics](https://google.com/analytics) (User Analytics)
	- 사용자의 행동 분석

- [Disqus](https://disqus.com) (Web Commenting)
	- 무료임
	- [API](https://disqus.com/api/docs/) 지원 함 ([Quota 는 한시간에 1000개](https://help.disqus.com/customer/portal/articles/1104798))
	- RSS도 지원하는데 이게 어느정도까지인지는 모르겠다. Quota는 공유하는듯?
	- [UI를 CSS로 조금 수정 가능](https://help.disqus.com/customer/portal/articles/545277)
	- [큰 사이트들은 Export XML이 안된다고 함](https://help.disqus.com/customer/en/portal/articles/1104797-importing-exporting)

- [Asana](https://asana.com/pricing) (Issue Tracker)
- [Trello](https://trello.com/pricing) (Issue Tracker)
- [Google Drive](https://support.google.com/drive/answer/2375123?hl=ko) (Documents Storage)
	- 15GiB 무료

- [Landscape.io](https://landscape.io) (Python Code Quality Coverage)
	- 오픈소스일경우 무료

- [Newrelic](https://newrelic.com/application-monitoring/pricing) (Server Monitoring)
	- 뭐든지 24시간의 기록만 저장

- [Sealion](https://sealion.com/) (Server OS Monitoring)
	- 2 computers
	- 특정 시점마다의 cui를 통한 결과를 알려줌
		- Trigger로 쓰기 좋음

- [Let's Encrypt](https://letsencrypt.org) (Free SSL Certificate)
	- 한달뒤부터 지원할 듯
	- 분명 지원안하는 구형 브라우저가 있을 듯

- [IFTTT](https://ifttt.com) (If This then That)
	- 내사랑 트리거

- 마지막으론, 당연히 [Slack](https://slack.com/pricing) (Chat)
	- 대화기록 만개 검색가능
	- 10개의 Service Integration 지원 (중요하니 영어로)

- 가 아니라 [Heroku](https://heroku.com/pricing)가 있다. 왜 이건 매번 내 눈에 안들어오는걸까.
	- 512 MiB Ram, 1 web / 1 worker
	- 30분 작동없으면 죽음ㅋㅋㅋㅋ
	- 하루에 6시간은 죽어있어야함


### Freebie만 모여있는 사이트들도 많네
- https://groth.supply/free
- https://www.producthunt.com/@hnshah/collections/free-stuff-for-startups

### 그러니까 나는
- AWS에서 필요한 거는 CloudFormation을 통해 JSON으로 묶어서 이를 Github에 올려서 잘 관리하면 되려나, 그리고 1년마다 바꿔주고 (되게 나쁜생각)
- EC2에서 필요한건 Docker 같은걸로 관리하고, Github에 보관하면 좋을듯, OS도 CoreOS같은거 쓰면 굳이 우리가 Deploy할 필요가 없음
- 이런 팁이 더 없나? 나중에 이어서 써보겠습니다.

#### 지금 만들려고 하는 타겟 프로덕트가
- 위키같이 항목이 많고,
- 매 항목마다 댓글을 달 수 있고,
- 댓글에 업 다운이 가능하며,
- 업 댓글이 많은 걸 베스트로 삼아서,
- 그 항목의 설명으로 포함되게 하는 것.

#### 이걸 이렇게 엮어서 해결 하면 안될까?
- 위의 시스템에서 실시간성을 좀 포기하면 될 것 같은데.
- 웹페이지는 Github Pages로 서빙해서
- CloudFlare로 CDN걸고 (DDoS도 방어해주겠지)
- 댓글과 업다운은 Disqus를 통해서 해결하고 (트래픽도 너네가 담당좀ㅋ 고멘)
- 우리가 주기적으로, (아마 하루에 한번을 원할테지만)
	- IFTTT + Disqus RSS (daily diff를 rss로 제공해주나)
	- Sealion (엌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ)
	- Travis CI
	- ...
- 어딘가에서, Disqus의 댓글과 업다운 현황을 긁어서,
	- AWS EC2
	- AWS Lamdba (근데 이건 짧은 시간밖에 안된다고 들었는데)
	- Parse 
	- Heroku
	- ...
- 등에서, 무엇의 도움을 받아 Like 숫자에 따라 재 편성하고,
	- AWS EC2 In-memory
	- AWS RDS DB (SQL)
	- AWS DynamoDB (NoSQL)
	- MongoLab MongoDB (NoSQL)
	- Google Drive Sheet (오예~ㅋㅋㅋㅋㅋ)
- 그 결과를 Static Blogging의 형태로 다시 저장하여
- 이를 Github Pages에 다시 푸시.

말이 되는 시나리오인가?