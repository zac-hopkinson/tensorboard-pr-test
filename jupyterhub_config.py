def setup_tensorboard_proxy(spawner):
    if spawner.server:
        env = spawner.server.base_url
        return env + "proxy/%PORT%/"
    return ""

c.Spawner.environment = {
    "TENSORBOARD_PROXY_URL": setup_tensorboard_proxy,
    # Potentially an alternative method without the callable:
    # "TENSORBOARD_PROXY_URL": "/hub/user-redirect/proxy/%PORT%/",
}

c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
