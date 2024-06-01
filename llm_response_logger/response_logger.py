
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import LLMResult
from typing import Any, Dict, List

class ResponseLogger(BaseCallbackHandler):
    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
       None

    async def on_llm_new_token(self, token: str, **kwargs) -> None:
        # we can print tokens as they are being streamed from LLM server
        None

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        print(response.flatten())
