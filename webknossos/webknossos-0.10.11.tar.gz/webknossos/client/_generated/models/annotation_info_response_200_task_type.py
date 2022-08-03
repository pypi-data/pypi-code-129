from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.annotation_info_response_200_task_type_settings import (
    AnnotationInfoResponse200TaskTypeSettings,
)

T = TypeVar("T", bound="AnnotationInfoResponse200TaskType")


@attr.s(auto_attribs=True)
class AnnotationInfoResponse200TaskType:
    """ """

    id: str
    summary: str
    description: str
    team_id: str
    team_name: str
    settings: AnnotationInfoResponse200TaskTypeSettings
    recommended_configuration: str
    tracing_type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        summary = self.summary
        description = self.description
        team_id = self.team_id
        team_name = self.team_name
        settings = self.settings.to_dict()

        recommended_configuration = self.recommended_configuration
        tracing_type = self.tracing_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "summary": summary,
                "description": description,
                "teamId": team_id,
                "teamName": team_name,
                "settings": settings,
                "recommendedConfiguration": recommended_configuration,
                "tracingType": tracing_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        summary = d.pop("summary")

        description = d.pop("description")

        team_id = d.pop("teamId")

        team_name = d.pop("teamName")

        settings = AnnotationInfoResponse200TaskTypeSettings.from_dict(
            d.pop("settings")
        )

        recommended_configuration = d.pop("recommendedConfiguration")

        tracing_type = d.pop("tracingType")

        annotation_info_response_200_task_type = cls(
            id=id,
            summary=summary,
            description=description,
            team_id=team_id,
            team_name=team_name,
            settings=settings,
            recommended_configuration=recommended_configuration,
            tracing_type=tracing_type,
        )

        annotation_info_response_200_task_type.additional_properties = d
        return annotation_info_response_200_task_type

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
