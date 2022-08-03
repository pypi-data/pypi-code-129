from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.project_info_by_name_response_200_owner import (
    ProjectInfoByNameResponse200Owner,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectInfoByNameResponse200")


@attr.s(auto_attribs=True)
class ProjectInfoByNameResponse200:
    """ """

    name: str
    team: str
    team_name: str
    priority: int
    paused: int
    expected_time: int
    is_blacklisted_from_report: int
    id: str
    owner: Union[Unset, ProjectInfoByNameResponse200Owner] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        team = self.team
        team_name = self.team_name
        priority = self.priority
        paused = self.paused
        expected_time = self.expected_time
        is_blacklisted_from_report = self.is_blacklisted_from_report
        id = self.id
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "team": team,
                "teamName": team_name,
                "priority": priority,
                "paused": paused,
                "expectedTime": expected_time,
                "isBlacklistedFromReport": is_blacklisted_from_report,
                "id": id,
            }
        )
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        team = d.pop("team")

        team_name = d.pop("teamName")

        priority = d.pop("priority")

        paused = d.pop("paused")

        expected_time = d.pop("expectedTime")

        is_blacklisted_from_report = d.pop("isBlacklistedFromReport")

        id = d.pop("id")

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, ProjectInfoByNameResponse200Owner]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = ProjectInfoByNameResponse200Owner.from_dict(_owner)

        project_info_by_name_response_200 = cls(
            name=name,
            team=team,
            team_name=team_name,
            priority=priority,
            paused=paused,
            expected_time=expected_time,
            is_blacklisted_from_report=is_blacklisted_from_report,
            id=id,
            owner=owner,
        )

        project_info_by_name_response_200.additional_properties = d
        return project_info_by_name_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
