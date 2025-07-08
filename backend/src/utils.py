"""
frontend -> clerk authenticate in frontend and issue a 
jwt token -> token is sent to the backend
-> from the backend we connect to clerk using our secret key 
-> then make sure the token is valid

we can do this in 2 ways:
- Over the network -> send a request to clerk server
- Networklessy -> with secret key and public jwt we can workout in backend if the token is valid
"""

from fastapi import HTTPException
from clerk_backend_api import Clerk, AuthenticateRequestOptions
import os
from dotenv import load_dotenv

load_dotenv()

clerk_sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))


def authenticate_and_get_user_details(request):
    try:
        request_state = clerk_sdk.authenticate_request(
            request,
            AuthenticateRequestOptions(
                #where should the request come from? 
                authorized_parties=["http://localhost:5173", "http://localhost:5174"],
                jwt_key= os.getenv("JWT_KEY")
            )
        )


        if not request_state.is_signed_in:
            raise HTTPException(status_code=401, detail="Invalid Token")
        
        """
        Explain: when authenticated we get a token, in that token it contain the information of the user whose request belongs to
        (we get them accessing sub)
        """
        user_id = request_state.payload.get("sub")

        return {"user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))