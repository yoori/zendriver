from __future__ import annotations
import warnings
from .. import cdp

class Debugger:
    def __init__(self, tab: 'Tab') -> None:
        self.tab = tab

    async def __aenter__(self):
        await self.tab.send(cdp.debugger.enable())
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.tab.send(cdp.debugger.disable())
        if exc_type and exc_val:
            raise exc_type(exc_val)

    async def pause(self) -> None:
        """Send character into the page."""
        await self.tab.send(cdp.debugger.pause())

    async def resume(self) -> None:
        """Send character into the page."""
        await self.tab.send(cdp.debugger.resume())
