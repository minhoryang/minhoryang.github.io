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

- Amazon Web Services (PaaS)
	- 1yr for freetier:
		- EC2(Computing) t2.micro
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

- Azure (PaaS)
	- $200 30days

- Google Cloud Platform (PaaS)
	- $300 60days

- Github (Source Repositories)
	- Max 1GiB per Repository (아마 --depth 1을 기준으로 하지 않을까?)
	- Organizations
	- Pages
		 - username.github.io 도메인 제공
		 	- 다른 CNAME 지정 가능
		 - https (wildcard) 인증서
		 - 무제한 트래픽
		 - 404 페이지 트윅 가능
		 
- Gitlab (Source Repositories)
	- Max 10GiB per Project(?)
	
- CloudFlare (CDN)
	- .

- Parse (BaaS)
	- .

- Travis CI (Continuous Integration)
	- .

- Mongolab (MongoDB)
	- .

- Google Analytics (User Analytics)
	- .

- Disqus (Web Commenting)
	- .

- Asana (Issue Tracker)
- Trello (Issue Tracker)
- Google Drive (Documents Storage)
	- .

- Landscape.io (Python Code Quality Coverage)
	- .

- Newrelic (Server Application Diagnotics)

- Sealion (Server OS Diagnotics)
	- 2 computers

- HTTPSEverywhere (Free SSL Certificate)

- 마지막으론, 당연히 Slack (Chat)

### Freebie만 모여있는 사이트들도 많네
- https://groth.supply/free
- https://www.producthunt.com/@hnshah/collections/free-stuff-for-startups
