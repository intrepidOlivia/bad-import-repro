import uvicorn
import sys

print('Main process running.')

import pkg_resources
print('pkg_resources path:', sys.modules['pkg_resources'])
print('sys.executable:', sys.executable)


async def run(scope, receive, send):
    print('Uvicorn process running')


if __name__ == "__main__":
    uvicorn.run(
        'src.repro:run',
        host='0.0.0.0',
        port=9000,
        reload=True
    )
