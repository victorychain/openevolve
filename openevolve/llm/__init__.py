"""
LLM module initialization
"""

from openevolve.llm.base import LLMInterface
from openevolve.llm.ensemble import LLMEnsemble
from openevolve.llm.openai import OpenRouterLLM

__all__ = ["LLMInterface", "OpenRouterLLM", "LLMEnsemble"]
