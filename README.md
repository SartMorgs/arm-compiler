# Arm Compiler

This repository consist of an API for a compiler arm cortex M0 processor, which provider a translate from arm's assembly code to binary code. This repository are a block of another bigger project called [arm-sim](http://github.com/arm-sim).

The content of this abstract are:

- How to run it by yourself
- How it works
- How to report bugs and errors
- How to contribute

## How to run it by yourself

You will need docker to run it by yourself to guarantee that it will run like a base environemtn where it was builded. You chan check [this link](https://docs.docker.com/engine/install/) to see how to install and configure docker for your machine.

To run the docker environment you'll need to build a image configured inside of a dockerfile, and after this run this image generating a docker container. For build the image you need to run the bellow command:

```bash
docker build -f arm_compiler_img -t docker/Dockerfile .
```

To run the image that you builded at last command you will use:

```bash
docker run --name arm_compiler -p 8000:8000 -d arm_compiler_img
```

Now you have the API running on your http://localhost:8000 and you can test it using postman or another way to made requests.


## How it works

We have 3 components necessary to build the arm compiler:

- A lexer to indentify all tokens presents into assembly code and also get errors for unexpected token inside of code. 
- A parser to get right order of code's sentences and also identify errors in this way
- Translator is used to return binary code from assembly tokens ordered by code block

The are used [PLY python package]() for lexer and parser component.

## How to report bugs and errors

In case of bugs and problems with arm-sim execution, there can be opened a github's issue in this repository describing clarery the situation. You can find some advices to open a good issue.
