import pytest
import structlog

from services.account import DmApiAccount

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False),
    ]
)


@pytest.fixture
def dm_account_api():
    return DmApiAccount(
        host='http://localhost:5051'
    )
