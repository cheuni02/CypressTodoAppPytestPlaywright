# conftest.py
import os
import pytest

# -------------------------
# Runtime switches (env)
# -------------------------
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
SLOW_MO = int(os.getenv("SLOW_MO", "0"))
RECORD_VIDEO = os.getenv("RECORD_VIDEO", "false").lower() == "true"
BASE_URL = os.getenv("BASE_URL", "https://example.cypress.io/")

# -------------------------
# Browser launch config
# -------------------------
@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """
    Equivalent of Playwright Test's:
      use: { headless, slowMo }
    """
    browser_type_launch_args["headless"] = HEADLESS
    browser_type_launch_args["slow_mo"] = SLOW_MO
    return browser_type_launch_args


# -------------------------
# Browser context config
# -------------------------
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Equivalent of Playwright Test's:
      use: { viewport, video, baseURL }
    """
    browser_context_args["viewport"] = {"width": 1280, "height": 800}
    browser_context_args["base_url"] = BASE_URL
    browser_context_args["ignore_https_errors"] = True

    if RECORD_VIDEO:
        browser_context_args["record_video_dir"] = "videos/"

    return browser_context_args

# -------------------------
# Test data reusable fixtures
# -------------------------

@pytest.fixture(scope="session")
def todosListFixture():
    return [
            "feed the goldfish",
            "call your best friend",
            "have a haircut",
            "cook your girlfriend something nice",
            "fill up the petrol",
            "take the trash out",
            "jog up to 5km"
        ]