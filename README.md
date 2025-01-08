# weather-app
**WEATHER APPLICATION** 

Project inspiration: madebygps

1. Weather Tracker (Develop Azure compute solutions)
A web application that allows users to track weather updates in real-time for their chosen cities. The system also triggers Azure Functions for alerts when a specific weather threshold is met (like if it's going to rain).

Infrastructure
Azure App Service Web App (Hosting the web application)
Azure Container Registry (Storing Docker images for the app)
Azure Container Instance (Running the containers for development/testing)
Azure Functions (Weather alert system)
Azure Container Apps (Running the containers in production)
Diagram
User 
|-> Web Application (Hosted on Azure App Service Web App)
   |-> Weather Alerts (Azure Functions)
      |-> Docker Images (Azure Container Registry)
         |-> Testing Containers (Azure Container Instance)
            |-> Running Containers (Azure Container Apps)
Implementation Guide
Create an Azure App Service Web App.
Develop a basic web application that uses weather APIs.
Containerize the application.
Publish the container image to Azure Container Registry.
Test the application using Azure Container Instance.
Implement an Azure Function to send alerts when a specified weather threshold is met.
Integrate Azure Function with your web application.
Deploy the web application to Azure Container Apps.
Setup a CI/CD pipeline for your application and Function.
Setup Application insights and Azure monitor
Push to GitHub
Document