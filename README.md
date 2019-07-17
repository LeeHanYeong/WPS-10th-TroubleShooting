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