from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for, render_template
from flask.json import jsonify
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)

app.secret_key = os.urandom(24)


# This information is obtained upon registration of a new GitHub OAuth
# application here: https://github.com/settings/applications/new
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'


@app.route('/')
def index():
    login_status = False
    avatar = None
    if 'gh_id' in session and 'avatar' in session:
        login_status = True
        avatar = session['avatar']
    return render_template('index.html', login=login_status,avatar=avatar)


@app.route("/login")
def gh_login():
    """Step 1: User Authorization.

    Redirect the user/resource owner to the OAuth provider (i.e. Github)
    using an URL with a few key OAuth parameters.
    """
    github = OAuth2Session(client_id)
    authorization_url, state = github.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    return redirect(authorization_url)


# Step 2: User authorization, this happens on the provider.

@app.route("/gh-callback", methods=["GET"])
def callback():
    """ Step 3: Retrieving an access token.

    The user has been redirected back from the provider to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """

    github = OAuth2Session(client_id, state=session['oauth_state'])
    token = github.fetch_token(token_url, client_secret=client_secret,
                               authorization_response=request.url)

    # At this point you can fetch protected resources but lets save
    # the token to be able to reuse later
    session['oauth_token'] = token

    # Save some basic profile info and avatar image in the session
    github = OAuth2Session(client_id, token=session['oauth_token'])
    profile_data = github.get('https://api.github.com/user').json()
    session['gh_id'] = profile_data['id']
    session['gh_login'] = profile_data['login']
    session['avatar'] = profile_data['avatar_url']
    session['is_admin'] = False

    # Crude way to set admin for additional functionality
    if session['gh_id'] in ['1474512']:
        session['is_admin'] = True

    return redirect(url_for('.index'))


@app.route("/profile", methods=["GET"])
def profile():
    """Fetching and displaying profile data using an OAuth 2 token.
    """
    github = OAuth2Session(client_id, token=session['oauth_token'])
    profile_data = github.get('https://api.github.com/user').json()
    return render_template('profile.html',data=profile_data,avatar=profile_data['avatar_url'])


@app.route("/logout", methods=["GET"])
def logout():
    """Log out the user. This will not clear the given GitHub authorization for this app.
    """
    session.clear()
    return redirect(url_for('.index'))


if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

    app.run(debug=True)

