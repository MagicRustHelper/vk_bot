from app.entities import CheckInDB, CreateCheck, ModeratorsCheck, ModeratorsCheckQuery
from app.services.api.base import BaseAPI


class CheckAPI(BaseAPI):
    async def create_check(self, steamid: str, moderator_vk_id: int, server_number: int) -> int:
        request_body = CreateCheck(steamid=steamid, moderator_vk_id=moderator_vk_id, server_number=server_number).dict(
            exclude_none=True
        )
        result = await self.client.api_POST_request('/v1/checks', body=request_body, response_model=CheckInDB)
        return result.id

    async def complete_check(self, check_id: int, is_ban: bool = False) -> CheckInDB:
        return await self.client.api_PUT_request(f'/v1/checks/{check_id}', query={'is_ban': str(is_ban)})

    async def cancel_check(self, check_id: int) -> CheckInDB:
        return await self.client.api_DELETE_request(f'/v1/checks/{check_id}')

    async def add_check(self, create_check: CreateCheck) -> int:
        result = await self.client.api_POST_request(
            '/v1/checks', body=create_check.dict(exclude_none=True), response_model=CheckInDB
        )
        return result.id

    async def get_checked_players(self, steamids: list[int]) -> dict[str, int]:
        return await self.client.api_POST_request('/v1/checks/get_checked', body=steamids, response_model=dict)

    async def get_last_check(self, steamid: str) -> CheckInDB:
        return await self.client.api_GET_request(f'/v1/checks/steamid/{steamid}', response_model=CheckInDB)

    async def get_moderator_checks(self, time_start: float, time_end: float) -> list[ModeratorsCheck]:
        query = ModeratorsCheckQuery(time_start=time_start, time_end=time_end).dict(exclude_none=True)
        return await self.client.api_GET_request(
            '/v1/checks/moderators_count',
            query=query,
            response_model=list[ModeratorsCheck],
        )
