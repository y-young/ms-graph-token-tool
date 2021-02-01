from aiohttp import web
import aiohttp
from urllib.parse import quote
import msal

ms_app = flow = None

async def getToken(request):
    code = request.query.get('code')
    result = ms_app.acquire_token_by_auth_code_flow(flow, dict(request.query))
    if "error" in result:
        return web.Response(text="An error occurred\n" + str(result))
    return web.Response(text="Your Refresh Token:\n" + result['refresh_token'])

def main():
    global ms_app, flow
    redirect_uri = 'http://localhost:5000/getAToken'
    scope = "User.ReadBasic.All Files.Read Files.ReadWrite"
    scope = scope.split(' ')
    print('Redirect URI: ' + redirect_uri)
    app_id = input('Input Application ID: ')
    app_secret = input('Input Application Secret: ')

    print('Initiating authorization flow...')
    ms_app = msal.ConfidentialClientApplication(
        app_id,
        authority='https://login.microsoftonline.com/common',
        client_credential=app_secret)
    flow = ms_app.initiate_auth_code_flow(scope, redirect_uri)
    print(
        'Please open the following link in browser to complete authorization:')
    print(flow['auth_uri'])
    print('Awaiting authorization...')

    app = web.Application()
    app.add_routes([web.get('/getAToken', getToken)])
    web.run_app(app, port=5000)

if __name__ == '__main__':
    main()