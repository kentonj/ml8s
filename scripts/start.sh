#!/bin/bash
# take a positional argument, which defaults to "serve". can optionally provide "train" followed by src.training.mytrainingscript
action=${1:-"serve"}
additional_args=${@:2}

serve () {
    # start the webserver to serve model results
    GUNICORN_WORKERS=${GUNICORN_WORKERS:-4}
    PORT=5000
    # use gunicorn which is a robust WSGI that serves a Flask app.
    gunicorn -w $GUNICORN_WORKERS app -b :$PORT
}

train () {
    # train the specified model
    # ex. docker-compose run model-service train src.training.iris_classifier
    echo "training module: $additional_args"
    python -m $additional_args
}

# evalute either "train" or "serve"
if [ "$action" = "serve" ]; then
    serve
elif [ "$action" = "train" ]; then
    train
else
    echo "only serve or train are valid actions, you provided: $action"
    exit 1
fi
