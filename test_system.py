import pytest
import subprocess

def test_full_pipeline():
    result = subprocess.run(["python", "ml_model.py"], capture_output=True, text=True)
    assert "Mean Squared Error" in result.stdout
    assert "R-squared" in result.stdout
