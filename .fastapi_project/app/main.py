from app.routers import (
    conexao_router,
    evento_router,
    localizacao_router,
    usuario_router,
)

app.include_router(usuario_router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(evento_router, prefix="/eventos", tags=["Eventos"])
app.include_router(localizacao_router, prefix="/localizacoes", tags=["Localizacoes"])
app.include_router(conexao_router, prefix="/conexoes", tags=["Conexoes"])
