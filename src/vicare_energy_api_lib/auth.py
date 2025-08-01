from aiohttp import ClientSession, ClientResponse


class Auth:
    """Authentication wrapper for making authenticated HTTP requests."""

    def __init__(self, websession: ClientSession, host: str, access_token: str):
        """Initialize the authentication wrapper."""
        
        self.websession = websession
        self.host = host
        self.access_token = access_token

    async def request(self, method: str, path: str, **kwargs) -> ClientResponse:
        """Make an authenticated HTTP request."""
    
        # Extract any existing headers from kwargs, or use empty dict if none provided
        if headers := kwargs.pop("headers", {}):
            headers = dict(headers)  # Convert to mutable dict copy
        
        # Add the Bearer token to the authorization header
        # This is required for OAuth 2.0 / JWT authentication
        headers["authorization"] = f"Bearer {self.access_token}"

        # Make the actual HTTP request with the authenticated headers
        # Combine host + path to form the complete URL
        return await self.websession.request(
            method, f"{self.host}/{path}", **kwargs, headers=headers,
        )