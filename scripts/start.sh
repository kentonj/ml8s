#!/bin/bash
# take a positional argument, which defaults to "serve". can optionally provide "train" followed by src.training.mytrainingscript
action=${1:-"serve"}
additional_args=${@:2}

serve () {
    # start the webserver to serve model results
    GUNICORN_WORKERS=${GUNICORN_WORKERS:-4}
    PORT=5000
    if [ "$STAGE" = "production" ]; then
        # production stage, we will want to use gunicorn to run our app rather than flask's development server
        gunicorn -w $GUNICORN_WORKERS app -b :$PORT
    else
        # we are not in the production stage, use flask to run the app as a development server
        export FLASK_ENV=development
        flask run --host 0.0.0.0 --port $PORT
    fi
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
