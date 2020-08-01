# ML8S
This is a template for training and serving machine learning models. 
The service consists of a docker-ized flask application, which will ultimately be deployed in a kubernetes cluster. Before running the machine learning service in Kubernetes, we can run it using docker-compose to ensure that everything works correctly before putting it into kubernetes.

In order to predict on some model, you will first need to train the classifier. In this case, there is a training script located at `src/training/iris_classifier/train.py`. It is important to train this model in the same environment that it will be served in, so see the below training section for how to run your training script in the container.

## Training 
- run `docker-compose run ml8s train src.training.iris_classifier.train`. 
    - This will pass the `train` command to the container's entrypoint script (see `scripts/start.sh`), and then specifies the python module that you wish to train. The model saves to `./src/models/iris_classifier.model` within the container, which is mounted to your local filesystem in `docker-compose.yml`. 
- run `docker-compose build`. This is necessary to now bake your model into the container.
## Serving ML8s
- make sure that you've trained a model and baked it into the container with the steps above.
### docker-compose
- run `docker-compose up`.
    - This will start the ml8s service and use the default container command `serve` to serve a flask api.
### Minikube
- If you have an actual kube cluster, use that. If not, install minikube to run a micro cluster.
- more instructions to come.