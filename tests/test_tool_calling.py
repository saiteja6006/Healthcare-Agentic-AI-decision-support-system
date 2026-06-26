from app.services.tool_calling_service import (
    ToolCallingService
)

service = ToolCallingService()

result = service.execute(
    "What policy requirements are needed for MRI approval?"
)

print("\n=== RESULT ===")

print(result)