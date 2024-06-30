class ExampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if isinstance(response.content, str):
            response.content = response.content.encode('utf-8')  # Convert string to bytes
        return response
