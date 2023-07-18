FROM microservice:base

RUN apk --no-cache add build-base

ADD app /home/app
WORKDIR /home/app
RUN make clean
RUN make
