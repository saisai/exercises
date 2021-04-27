
class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        print(dir(self))
        if hasattr(self, 'process_request'):
            print('has')
            response = self.process_request(request)
        if not response:
            print('has c')
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            print('has b')
            response = self.process_response(request, response)
        return response


class SecurityMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_request(self, request):
        print('process_request')
        return request

    def process_response(self, request, response):
        print("process_response")
        return response

t = SecurityMiddleware()
print(t)
print(dir(t))
c = t('request')
print(c)
r = t('response')
print(r)

