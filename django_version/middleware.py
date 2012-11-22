from sheepdog.version import get_version

class VersionInHeaderMiddleware(object):
    
    def process_response(self, request, response):
        response['X-Version-Number'] = get_version()
        return response