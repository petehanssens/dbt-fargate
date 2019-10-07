# Links used

https://github.com/nathanpeck/aws-cloudformation-fargate


## Steps to setup

1. Run fargate.yaml in the cloudformation console
2. Repeate for dbt-task-def.yaml
3. Optionally you can run a long running "fargate-container.yaml" webserver if you like - I'm hoping to extend the code to host dbt docs there.
4. Go to the sls-dbt folder to create the lambda function to trigger the fargate container.