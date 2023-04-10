"""
Main flask app.
"""

from matokidata import matokidata


@matokidata
class Position:
    name: str
    lon: float
    lat: float


web_app.add_url_rule(
    '/redis/',
    view_func=RedisAPI.as_view('redis_handler'),
    methods=['GET', 'POST', 'DELETE'])

web_app.add_url_rule(
    '/tables/',
    view_func=CheckTablesAPI.as_view('tables_check'),
    methods=['GET'])

web_app.add_url_rule(
    '/tables/reload/<mapping_id>/',
    view_func=CheckTablesAPI.as_view('reload_table'),
    methods=['POST'])

web_app.add_url_rule(
    '/accountshare/',
    view_func=AccountShareCheckerAPI.as_view('shares_check'),
    methods=['GET']
)

web_app.add_url_rule(
    '/share_cleanup/',
    view_func=RemoveTacsAPI.as_view('cleanup_share'),
    methods=['POST']
)

if __name__ == '__main__':
    web_app.run()
