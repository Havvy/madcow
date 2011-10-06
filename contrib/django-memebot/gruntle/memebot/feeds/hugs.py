"""All links posted to #hugs"""

from gruntle.memebot.feeds import BaseFeed

class Feed(BaseFeed):

    title = 'All #hugs URLs'
    description = __doc__

    def filter(self, published_links):
        """Filter published links to the ones we care about"""
        return published_links.filter(source__type='irc', source__name='#hugs')
