from html.parser import HTMLParser
from urllib.parse import urljoin


class Linkextractor(HTMLParser):

    def __init__(self, base_url,  *args, **kwarg):
        super().__init__(*args, **kwarg)
        self.base_url = base_url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag not in ('link', 'script',):
            return
        attrs = dict(attrs)
        if tag == 'link':
            if 'rel' in attrs and attrs['rel'] == 'stylesheet':
                link = self._refind(attrs['href'])
                self.links.append(link)
        elif tag == 'script':
            if 'src' in attrs:
                link = self._refind(attrs['src'])
                self.links.append(link)

    def _refind(self, link):
        return urljoin(self.base_url, link)