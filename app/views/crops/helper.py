from typing import Dict

from ...utils.crops import soilType

from .schema import CropSchema

#controller helpers
def getResult(data: CropSchema):
    try:
        data = data.__dict__.values()
        result = soilType(data)
        return {
            "status": "ok",
            "message": "results",
            "result": result
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)#"something went wrong"
        }