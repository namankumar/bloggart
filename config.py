# Name of the blog
blog_name = 'idea Lab'

# Your name (used for copyright info)
author_name = 'Naman Kumar'

# (Optional) slogan
slogan = 'dangerously convenient, surprisingly acceptable'

# The hostname this site will primarially serve off (used for Atom feeds)
#host = 'www.namank.com'
host = 'localhost:8081'

# Selects the theme to use. Theme names correspond to directories under
# the 'themes' directory, containing templates and static content.
theme = 'default'

# List of page templates
page_templates = {
	'Theme.html': 'Theme',
	'Simple.html': 'Simple',
}

# Defines the URL organization to use for blog postings. Valid substitutions:
#   slug - the identifier for the post, derived from the title
#   year - the year the post was published in
#   month - the month the post was published in
#   day - the day the post was published in
post_path_format = '/%(slug)s'

# A nested list of sidebar menus, for convenience. If this isn't versatile
# enough, you can edit themes/default/base.html instead.
sidebars = [
  ("designer", [
  	'<a href="http://www.namank.com/who">who</a>',
 	'<a href="http://www.namank.com/portfolio">portfolio</a>',
    '<a href="http://ca.linkedin.com/in/namankumar">linkedin</a>',
 ]),
 ('around', [
	'<a href="https://github.com/namankumar">open source</a>', 
	'<a href="http://www.quora.com/Naman-Kumar">quora</a>',
 	'<a href="http://www.twitter.com/naman_k">twitter</a>',
 ]),
 ('happenings', [
    '<a href="http://tedxwaterloo.com">tedXwaterloo</a>',
 ]),
]
# Number of entries per page in indexes.
posts_per_page = 10

# The mime type to serve HTML files as.
html_mime_type = "text/html; charset=utf-8"

# To use disqus for comments, set this to the 'short name' of the disqus forum
# created for the purpose.
disqus_forum = "namankumar"

# Length (in words) of summaries, by default
summary_length = 50

# If you want to use Google Analytics, enter your 'web property id' here
analytics_id = "UA-22212468-1"

# If you want to use PubSubHubbub, supply the hub URL to use here.
hubbub_hub_url = 'http://pubsubhubbub.appspot.com/'

# If you want to ping Google Sitemap when your sitemap is generated change this to True, else False
# see: http://www.google.com/support/webmasters/bin/answer.py?hl=en&answer=34609 for more information
google_sitemap_ping = True

# If you want to use Google Site verification, go to
# https://www.google.com/webmasters/tools/ , add your site, choose the 'upload
# an html file' method, then set the NAME of the file below.
# Note that you do not need to download the file provided - just enter its name
# here.
google_site_verification = None

# Default markup language for entry bodies (defaults to html).
default_markup = 'html'

# Syntax highlighting style for RestructuredText and Markdown,
# one of 'manni', 'perldoc', 'borland', 'colorful', 'default', 'murphy',
# 'vs', 'trac', 'tango', 'fruity', 'autumn', 'bw', 'emacs', 'pastie',
# 'friendly', 'native'.
highlighting_style = 'friendly'

# Absolute url of the blog application use '/blog' for host/blog/
# and '' for host/.Also remember to change app.yaml accordingly
url_prefix = ''

# Defines where the user is defined in the rel="me" of your pages.
# This allows you to expand on your social graph.
rel_me = "https://plus.google.com/113489023394453793264/about"

# For use a feed proxy like feedburne.google.com
feed_proxy = None

# To use Google Friends Connect.                                          
# If you want use Google Friends Connect, go to http://www.google.com/friendconnect/ 
# and register your domain for get a Google Friends connect ID.
google_friends_id = None
google_friends_comments = True # For comments.
google_friends_members  = True # For a members container.

# To format the date of your post.
# http://docs.djangoproject.com/en/1.1/ref/templates/builtins/#now
date_format = "d F, Y"
