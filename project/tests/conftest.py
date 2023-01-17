import os

import pytest
from app.config import Settings, get_settings
from app.server import create_application
from starlette.testclient import TestClient


def get_settings_override():
    return Settings(testing=True, database_url=os.environ.get('DATABASE_TEST_URL'))


@pytest.fixture(scope='module')
def test_app():
    # Set up
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:
        # Testing
        yield test_client
