# tests/test_agent.py
import pytest
from agent import greet, format_prompt

class TestGreet:
    def test_normal_name(self):
        result = greet("Funa")
        assert "Funa" in result
        assert "Hello" in result
    
    def test_empty_name(self):
        with pytest.raises(ValueError):
            greet("")   

class TestFormatPrompt:
    def test_no_prompt(self):
        result = format_prompt("Hello")
        assert len(result) == 1
        assert result[0]["role"] == "user"
        assert result[0]["content"] == "Hello"
    
    def test_with_prompt(self):
        result = format_prompt("Hello", system="Japanese")
        assert len(result) == 2
        assert result[0]["role"] == "system"
        assert result[1]["role"] == "user"
