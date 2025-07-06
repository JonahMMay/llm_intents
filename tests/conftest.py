# tests/conftest.py
# pylint: disable=protected-access,redefined-outer-name
"""Global fixtures for LLM Intents integration tests."""

import pytest
from homeassistant.core import HomeAssistant
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.llm_intents import DOMAIN

from . import async_init_integration, patch_async_setup_entry

pytest_plugins = "pytest_homeassistant_custom_component"

pytestmark = pytest.mark.allow_socket


@pytest.fixture
def mock_config_entry():
    """Return a MockConfigEntry for llm_intents with minimal required data."""
    return MockConfigEntry(
        domain=DOMAIN,
        data={
            "api_key": "dummy_key",
            "num_results": 2,
            "country_code": "US",
            "latitude": 0.0,
            "longitude": 0.0,
            "timezone": "UTC",
        },
    )

@pytest.fixture
async def init_integration(
    hass: HomeAssistant, mock_config_entry: MockConfigEntry
) -> MockConfigEntry:
    """
    Set up the LLM Intents integration for testing.

    Patch async_setup_entry so Home Assistant will accept our entry,
    then initialize the integration.
    """
    with patch_async_setup_entry(enabled=True):
        await async_init_integration(hass, mock_config_entry)

    return mock_config_entry
