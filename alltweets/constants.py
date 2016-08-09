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

APP_ONLY_APIS = {
    'GET statuses/user_timeline',
    # 'GET statuses/retweets/:id',
    # 'GET statuses/show/:id',
    'GET statuses/retweeters/ids',
    'GET statuses/lookup',

    'GET search/tweets',

    'GET friends/ids',
    'GET followers/ids',
    'GET friendships/show',
    'GET friends/list',
    'GET followers/list',

    'GET users/lookup',
    'GET users/show',
    # 'GET users/suggestions/:slug',
    'GET users/suggestions',
    # 'GET users/suggestions/:slug/members',

    'GET favorites/list',

    'GET lists/list',
    'GET lists/statuses',  # !!!
    'GET lists/memberships',
    'GET lists/subscribers',
    'GET lists/subscribers/show',
    'GET lists/members/show',
    'GET lists/members',
    'GET lists/show',
    'GET lists/subscriptions',
    'GET lists/ownerships'

    'GET trends/place',
    'GET trends/available',
    'GET trends/closest',

    'GET application/rate_limit_status',

    'GET help/configuration',
    'GET help/languages',
    'GET help/privacy',
    'GET help/tos',
}