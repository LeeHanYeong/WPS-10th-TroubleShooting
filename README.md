# WPS 10기 trouble-shooting

## Room-Reservation

중개모델(Intermediate model)을 사용합니다

<https://docs.djangoproject.com/en/2.2/topics/db/models/#extra-fields-on-many-to-many-relationships>

Room

- `booker_set` = MTM(User, through='Reservation')

Reservation

- User
- Room
- 그 외 extra fields

장점

- Room에 해당하는 Reservation을 만들면, 자동으로 `booker_set` 사용가능



### 위 경우 예약이 가능한지 여부

Reservation

- room

- start_date
- end_date

클라이언트의 요청

ex) 2019-07-18 ~ 2019-07-21이 Room(pk: 356)에 대해서 가능하냐?

시작/종료가 주어짐

start_date가 종료보다 크거나 같으면 무조건 가능

end_date가 시작보다 작거나 같으면 무조건 가능

start_date가 시작보다 작은경우에는, end_date가 시작보다 작은 경우만 가능

end_date가 종료보다 큰 경우에는, start_date가 종료보다 큰 경우만 가능



start_date가

- 17 (end_date가 18이하면 가능)
- 18 x
- 19 x
- 20 x
- 21 o

end_date가 

- 18 o
- 19 x
- 20 x
- 21 x
- 22 ? (start_date가 21이상이면 가능, 아니면 불가능)

Reservation.objects.filter(

​	room=356,

​	

)



## Stay Search

filter원하는 조건

- address (문자열)

Stay.objects.filter(address__icontains=key)



StayListAPIView(generics.ListAPIView)를 사용할 때

- address라는 값을 `query_params`로 전달받음
  `/api/stay/?address=성수동`
- 받은 `query_params` 를 사용해서 `get_queryset()` 을 재정의

<https://www.django-rest-framework.org/api-guide/filtering/>



## 배포관련

- EC2 (서버 컴퓨터)
- Nginx (웹 서버)
  - 설정파일: `/etc/nginx/sites-available/default`
    - `server_name`
      - 어떤 Host명으로 접속이 되었는지를 구분
      - 커스텀 도메인을 사용한다면 공백으로 구분해서 추가
        `server_name abc.com www.abc.com`
- uWSGI (WSGI)
  - 설정파일: `/var/www/django/ini/uwsgi.ini`
  - 웹 서버와 웹 애플리케이션간의 중간 연결을 담당
  - 웹 서버와 애플리케이션간에 Unix socket을 사용해서 서로의 데이터를 주고받도록 해줌
    - 소켓파일 위치: `/var/www/django/run/uwsgi.sock`
- Django



## DRF 규칙

GenericAPIView를 쓸 경우 재정의하면 안되는 함수들

- get, post, patch, put, delete
  - 아예 건드리지 마세요

- list, retreive
  - get_queryset재정의 또는 filterset_fields또는 FilterSet을 사용
- create
  - perform_create를 사용
- update
  - perform_update를 사용
- destroy
  - perform_destory를 사용



## 자잘한 팁

### [gitignore.io](<https://gitignore.io/>)

`.gitignore` 만들 때 씁시다



### PyCharm Command line launcher

`Tools` -> `Create Command-line launcher`

사용시

(원하는 위치로 shell에서 이동 후)`charm .`



### zsh (linux)

```
# zsh 설치
sudo apt-get install zsh

# oh-my-zsh 설치
sudo curl -L http://install.ohmyz.sh | sh
```



### mac개발환경 구축

<https://subicura.com/2017/11/22/mac-os-development-environment-setup.html>

SpaceVim깔면 엄----청나게 무거우니까 저거만빼고 해보세요



### Django models문서

<https://lhy.kr/django-introduction-to-models>

이거는 다 읽고나서 개발하시면 좋습니다



### Pycharm - Code Reformat

자동으로 PEP8에 맞게 코드를 정렬&수정시켜줍니다



### choices사용시

CharField사용을 추천드립니다

`(1, '집'), (2, '학원)`

이 방식보다는

`('house', '집'), ('academy', '학원')`

위 같은 형식이 실제 DB데이터를 보기도 훨씬 좋고, 클라이언트에 문서로 제공할때도 쉽습니다



### PostgreSQL GUI

<https://www.pgadmin.org/>



### shell_plus를 JupyterNotebook으로 실행하기

```shell
manage.py shell_plus --notebook
```

