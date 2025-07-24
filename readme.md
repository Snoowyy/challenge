# Meli Challenge

## Description

This project is a monorepo that contains all the code for the Meli Challenge. The project is divided into two main parts: the frontend and the backend. The frontend is a Vue3 application that interacts with the backend through HTTP requests. The backend is a FastAPI application that handles all the business logic and data management.

Also included in this project is a generator that uses the Ollama library to generate components for the frontend. The generator takes in a set of characteristics and generates a list of components that meet those characteristics. The generator is used to generate the components for the Meli Challenge.

Same as the generator, i used Ollama to generate a enrichment endpoint that takes the characteristics of a product and returns a list of related products. This is used to enrich the product information with related products.

## Table of Contents

- [Meli Challenge](#meli-challenge)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Technologies](#technologies)
  - [Installation](#installation)
  - [Running the project](#running-the-project)
  - [API Documentation](#api-documentation)
  - [How it's going work](#how-its-going-work)
    - [Archiecture](#archiecture)
    - [Explain](#explain)

## Technologies

- Python 3.10 or higher
- Node.js 22.14 or higher
- FastAPI
- Vue 3
- Ollama

## Installation

To install the project, you will need to have Python installed and node installed. Once you have both installed, you can run the following commands to install the project dependencies:

```
pip install -r backend/requirements.txt
pip install -r generator/requirements.txt
```

Then, you can install the frontend dependencies by navigating to the `frontend` directory and running:

```
cd frontend
npm install
```

Also if you want to use the generator and consume the enrichment endpoint, you will need to install ollama and pull the model `ollama/7b-instruct`

With this, you will have all the dependencies installed and ready to run the project.

## Running the project

With all the dependencies installed, you can run the project by navigating to the `backend` directory and running:

```
uvicorn main:app --reload
```

This will start the backend server and you can access the API at `http://localhost:8000/docs`.

To run the frontend, navigate to the `frontend` directory and run:

```
npm run dev
```

This will start the frontend server and you can access the frontend at `http://localhost:5173`.

To run the generator, navigate to the `generator` directory and run:

```
python image_to_code.py
```

This will generate the components for the frontend based on the image provided.

Note: if you want to use another port for the backend or frontend, you can specify the port using the `--port` option for uvicorn and the `--port` option for npm respectively.

## API Documentation

The API documentation can be found at `http://localhost:8000/docs`.

## How it's going work 🔨

### Archiecture 🏛️

The architecture of the project is designed to be modular and scalable. The backend is built using FastAPI and follow the hexagonal architecture pattern. The frontend is built using Vue 3 and follows the single-page application (SPA) architecture pattern.

### Explain 🔍

The project architecture in backend is divided into three main parts: the domain, the application, the ports and the infrastructure. The domain layer contains the business logic and data management, the application layer contains the use cases and the ports layer contains the interfaces that the application uses to interact with the domain layer. The infrastructure layer contains the adapters and the repositories that the application uses to interact with the external systems.

The frontend is divided into two main parts: the components and the views. The components folder contains all the Vue 3 components that are used in the frontend. The views folder contains all the Vue 3 views that are used to render the components.

### Challenges faced 🧗

For this project, i used the Ollama library for different purposes. this implementation include the following challenges:

- How to use the Ollama library to generate components for the frontend?
  - Response: For this challenge i need created a clean promp that only contains the response as a JSON object, without any additional explanations and implement other promp that check the vue component and the correctness of the syntax.
- How to use vue components in the frontend?
  - Response: Although the model did not provide all the necessary components because the refinement was very short and the model used was only 7 billion, I was able to take the bases of what it gave me to start working from there.

## Improvements and trade offs 📈

1. What would you improve from your code? why?

   - [ ] Add unit tests
   - [ ] Add more error handling
   - [ ] Use a robust ORM
   - [ ] Use a robust authentication middleware
   - [ ] Use a robust rate limiting service
   - [ ] Use a robust caching service to the endpoints that use the Ollama library
   - [ ] Use a robust logging service
   - [ ] Improve the frontend performance
   - [ ] Better language model prompts
   - [ ] Better image processing

2. What would you trade off from your code? why?

   - [ ] Add more features to the frontend
   - [ ] Improve the frontend architecture
