import json

from tests.integration.long_callback.utils import setup_long_callback_app


def test_lcbc012_long_callback_ctx(dash_duo, manager):
    with setup_long_callback_app(manager, "app_callback_ctx") as app:
        dash_duo.start_server(app)
        dash_duo.find_element("button:nth-child(1)").click()
        dash_duo.wait_for_text_to_equal("#running", "off")

        output = json.loads(dash_duo.find_element("#result").text)

        assert output["triggered"]["index"] == 0
