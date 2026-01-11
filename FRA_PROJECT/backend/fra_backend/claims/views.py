from rest_framework.decorators import api_view
from rest_framework.response import Response
from .db import claims_collection


claims = [
    {"id": "CLM001", "status": "Pending"},
    {"id": "CLM002", "status": "Approved"},
    {"id": "CLM003", "status": "Pending"},
]



@api_view(["POST"])
def update_claim(request):
    cid = request.data.get("id")
    new_status = request.data.get("status")

    for c in claims:
        if c["id"] == cid:
            c["status"] = new_status
            return Response({"message": "Updated"})

    return Response({"error": "Claim not found"})


@api_view(['POST'])
def submit_claim(request):
    data = request.data
    data["status"] = "Pending"
    claims_collection.insert_one(data)
    return Response({"message": "Claim Submitted Successfully"})


@api_view(['GET'])
def get_claims(request):
    claims = list(claims_collection.find({}, {"_id": 0}))
    return Response(claims)


@api_view(['POST'])
def update_status(request):
    name = request.data.get("name")
    new_status = request.data.get("status")

    claims_collection.update_one(
        {"name": name},
        {"$set": {"status": new_status}}
    )

    return Response({"message": "Status Updated"})
