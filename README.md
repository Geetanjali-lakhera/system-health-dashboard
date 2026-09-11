# System Health Dashboard API

A lightweight Flask-based System Health Dashboard API built as part of the C456 SRE Mini Project.

## Features

- Health status endpoint
- Application version endpoint
- Environment configuration through an environment variable
- Overall application status endpoint
- Request metrics endpoint
- Application information endpoint

## API Endpoints

| Endpoint | Description |
|---|---|
| `/health` | Returns application health status |
| `/version` | Returns current application version |
| `/environment` | Returns configured environment |
| `/status` | Returns overall application status |
| `/metrics` | Returns request count |


## Merge Conflict Resolution

A controlled merge conflict was intentionally created between `develop` and `feature/improve-app`.

Both branches modified the application version in `app.py`:

- `develop` changed the version to `1.0.1`
- `feature/improve-app` changed the version to `1.1.0`

Git detected the conflicting changes and stopped the merge. The conflict was manually resolved by keeping version `1.1.0`. The resolved file was staged and the merge was completed with the commit:

`merge: resolve version conflict`

This demonstrated how Git identifies conflicting changes and how a developer can manually resolve and commit the result.
