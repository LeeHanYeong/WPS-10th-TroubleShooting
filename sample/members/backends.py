from django.contrib.auth import get_user_model

User = get_user_model()


class SocialBackend:
    def authenticate(self, request, type, unique_user_id, name):
        """

        :param request:
        :param type: 어떤 유형의 소셜로그인인지
        :param unique_user_id: 클라이언트가 OAuth를 통해 가져온 Unique user id
        :return: User object
        """
        # 추가정보 필요없이 유저를 생성하면 되는 경우
        user, user_created = User.objects.update_or_create(
            type=type,
            username=unique_user_id,
            defaults={
                'name': name,
            }
        )
        return user

        # 추가정보가 필요한 경우 (인증 실패처리 해야함)
        if type == User.TYPE_DJANGO:
            return None

        try:
            user = User.objects.get(
                type=type,
                username=unique_user_id,
            )
            return user
        except User.DoesNotexist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
