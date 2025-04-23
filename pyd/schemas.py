from pyd import BaseProduct
from pyd.base_models import BaseCategory
from pydantic import validator
class SchemaCar(BaseProduct):
    category: BaseCategory| None
class SchemaCategory(BaseCategory):
    cars: list[BaseProduct]