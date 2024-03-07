# from datetime import datetime
# from typing import Optional
from datetime import datetime
from typing import Optional, Type, get_type_hints, Tuple, Dict, Any

from pydantic import BaseModel, ConfigDict, Field, AliasChoices, AliasPath
from pydantic._internal._model_construction import ModelMetaclass
from pydantic.dataclasses import dataclass

# from models.models import OperatorsORM, DPC, DPCMgmn

config = ConfigDict(validate_assignment = True)

# class AllOptional(ModelMetaclass): # Этот метод предотвращает проверку данных
#     def __new__(cls, name, bases, namespaces, **kwargs):
#         annotations = namespaces.get('__annotations__', {})
#         for base in bases:
#             annotations.update(base.__annotations__)
#         for field in annotations:
#             if not field.startswith('__'):
#                 annotations[field] = Optional[annotations[field]]
#         namespaces['__annotations__'] = annotations
#         return super().__new__(cls, name, bases, namespaces, **kwargs)

class _AllOptionalMeta(ModelMetaclass):
    def __new__(self, name: str, bases: Tuple[type], namespaces: Dict[str, Any], **kwargs):
        annotations: dict = namespaces.get('__annotations__', {})

        for base in bases:
            for base_ in base.__mro__:
                if base_ is BaseModel:
                    break

                annotations.update(base_.__annotations__)

        for field in annotations:
            if not field.startswith('__'):
                annotations[field] = Optional[annotations[field]]

        namespaces['__annotations__'] = annotations

        return super().__new__(self, name, bases, namespaces, **kwargs)

# @dataclass(config=config)
class OperatorsAddDTO(BaseModel):
    model_config = ConfigDict()
    name: str
    flag: bool

    class Meta:
        orm_mode = True

# @dataclass(config=config)
class DpcsAddDTO(BaseModel):
    model_config = ConfigDict()

    id: Optional[int]
    name: Optional[int]
    abcdef: Optional[str]
    structurnii: Optional[str]
    zone_obslujivaniya: Optional[str]

    class Meta:
        orm_model = True
        # orm_model = "LocationsDTO"


# @dataclass(config=config)
class DpcsMgmnAddDTO(BaseModel):
    model_config = ConfigDict()

    dpc_name: Optional[str] = Field(serialization_alias='name', validation_alias=AliasChoices('name', AliasPath('dpc_name')))
    opc: Optional[str]
    kommutator: Optional[str]
    name_trank: Optional[str]
    region_kommutatora: Optional[str]
    region_shluza: Optional[str]
    uroven_prisoedineniya: Optional[str]

    class Meta:
        orm_model = True

# @dataclass(config=config)
class LocationsAddDTO(BaseModel):
    model_config = ConfigDict()

    name: str

# @dataclass(config=config)
class EmailsOperAddDTO(BaseModel):
    model_config = ConfigDict()

    email: str
    operator_id: int

    class Config:
        from_attributes = True

class EmailsOperDTO(EmailsOperAddDTO):
    id: int

class LocationsDTO(LocationsAddDTO):
    id: int

class OperatorsDTO(OperatorsAddDTO):
    id: int
    emails: Optional ["EmailsOperDTO"]


class DpcsDTO(DpcsAddDTO):
    id: Optional [int]
    operators: "OperatorsDTO"
    locations: "LocationsDTO"


class DpcsMgmnDTO(DpcsMgmnAddDTO):
    id: Optional [int]
    operators_mgmn: "OperatorsDTO" = Field(
        alias='operators',
        serialization_alias='operators',
        validation_alias=AliasChoices('operators', AliasPath('operators_mgmn')))


class DpcsRelDTO(DpcsDTO, metaclass=_AllOptionalMeta):
    pass


class DpcsMgmnRelDTO(DpcsMgmnDTO, metaclass=_AllOptionalMeta):
    pass

# @dataclass(config=config)
class EmailsRegionRelDTO(BaseModel, metaclass=_AllOptionalMeta):
    model_config = ConfigDict()

    id: int
    region: str
    email: str


class OperatorsRelDTO(OperatorsDTO, metaclass=_AllOptionalMeta):
    count_sp: int
    dpcs: list["DpcsDTO"]
    # emails: list["EmailsOperDTO"]
    emails: "EmailsOperDTO"
    # emails: str

class OperatorsMgmnRelDTO(OperatorsDTO, metaclass=_AllOptionalMeta):
    count_sp: int
    dpcs_mgmn: list["DpcsMgmnDTO"] = Field(serialization_alias = 'dpcs')
    emails: "EmailsOperDTO"

# @dataclass(config=config)
class LogsRelDTO(BaseModel, metaclass=_AllOptionalMeta):
    model_config = ConfigDict()

    id: int
    status: str
    creator: str
    logs: str
    date_create: datetime

# class OperatorIncidentRelDTO(OperatorsDTO, metaclass=_AllOptionalMeta):
#     count_sp: int
#     dpcs: Optional["DpcsDTO"]
#     emails: Optional["EmailsOperDTO"]


# @dataclass(config=config)
class IncidentsAddDTO(BaseModel):
    model_config = ConfigDict()

    id: Optional[int]
    name: Optional[str]
    operator_id: Optional[int]
    dpc_id: Optional[int]
    operator_name: Optional[str]
    flag: Optional[bool]
    dpc_name: Optional[str]
    opc_name: Optional[str]

    class Meta:
        orm_model = True

class IncidentsDTO(IncidentsAddDTO):
    id: Optional [int]
    # operator: "OperatorIncidentRelDTO"
    # operator: "OperatorsDTO"
    dpc: "DpcsDTO"

class IncidentsRelDTO(IncidentsDTO, metaclass=_AllOptionalMeta):
    pass

# @dataclass(config=config)
class IncGasiDTO(BaseModel):
    model_config = ConfigDict()

    # id: Optional[int]
    # number_inc: Optional[str]
    # description: Optional[str]
    status: Optional[str]
    # executor: Optional[str]
    # executor_group: Optional[str]
    # influence: Optional [int]
    cause: Optional[str]
    link: Optional[str]
    # creation_time: Optional[datetime]
    parent_inc: Optional[str]
    # initiator_login: Optional[str]
    source: Optional[str]
    # executor_login: Optional[str]
    # initiator: Optional[str]
    # initiator_group: Optional[str]
    # supervisor: Optional[str]
    # supervisor_group:Optional[str]
    # supervisor_login: Optional[str]
    # ne_name: Optional[str]

    class Meta:
        orm_mode = True
    # class Config:
    #     from_attributes = True


class IncGasiRel(IncGasiDTO, metaclass=_AllOptionalMeta):
    pass