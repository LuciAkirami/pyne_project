import pynecone as pc

config = pc.Config(
    app_name="pyne_project",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
