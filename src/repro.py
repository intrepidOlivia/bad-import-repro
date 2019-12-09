import uvicorn
import sys
import pkg_resources

print('------Repro Debug------')
print('pkg_resources path:', sys.modules['pkg_resources'])
print('sys.executable:', sys.executable)
print('Asyncpg Dialects (Should not be empty):', list(pkg_resources.iter_entry_points('sqlalchemy.dialects', 'postgresql.asyncpg')))
print('-----------------------')

async def run(scope, receive, send):
    print('Uvicorn process running')

if __name__ == "__main__":
    uvicorn.run(
        'src.repro:run',
        host='0.0.0.0',
        port=9000,
        reload=True
    )
