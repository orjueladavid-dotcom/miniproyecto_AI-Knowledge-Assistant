class BootstrapAssistantService:
    async def answer(self, question: str) -> dict:
        q_lower = question.lower()
        if "pydantic" in q_lower:
            answer = "Pydantic es una biblioteca de Python para validación de datos."
        elif "asyncio" in q_lower:
            answer = "Asyncio permite escribir código concurrente usando async/await."
        elif "pytest" in q_lower:
            answer = "Pytest es un framework de pruebas para Python."
        else:
            answer = f"Respuesta simulada para: {question}"
        return {
            "answer": answer,
            "provider": "bootstrap-local",
        }


class AssistanceService:
    @staticmethod
    def answer_question(question: str) -> tuple[str, str]:
        q_lower = question.lower()
        if "pydantic" in q_lower:
            answer = "Pydantic es una biblioteca de Python utilizada para la validación de datos."
        elif "asyncio" in q_lower:
            answer = "Asyncio es la biblioteca de Python para escribir código concurrente."
        elif "pytest" in q_lower:
            answer = "Pytest es un framework de pruebas en Python."
        else:
            answer = f"Respuesta simulada para: {question}"
        return answer, "bootstrap-local"