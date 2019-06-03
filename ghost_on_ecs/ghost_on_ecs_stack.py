from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    cdk,
)


class GhostOnEcsStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, *kwargs)

        # Create VPC and Fargate Cluster
        # NOTE: Limit AZs to avoid reaching resource quotas
        vpc = ec2.VpcNetwork(
            self, "MyGhostOnEcsVpc",
            max_a_zs=2
        )

        cluster = ecs.Cluster(
            self, 'Ec2GhostOnEcsCluster',
            vpc=vpc
        )

        fargate_service = ecs.LoadBalancedFargateService(
            self, "FargateGhostOnEcsService",
            cluster=cluster,
            image=ecs.ContainerImage.from_registry("ghost")
        )

        cdk.CfnOutput(
            self, "LoadBalancerDNS",
            value=fargate_service.load_balancer.dns_name
        )
