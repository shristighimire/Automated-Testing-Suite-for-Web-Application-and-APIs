@echo off
echo Running Selenium Web Tests...
dotnet test ./src/Web/WebTests.csproj

echo Running API Tests...
dotnet test ./src/API/ApiTests.csproj
