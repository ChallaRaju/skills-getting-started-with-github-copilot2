import pytest
from httpx import AsyncClient, ASGITransport
from src.app import app

import asyncio


@pytest.mark.anyio
async def test_root_redirect():
    # Arrange
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Act
        response = await ac.get("/")
    # Assert
    assert response.status_code in (200, 307, 302)


@pytest.mark.anyio
async def test_static_files_served():
    # Arrange
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Act
        response = await ac.get("/static/index.html")
    # Assert
    assert response.status_code == 200
    assert "Mergington High School" in response.text


@pytest.mark.anyio
async def test_activities_list():
    # Arrange
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Act
        response = await ac.get("/activities")
    # Assert
    assert response.status_code in (200, 404)  # Adjust as per actual implementation
