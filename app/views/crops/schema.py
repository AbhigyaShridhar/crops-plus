from pydantic import BaseModel, Field

class CropSchema(BaseModel):
    soil1: float = Field(...,example=1.9)
    soil2: float = Field(...,example=1.9)
    soil3: float = Field(...,example=1.9)
    soil4: float = Field(...,example=1.9)
    soil5: float = Field(...,example=1.9)
    soil6: float = Field(...,example=1.9)
    soil7: float = Field(...,example=1.9)
    soil8: float = Field(...,example=1.9)
    soil9: float = Field(...,example=1.9)
    soil10: float = Field(...,example=1.9)
    