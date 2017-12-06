from enum import Enum


class SpiderStatus(Enum):
    NAO_IMPLEMENTADO = 0
    IMPLEMENTADO = 1
    IMPLEMENTADO_PROBLEMA = 2
    OBSOLETO = 3


class DocumentoStatus(Enum):
    NAO_EXISTE = 0
    NAO_IMPLEMENTADO = 1
    IMPLEMENTADO = 2
    IMPLEMENTADO_PROBLEMA = 3
    OBSOLETO = 4


class InstanciaStatus(Enum):
    NAO_EXISTE = 0
    NAO_IMPLEMENTADO = 1
    IMPLEMENTADO = 2
