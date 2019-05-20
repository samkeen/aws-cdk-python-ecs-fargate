#!/usr/bin/env python3

from aws_cdk import cdk

from ghost_on_ecs.ghost_on_ecs_stack import GhostOnEcsStack


app = cdk.App()
GhostOnEcsStack(app, "ghost-on-ecs-cdk-1")

app.run()
