from vicare_energy_api_lib.auth import Auth
import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_auth_request_adds_authorization_header():
    mock_session = AsyncMock()
    auth = Auth(mock_session, "http://host", "token123")
    await auth.request("GET", "path")
    args, kwargs = mock_session.request.call_args
    assert kwargs["headers"]["authorization"] == "Bearer token123"