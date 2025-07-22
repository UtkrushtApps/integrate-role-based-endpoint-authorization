from fastapi import Request, HTTPException, status, Depends
from typing import Optional

# This is a simplified in-memory token store for the exercise
ISSUED_TOKENS = set()


def issue_token_for_user(username: str) -> str:
    # TODO: Implement token generation logic here - for test setup only
    # For now, just return a static value
    token = f"token-{username}"
    ISSUED_TOKENS.add(token)
    return token


def get_current_user(request: Request) -> Optional[dict]:
    # TODO: Implement robust, stateless token extraction & verification
    # This code is intentionally incomplete for the assessment
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid Authorization header")
    token = auth_header.split(" ", 1)[1]
    # Placeholder validation logic -- TODO: FIX so token validation is stateless and consistent
    if token not in ISSUED_TOKENS:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    # In actual production, decode and verify the token
    return {"username": token.replace("token-", "")}
