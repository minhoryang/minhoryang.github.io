.. title: Future of Microservices Paradigm
.. slug: future-of-microservices-paradigm
.. date: 2015-10-13 22:04:11 UTC+09:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

Microservices 패러다임이 꽤나 화제였었고, 우리도 작성하는 서버의 기본구조를 비슷하게 가져갔다.
"소스코드는 한줄기로 관리하나, 각각의 모듈을 분리해서 사용할 수 있도록"
그러나 Calling Hierarchy에 따른 Dependency Injection문제나 DBaaS가 필요해 지는 등 여러가지 생각이 필요해지기에 이리저리 궁리를 하다, 우리와 비슷한 생각을 하는 아티클을 찾아 여기 공유한다. 나중에라도 잘 정리할 수 있었으면 좋겠다.

우선 우리는 기존의 환경(flask/sqlalchemy/celery/rabbitmq/postgresql/...)에 gRPC+docker+kubernetes+consul 등을 쓸 생각을 하고 있다. 물론 사심이 절반 이상이기에 경계하고있다.
(+ CiscoCloud의 MANTL이 나랑 비슷한 생각을 가지고 있어 계속 지켜보고있는 중이다)

1.  http://highscalability.com/blog/2015/10/12/making-the-case-for-building-scalable-stateful-services-in-t.html

2.  http://www.stavros.io/posts/microservices-cargo-cult/

3.  http://philcalcado.com/2015/09/08/how_we_ended_up_with_microservices.html

4.  http://dev.otto.de/2015/09/30/on-monoliths-and-microservices/

5.  https://integrate2015.sched.org/event/385d40883b82c032d15c8b705b1d420c

6.  https://inconshreveable.com/10-07-2015/the-neomonolith/

7.  https://github.com/CiscoCloud/microservices-infrastructure

