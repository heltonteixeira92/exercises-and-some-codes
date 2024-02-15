from urllib.parse import urlparse

link = 'https://www.google.com/search?channel=fs&client=ubuntu-sn&q=random+list#ip=1'

parse_result = urlparse(link)

'''
    ParseResult(
    scheme='https',
    netloc='www.google.com',
    path='/search', params='',
    query='channel=fs&client=ubuntu-sn&q=random+list',
    fragment='ip=1')
'''