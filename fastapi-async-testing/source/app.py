from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    """Root endpoint handler"""
    return {'message': "KernelCI API"}