import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="ghost_on_ecs",
    version="0.0.1",

    description="Simple AWS CDK Python app which deploys the Ghost container to ECS Fargate",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Sam Keen",

    package_dir={"": "ghost_on_ecs"},
    packages=setuptools.find_packages(where="ghost_on_ecs"),

    install_requires=[
        "aws-cdk.cdk",
        "aws_ec2",
        "aws_ecs",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
