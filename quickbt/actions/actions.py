import asyncio
from winrt.windows.devices import radios

def turn_on(systray):
    asyncio.run(_action())

def turn_off(systray):
    asyncio.run(_action(False))

async def _action(power_state = True):
    all_radios = await radios.Radio.get_radios_async()
    for this_radio in all_radios:
        if this_radio.kind == radios.RadioKind.BLUETOOTH:
            if power_state:
                result = await this_radio.set_state_async(radios.RadioState.ON)
            else:
                result = await this_radio.set_state_async(radios.RadioState.OFF)
