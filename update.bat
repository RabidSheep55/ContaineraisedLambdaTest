docker build -t is-exact-equal:lambda .
docker tag is-exact-equal:lambda 421311628602.dkr.ecr.eu-west-2.amazonaws.com/is-exact-equal:lambda
docker push 421311628602.dkr.ecr.eu-west-2.amazonaws.com/is-exact-equal:lambda
aws lambda update-function-code --function-name isExactEqual --image-uri 421311628602.dkr.ecr.eu-west-2.amazonaws.com/is-exact-equal:lambda
