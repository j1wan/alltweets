API_PARAMETERS = (
    'user_id',
    'screen_name',
    'since_id',
    'count',
    'max_id',
    'trim_user',
    'exclude_replies',
    'contributor_details',
    'include_rts',
)

USER_AGENT = 'AllTweets'

ENDPOINTS = {
    'statuses/user_timeline': ('GET', 'api'),
    'search/tweets': ('GET', 'api'),
    'followers/ids': ('GET',  'api'),
    'followers/list': ('GET',  'api'),
    'friends/ids': ('GET',  'api'),
    'friends/list': ('GET',  'api')
}