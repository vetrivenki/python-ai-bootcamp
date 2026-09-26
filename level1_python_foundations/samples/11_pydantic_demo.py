# 11_pydantic_demo.py
# Level 1 — Topic 11: Pydantic validation, schemas, settings

from pydantic import BaseModel, Field, EmailStr, field_validator

try:
    from pydantic_settings import BaseSettings
    HAS_SETTINGS = True
except ImportError:
    HAS_SETTINGS = False


class User(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=0, le=120)

    @field_validator("name")
    @classmethod
    def name_must_be_capitalized(cls, v: str) -> str:
        if not v[0].isupper():
            raise ValueError("Name must start with capital letter")
        return v


if HAS_SETTINGS:
    class Settings(BaseSettings):
        api_key: str = "demo-key"
        debug: bool = False
        max_tokens: int = 1000

        class Config:
            env_file = ".env"


if __name__ == "__main__":
    user = User(id=1, name="Alice", email="alice@example.com", age=28)
    print(user.model_dump())

    if HAS_SETTINGS:
        settings = Settings()
        print(settings.model_dump())

    print("\n# Install if needed:")
    print("# pip install pydantic pydantic-settings email-validator")
