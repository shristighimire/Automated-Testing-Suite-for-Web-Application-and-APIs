# Automated Testing Suite for Web Application and APIs

## Overview
This project demonstrates automated testing for web applications and APIs using Selenium for web testing, Postman for API testing, and .NET for integration. It includes both unit and integration tests to ensure the software works as expected.

## Requirements
- .NET SDK
- Selenium WebDriver
- Postman (for API testing)
- NUnit
- RestSharp
- ChromeDriver

## Setting up the Environment
1. Clone the repository:
## git clone https://github.com/yourusername/automated-testing-suite.git
2. Install the necessary NuGet packages:
## Install-Package Selenium.WebDriver Install-Package RestSharp
## Running the Tests
- For web tests, run the following command:
## dotnet restore
text

## Running the Tests
- For web tests:
dotnet test ./src/Web/WebTests.csproj
text

- For API tests:
dotnet test ./src/API/ApiTests.csproj
text

- To run all tests:
./test-runner/run-tests.bat
text

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Create a LICENSE file in the root directory with the MIT License text.
Update the WebTests.cs file in src/Web/:
csharp
using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace WebTests
{
    [TestFixture]
    public class WebTests
    {
        private IWebDriver driver;

        [SetUp]
        public void SetUp()
        {
            driver = SeleniumDriverSetup.GetDriver();
            driver.Navigate().GoToUrl("https://www.example.com");
        }

        [Test]
        public void TestHomePageTitle()
        {
            var title = driver.Title;
            Assert.AreEqual("Expected Page Title", title);
        }

        [Test]
        public void TestLoginForm()
        {
            driver.FindElement(By.Id("username")).SendKeys("testuser");
            driver.FindElement(By.Id("password")).SendKeys("password123");
            driver.FindElement(By.Id("loginButton")).Click();

            var dashboard = driver.FindElement(By.Id("dashboard"));
            Assert.IsTrue(dashboard.Displayed);
        }

        [TearDown]
        public void TearDown()
        {
            driver.Quit();
        }
    }
}
Update the ApiTests.cs file in src/API/:
csharp
using NUnit.Framework;
using RestSharp;

namespace ApiTests
{
    [TestFixture]
    public class ApiTests
    {
        private RestClient client;

        [SetUp]
        public void SetUp()
        {
            client = new RestClient("https://api.example.com");
        }

        [Test]
        public void TestApiResponse()
        {
            var request = new RestRequest("/endpoint", Method.GET);
            var response = client.Execute(request);

            Assert.AreEqual(200, (int)response.StatusCode);
            Assert.IsTrue(response.Content.Contains("expected value"));
        }

        [Test]
        public void TestApiPostRequest()
        {
            var request = new RestRequest("/endpoint", Method.POST);
            request.AddJsonBody(new { name = "test" });
            var response = client.Execute(request);

            Assert.AreEqual(201, (int)response.StatusCode);
        }
    }
}
Create the run-tests.bat file in the test-runner directory:
text
@echo off
echo Running Selenium Web Tests...
dotnet test ../src/Web/WebTests.csproj

echo Running API Tests...
dotnet test ../src/API/ApiTests.csproj
