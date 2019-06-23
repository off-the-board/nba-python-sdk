import json
import os

import nose
import nose.tools
import responses

from nba_sdk.statsclient import NBAStatsClient
from nba_sdk.tests.client.test_utils import get_free_port, load_json
from nba_sdk.tests.fixtures import ASSIST_LEADERS_PAYLOAD

JSON_DIR = os.path.join(os.path.dirname(__file__), "fixtures/")


class TestNBAStatsClient(object):
    base_url = "http://localhost:{port}".format(port=get_free_port())
    mock_nba_stats_client = NBAStatsClient(base_url=base_url)

    @responses.activate
    def test_assist_leaders(self):
        uri_path = "{base_url}/assistleaders?LeagueID=00&PerMode=Totals&PlayerOrTeam=Team&Season=2018-19&SeasonType" \
                   "=Regular+Season".format(base_url=self.base_url)
        response_body = load_json(os.path.join(JSON_DIR, "assist_leaders_response.json"))
        responses.add(responses.GET, uri_path, status=200, body=json.dumps(response_body),
                      content_type="application/json")
        res = self.mock_nba_stats_client.assist_leaders(ASSIST_LEADERS_PAYLOAD)
        nose.tools.assert_equal(res.status_code, 200)
        nose.tools.assert_dict_equal(res.json(), response_body)


nose.main()
