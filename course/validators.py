from rest_framework.serializers import ValidationError


class YoutubeValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if dict(value).get(self.field) is None:
            return value
        elif dict(value).get(self.field).startswith('https://www.youtube.com/'):
            return value
        else:
            raise ValidationError(f'{self.field} must start with https://www.youtube.com/')

