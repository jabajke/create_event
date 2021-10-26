import uvicorn

uvicorn.run(
    'sql_app.main:app',
    reload=True
)
