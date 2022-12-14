from typing import TYPE_CHECKING

from loguru import logger
from vkbottle.bot import BotLabeler

from app.core import constants
from app.core.exceptions import CantGetTimePassed
from app.helpers.custom_rules import CommandListRule, GetMagicRustAPIRule
from app.helpers.filtres import PlayerFilter, RCCPlayerFilter
from app.helpers.parser import args_parser
from app.helpers.rcc_manager import rcc_manager
from app.views import NewPlayersView, RCCPlaeyrsView, StatsPlayersView

if TYPE_CHECKING:
    from vkbottle.bot import Message

    from app.services.magic_rust.MR_api import MagicRustAPI


labeler = BotLabeler()


@labeler.message(
    CommandListRule(['new', 'туц', 'новые'], prefixes=['/', '.']),
    GetMagicRustAPIRule(),
)
async def get_new_players(message: 'Message', magic_rust_api: 'MagicRustAPI') -> None:
    """Handle /new command and send new players to chat"""
    new_players = await magic_rust_api.get_online_new_players()
    if not new_players:
        return await message.answer('Новых игроков не найдено')
    new_players_with_stats = await magic_rust_api.fill_stats_for_players(new_players)

    player_filter = PlayerFilter(by_kd=1.0, by_check_on_magic=True)

    filtered_players = await player_filter.execute(new_players_with_stats)
    sorted_players = sorted(filtered_players, key=lambda player: player.stats.kd, reverse=True)
    return await message.answer(NewPlayersView(sorted_players))


@labeler.message(CommandListRule(['stats', 'стата', 'ыефеы'], prefixes=['/', '.'], args_count=1), GetMagicRustAPIRule())
async def get_big_kd_players(message: 'Message', magic_rust_api: 'MagicRustAPI', args: list | None = None) -> None:
    if args:
        kd = float(args[0])
    else:
        kd = constants.DEFAULT_BIG_KD

    players = await magic_rust_api.get_online_players()
    players_with_stats = await magic_rust_api.fill_stats_for_players(players)

    player_filter = PlayerFilter(by_kd=kd, by_check_on_magic=True)

    filtered_players = await player_filter.execute(players_with_stats)
    sorted_players = sorted(filtered_players, key=lambda player: player.stats.kd, reverse=True)
    return await message.answer(StatsPlayersView(sorted_players, kd))


@labeler.message(
    CommandListRule(['bans', 'баны', 'ифты'], prefixes=['/', '.'], args_count=1),
    GetMagicRustAPIRule(),
)
async def get_banned_players(
    message: 'Message',
    magic_rust_api: 'MagicRustAPI',
    args: list = None,
):
    try:
        time_passed = args_parser.parse_time_passed(args)
    except CantGetTimePassed:
        return await message.answer('Не правильно указано время. Используйте формат 30s, 30m, 30h, 30d, 30w, 2y.')

    try:
        online_players = await magic_rust_api.get_online_players()
    except Exception as e:
        logger.exception(e)
        return await message.answer('Ошибка при получении игроков на сервере.')
    online_players_steamids = [player.steamid for player in online_players]

    try:
        rcc_players = await rcc_manager.get_rcc_players_and_cache(online_players_steamids)
    except Exception as e:
        logger.exception(e)
        return await message.answer('Ошибка при получении данных с RCC.')

    rcc_players_filter = RCCPlayerFilter(by_seconds_passed_after_ban=time_passed)
    filtered_rcc_players = rcc_players_filter.execute(rcc_players)

    sorted_players = sorted(filtered_rcc_players, key=lambda player: len(player.bans), reverse=True)

    await message.answer(RCCPlaeyrsView(sorted_players))
