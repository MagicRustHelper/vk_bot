from typing import TYPE_CHECKING

from loguru import logger
from sqlalchemy.exc import IntegrityError

from app.services.storage import crud
from app.services.storage.schemas.reports import ReportsCreate
from app.services.storage.session import get_session

if TYPE_CHECKING:
    from app.core.typedefs import ReportMessage


class ReportController:
    async def add_report(self, report_message: 'ReportMessage') -> None:
        logger.debug(f'add report - {report_message}')
        obj_in_report_message = ReportsCreate(
            author_nickname=report_message.author_nickname,
            report_steamid=report_message.report_steamid,
            server_number=report_message.server_number,
        )
        async with get_session() as session:
            try:
                await crud.reports.create(session, obj_in=obj_in_report_message)
            except IntegrityError:
                logger.debug('Report already exist, skip..')
