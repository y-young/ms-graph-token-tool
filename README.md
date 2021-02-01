# ms-graph-token-tool
A tool for acquiring refresh token of Microsoft Graph API

## Prerequisites
1. Register an app in [App registrations](https://go.microsoft.com/fwlink/?linkid=2083908) of Azure Active Directory
2. Set redirect URI to `http://localhost:5000/getAToken`
3. On the **Certificates & secrets** page, create a new Client Secret
4. Note down **Application(client) ID** and **Client Secret**
5. Grant API permissions: **Files.Read**, **Files.ReadWrite**

## Usage
1. `pip install -r requirements.txt`
2. `python start.py`
3. Follow the instructions, complete the authorization in your browser
4. If succeeds, your refresh token will be displayed on the final page
