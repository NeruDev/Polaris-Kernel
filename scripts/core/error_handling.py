# yaml_frontmatter:
#   id: 'error_handling'
#   title: 'Gestor unificado de errores y recolección de incidencias'
#   tags: ['core', 'error-handling']


class MathKernelError(Exception):
    """Base para todas las excepciones del proyecto."""

    pass


class FileOperationError(MathKernelError):
    """Error relacionado con el sistema de archivos."""

    pass


class ProcessingError(MathKernelError):
    """Error en la lógica de procesamiento de datos."""

    pass


class ErrorCollector:
    """Recolector centralizado para el pipeline de build."""

    def __init__(self):
        self.errors = []
        self.has_critical_errors = False

    def add(self, stage: str, exception: Exception, critical: bool = False):
        self.add_message(stage, str(exception), critical)

    def add_message(self, stage: str, message: str, critical: bool = False):
        self.errors.append({"stage": stage, "message": message, "critical": critical})
        if critical:
            self.has_critical_errors = True

    @property
    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def format_summary(self) -> list[str]:
        summary = []
        for err in self.errors:
            prefix = "[CRITICAL]" if err["critical"] else "[WARN]"
            summary.append(f"{prefix} [{err['stage']}] {err['message']}")
        return summary
