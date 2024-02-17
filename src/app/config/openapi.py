from pydantic import Field, EmailStr, AnyUrl
from pydantic_settings import BaseSettings


class OpenApiSettings(BaseSettings):
    title: str = Field(default="СУП", alias="OPENAPI_TITLE")
    description: str | None = Field(default=None, alias="OPENAPI_DESCRIPTION")
    licence_name: str = Field("Apache 2.0", alias="OPENAPI_LICENSE_NAME")
    licence_identifier: str = Field("MIT", alias="OPENAPI_LICENSE_IDENTIFIER")
    licence_url: AnyUrl | None = Field("https://www.apache.org/licenses/LICENSE-2.0.html", alias="OPENAPI_LICENSE_URL")
    contact_name: str | None = Field("Michael Omelchenko", alias="OPENAPI_CONTACT_NAME")
    contact_url: AnyUrl | None = Field("https://t.me/DJWOMS", alias="OPENAPI_CONTACT_URL")
    contact_email: EmailStr | None = Field("djwoms@gmail.com", alias="OPENAPI_CONTACT_EMAIL")

    @property
    def contact(self) -> dict:
        return {
            "name": self.contact_name,
            "url": self.contact_url,
            "email": self.contact_email
        }

    @property
    def config(self) -> dict:
        return {
            "name": self.licence_name,
            "url": self.licence_url,
            "identifier": self.licence_identifier
        }


settings = OpenApiSettings()
