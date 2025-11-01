from fastapi import Request, HTTPException


def get_current_user(request: Request):
    """Return current authenticated user from session or raise 401."""
    user_email = request.session.get('user_email')
    if not user_email:
        raise HTTPException(status_code=401, detail="Usuário não autenticado")
    return {"email": user_email}
